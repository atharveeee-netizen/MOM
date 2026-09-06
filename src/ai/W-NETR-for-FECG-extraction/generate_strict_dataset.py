import json
import numpy as np
import os

with open(r'C:\Users\25beevdt047\.gemini\antigravity-ide\scratch\MOM\experiments\data_split\adfe_cgdb_split.json', 'r') as f:
    split_config = json.load(f)

train_subs = split_config['train']
val_subs = split_config['val']
test_subs = split_config['test']

fecg_paths_train, mixture_paths_train = [], []
fecg_paths_val, mixture_paths_val = [], []
fecg_paths_test, mixture_paths_test = [], []

subs = ['r01', 'r04', 'r07', 'r08', 'r10']
channels = ['1', '2', '3', '4']

for sub in subs:
    for ch in channels:
        for kh in range(0, 74):
            # Normal chunk
            fecg_path = f'ADFECGDB/fecg_ground/{sub}_{ch}_{kh}'
            mixture_path = f'ADFECGDB/mixture/{sub}_{ch}_{kh}'
            
            # Offset chunk
            fecg_path_offset = f'ADFECGDB/fecg_ground/{sub}_{ch}_{kh}_5'
            mixture_path_offset = f'ADFECGDB/mixture/{sub}_{ch}_{kh}_5'
            
            paths_to_add = [(fecg_path, mixture_path), (fecg_path_offset, mixture_path_offset)]
            
            for fp, mp in paths_to_add:
                # Ensure the file actually exists (the header file)
                if not os.path.exists(os.path.join(r'C:\Users\25beevdt047\.gemini\antigravity-ide\scratch\MOM\ml\pretrained\W-NETR-for-FECG-extraction', fp + '.hea')):
                    continue
                    
                if sub in train_subs:
                    fecg_paths_train.append(fp)
                    mixture_paths_train.append(mp)
                elif sub in val_subs:
                    fecg_paths_val.append(fp)
                    mixture_paths_val.append(mp)
                elif sub in test_subs:
                    fecg_paths_test.append(fp)
                    mixture_paths_test.append(mp)

# Save arrays
np.save('ADFECGDB/fecg_paths_train.npy', np.array(fecg_paths_train))
np.save('ADFECGDB/mixture_paths_train.npy', np.array(mixture_paths_train))

np.save('ADFECGDB/fecg_paths_val.npy', np.array(fecg_paths_val))
np.save('ADFECGDB/mixture_paths_val.npy', np.array(mixture_paths_val))

np.save('ADFECGDB/fecg_paths_test.npy', np.array(fecg_paths_test))
np.save('ADFECGDB/mixture_paths_test.npy', np.array(mixture_paths_test))

print(f"Train samples: {len(fecg_paths_train)}")
print(f"Val samples: {len(fecg_paths_val)}")
print(f"Test samples: {len(fecg_paths_test)}")
