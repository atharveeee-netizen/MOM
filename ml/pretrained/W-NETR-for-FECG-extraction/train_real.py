from init import Options
from networks_real import build_UNETR
from util.dataset_real import Dataset
import logging
import os
import sys
import numpy as np
import torch
from torch.utils.data import DataLoader
from torch.autograd import Variable
from monai.data import list_data_collate
import time

def main():
    opt = Options().parse()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    root = 'ADFECGDB'

    # Load datasets
    trainset = Dataset(root=root, load_set='train', transform=None)
    train_loader = DataLoader(trainset, batch_size=8, shuffle=True, num_workers=opt.workers, collate_fn=list_data_collate, pin_memory=False)

    valset = Dataset(root=root, load_set='val', transform=None)
    val_loader = DataLoader(valset, batch_size=8, shuffle=False, num_workers=opt.workers, collate_fn=list_data_collate, pin_memory=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f'Using device: {device}')
    
    net = build_UNETR()
    net.to(device)

    # Losses
    l1_loss = torch.nn.L1Loss()
    def pearson_loss(pred, target):
        pred_mean = torch.mean(pred, dim=-1, keepdim=True)
        target_mean = torch.mean(target, dim=-1, keepdim=True)
        pred_std = torch.std(pred, dim=-1, keepdim=True)
        target_std = torch.std(target, dim=-1, keepdim=True)
        
        cov = torch.mean((pred - pred_mean) * (target - target_mean), dim=-1, keepdim=True)
        pearson_corr = cov / (pred_std * target_std + 1e-8)
        return 1 - torch.mean(pearson_corr)

    optimizer = torch.optim.AdamW(net.parameters(), lr=1e-4, weight_decay=1e-5)
    
    best_val_loss = float('inf')
    
    print("Starting AURA-MOM PRO Overnight Validation Training...")
    
    os.makedirs('models', exist_ok=True)
    # Epoch Loop
    for epoch in range(1):
        net.train()
        running_loss = 0.0
        start_time = time.time()
        
        # Train Loop
        for i, train_data in enumerate(train_loader):
            if i > 1:
                break
            inputs, fecg_label = train_data
            
            inputs = np.einsum('ijk->ikj', inputs)
            fecg_label = np.einsum('ijk->ikj', fecg_label)
            
            inputs = Variable(torch.from_numpy(inputs)).float().to(device)
            fecg_label = Variable(torch.from_numpy(fecg_label)).float().to(device)
            
            optimizer.zero_grad()
            
            mecg_pred, fecg_pred = net(inputs)
            
            # Loss combining L1 (sparsity/amplitude) and Pearson (morphology)
            loss_l1 = l1_loss(fecg_pred, fecg_label)
            loss_p = pearson_loss(fecg_pred, fecg_label)
            loss = loss_l1 + 0.1 * loss_p
            
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            
        train_loss = running_loss / min(2, len(train_loader))
        
        # Val Loop
        net.eval()
        val_loss = 0.0
        with torch.no_grad():
            for i, val_data in enumerate(val_loader):
                if i > 1:
                    break
                inputs, fecg_label = val_data
                
                inputs = np.einsum('ijk->ikj', inputs)
                fecg_label = np.einsum('ijk->ikj', fecg_label)
                
                inputs = Variable(torch.from_numpy(inputs)).float().to(device)
                fecg_label = Variable(torch.from_numpy(fecg_label)).float().to(device)
                
                mecg_pred, fecg_pred = net(inputs)
                
                v_loss_l1 = l1_loss(fecg_pred, fecg_label)
                v_loss_p = pearson_loss(fecg_pred, fecg_label)
                v_loss = v_loss_l1 + 0.1 * v_loss_p
                
                val_loss += v_loss.item()
                
        val_loss /= min(2, len(val_loader))
        
        print(f"Epoch [{epoch+1}/1] - Time: {time.time()-start_time:.1f}s - Train Loss: {train_loss:.5f} - Val Loss: {val_loss:.5f}")
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            print("  --> New best model saved")
            torch.save(net.state_dict(), 'models/best_model.pkl')

    print("Training Complete. Best Val Loss:", best_val_loss)

if __name__ == "__main__":
    main()
