import os
import sys
import yaml
import torch
import time
import numpy as np
from torch.utils.data import DataLoader
from torch.autograd import Variable
import logging

# Symlink path integration for raw W-NETR architecture
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/ai/W-NETR-for-FECG-extraction'))
try:
    from networks_real import build_UNETR
    from util.dataset_real import Dataset
    from monai.data import list_data_collate
except ImportError as e:
    print(f"Warning: W-NETR dependencies not fully available: {e}")

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def pearson_loss(pred, target):
    pred_mean = torch.mean(pred, dim=-1, keepdim=True)
    target_mean = torch.mean(target, dim=-1, keepdim=True)
    pred_std = torch.std(pred, dim=-1, keepdim=True)
    target_std = torch.std(target, dim=-1, keepdim=True)
    cov = torch.mean((pred - pred_mean) * (target - target_mean), dim=-1, keepdim=True)
    pearson_corr = cov / (pred_std * target_std + 1e-8)
    return 1 - torch.mean(pearson_corr)

def calculate_rmse(pred, target):
    return torch.sqrt(torch.nn.MSELoss()(pred, target))

def train_syzygy_orchestrator(config_path):
    cfg = load_config(config_path)
    print(f"--- SYZYGY ORCHESTRATOR: W-NETR FULL TRAINING ---")
    print(f"Experiment: {cfg['experiment']['name']}")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Assigned Device: {device}")
    
    seed = cfg['training']['seeds'][0]
    torch.manual_seed(seed)
    np.random.seed(seed)
    
    # Instantiate exact W-NETR PyTorch Module (Unmodified Architecture)
    model = build_UNETR().to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(), 
        lr=float(cfg['training']['learning_rate']), 
        weight_decay=float(cfg['training']['weight_decay'])
    )
    
    l1_loss = torch.nn.L1Loss()
    
    # Ensure save directory is absolute (since we change CWD later)
    save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', cfg['checkpoints']['save_dir']))
    os.makedirs(save_dir, exist_ok=True)
    
    epochs = cfg['training']['epochs']
    print(f"Starting {epochs}-epoch convergence run. Target End Time: Tomorrow 9 AM")
    
    # Load Datasets using absolute paths to the underlying dataset directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/ai/W-NETR-for-FECG-extraction'))
    
    # WFDB paths in the .npy arrays are relative (e.g., 'ADFECGDB/...'). 
    # We must change the working directory so wfdb.rdsamp resolves them correctly.
    os.chdir(base_dir)
    
    root = cfg['data']['dataset_name']
    print(f"Loading datasets from {os.path.join(base_dir, root)}...")
    trainset = Dataset(root=root, load_set='train', transform=None)
    train_loader = DataLoader(
        trainset, 
        batch_size=cfg['training']['batch_size'], 
        shuffle=True, 
        num_workers=cfg['hardware']['workers'], 
        collate_fn=list_data_collate, 
        pin_memory=False
    )
    
    valset = Dataset(root=root, load_set='val', transform=None)
    val_loader = DataLoader(
        valset, 
        batch_size=cfg['training']['batch_size'], 
        shuffle=False, 
        num_workers=cfg['hardware']['workers'], 
        collate_fn=list_data_collate, 
        pin_memory=False
    )

    best_val_loss = float('inf')
    early_stopping_patience = cfg['training']['early_stopping_patience']
    patience_counter = 0

    print("Initialization complete. Pipeline execution starting...")
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        start_time = time.time()
        
        # Train Loop
        for i, train_data in enumerate(train_loader):
            inputs, fecg_label = train_data
            inputs = np.einsum('ijk->ikj', inputs)
            fecg_label = np.einsum('ijk->ikj', fecg_label)
            
            inputs = Variable(torch.from_numpy(inputs)).float().to(device)
            fecg_label = Variable(torch.from_numpy(fecg_label)).float().to(device)
            
            optimizer.zero_grad()
            
            mecg_pred, fecg_pred = model(inputs)
            
            loss_l1 = l1_loss(fecg_pred, fecg_label)
            loss_p = pearson_loss(fecg_pred, fecg_label)
            
            loss = cfg['loss']['l1_weight'] * loss_l1 + cfg['loss']['pearson_weight'] * loss_p
            
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            
        train_loss = running_loss / len(train_loader)
        
        # Val Loop
        model.eval()
        val_loss = 0.0
        val_rmse = 0.0
        with torch.no_grad():
            for i, val_data in enumerate(val_loader):
                inputs, fecg_label = val_data
                inputs = np.einsum('ijk->ikj', inputs)
                fecg_label = np.einsum('ijk->ikj', fecg_label)
                
                inputs = Variable(torch.from_numpy(inputs)).float().to(device)
                fecg_label = Variable(torch.from_numpy(fecg_label)).float().to(device)
                
                mecg_pred, fecg_pred = model(inputs)
                
                v_loss_l1 = l1_loss(fecg_pred, fecg_label)
                v_loss_p = pearson_loss(fecg_pred, fecg_label)
                v_loss = cfg['loss']['l1_weight'] * v_loss_l1 + cfg['loss']['pearson_weight'] * v_loss_p
                
                val_loss += v_loss.item()
                val_rmse += calculate_rmse(fecg_pred, fecg_label).item()
                
        val_loss /= len(val_loader)
        val_rmse /= len(val_loader)
        
        print(f"Epoch [{epoch+1}/{epochs}] - Time: {time.time()-start_time:.1f}s - Train Loss: {train_loss:.5f} - Val Loss: {val_loss:.5f} - Val RMSE: {val_rmse:.5f} mV")
        
        # Incremental Save
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            save_path = os.path.join(save_dir, 'best_model.pkl')
            torch.save(model.state_dict(), save_path)
            print(f"  --> [SAVED] New best model: RMSE {val_rmse:.5f}")
        else:
            patience_counter += 1
            if patience_counter >= early_stopping_patience:
                print(f"Early stopping triggered after {epoch+1} epochs.")
                break

    print(f"Training Complete. Best Val Loss: {best_val_loss:.5f}")

if __name__ == "__main__":
    cfg_path = os.path.join(os.path.dirname(__file__), '../configs/wnetr_training.yaml')
    train_syzygy_orchestrator(cfg_path)
