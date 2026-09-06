import os
import sys
import yaml
import torch
import time
import numpy as np
from datetime import datetime
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
    print(f"--- SYZYGY ORCHESTRATOR: W-NETR FULL TRAINING ---", flush=True)
    print(f"Experiment: {cfg['experiment']['name']}", flush=True)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Assigned Device: {device}", flush=True)
    
    seed = cfg['training']['seeds'][0]
    torch.manual_seed(seed)
    np.random.seed(seed)
    
    # Instantiate exact W-NETR PyTorch Module (Unmodified Architecture)
    model = build_UNETR().to(device)
    
    # Save directory resolution
    save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', cfg['checkpoints']['save_dir']))
    os.makedirs(save_dir, exist_ok=True)
    ckpt_path = os.path.join(save_dir, 'best_model.pkl')
    
    # Telemetry CSV resolution
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    telemetry_csv = os.path.join(repo_root, 'results', 'training_telemetry.csv')
    
    start_epoch = 0
    best_val_loss = float('inf')
    
    # Check for existing telemetry to resume cleanly
    if os.path.exists(telemetry_csv):
        try:
            with open(telemetry_csv, 'r') as f:
                lines = [l.strip() for l in f if l.strip()]
            if len(lines) > 1:
                # Find last completed epoch and best val loss
                last_epoch = 0
                for line in lines[1:]:
                    parts = line.split(',')
                    if len(parts) >= 7:
                        ep = int(parts[0])
                        vl = float(parts[4])
                        last_epoch = max(last_epoch, ep)
                        best_val_loss = min(best_val_loss, vl)
                start_epoch = last_epoch
                print(f"Found existing telemetry with {last_epoch} completed epochs. Best Val Loss: {best_val_loss:.5f}", flush=True)
        except Exception as e:
            print(f"Note: Could not parse telemetry CSV ({e}). Starting fresh or from checkpoint.", flush=True)
            
    # Load weights from checkpoint if available
    if os.path.exists(ckpt_path):
        try:
            state_dict = torch.load(ckpt_path, map_location=device)
            model.load_state_dict(state_dict)
            print(f"Loaded existing checkpoint from {ckpt_path}! Resuming training from Epoch {start_epoch + 1}.", flush=True)
        except Exception as e:
            print(f"Warning: Failed to load checkpoint ({e}). Starting from random initialization.", flush=True)
    else:
        print("No prior checkpoint found. Starting initial weights.", flush=True)
        
    optimizer = torch.optim.AdamW(
        model.parameters(), 
        lr=float(cfg['training']['learning_rate']), 
        weight_decay=float(cfg['training']['weight_decay'])
    )
    
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, 
        mode='min', 
        factor=0.5, 
        patience=10, 
        min_lr=1e-6
    )
    
    l1_loss = torch.nn.L1Loss()
    epochs = cfg['training']['epochs']
    print(f"Configured for {epochs} total epochs. Starting at Epoch {start_epoch + 1}...", flush=True)
    
    # Load Datasets using absolute paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/ai/W-NETR-for-FECG-extraction'))
    os.chdir(base_dir)
    
    root = cfg['data']['dataset_name']
    print(f"Loading datasets from {os.path.join(base_dir, root)}...", flush=True)
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

    early_stopping_patience = cfg['training'].get('early_stopping_patience', 500)
    patience_counter = 0

    print("Initialization complete. Pipeline execution running...", flush=True)
    target_cutoff = datetime(2026, 9, 7, 12, 0, 0)
    
    for epoch in range(start_epoch, epochs):
        now = datetime.now()
        if now >= target_cutoff:
            print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Target end time 12:00 PM (2026-09-07) reached. Completing training run cleanly.", flush=True)
            break

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
        duration = time.time() - start_time
        timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        is_best = False
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            is_best = True
            torch.save(model.state_dict(), ckpt_path)
            best_msg = f" --> [SAVED] New best model: RMSE {val_rmse:.5f}"
        else:
            patience_counter += 1
            best_msg = ""
        # Scheduler step and dynamic LR logging
        curr_lr = optimizer.param_groups[0]['lr']
        scheduler.step(val_loss)
        new_lr = optimizer.param_groups[0]['lr']
        lr_msg = f" | LR: {new_lr:.2e}" if new_lr != curr_lr else ""

        log_line = f"[{timestamp_str}] Epoch [{epoch+1}/{epochs}] - Time: {duration:.1f}s - Train Loss: {train_loss:.5f} - Val Loss: {val_loss:.5f} - Val RMSE: {val_rmse:.5f} mV{best_msg}{lr_msg}"
        print(log_line, flush=True)
        
        # Append to telemetry CSV
        try:
            with open(telemetry_csv, 'a') as f:
                f.write(f"{epoch+1},{timestamp_str},{duration:.1f},{train_loss:.5f},{val_loss:.5f},{val_rmse:.5f},{is_best}\n")
        except Exception as e:
            print(f"Warning: Failed to append to telemetry CSV: {e}", flush=True)
            
        if patience_counter >= early_stopping_patience:
            print(f"[{timestamp_str}] Early stopping triggered after {epoch+1} epochs.", flush=True)
            break

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Training Complete. Best Val Loss: {best_val_loss:.5f}", flush=True)

if __name__ == "__main__":
    cfg_path = os.path.join(os.path.dirname(__file__), '../configs/wnetr_training.yaml')
    train_syzygy_orchestrator(cfg_path)
