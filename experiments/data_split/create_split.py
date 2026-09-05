import json
import os

def create_splits():
    # ADFECGDB has 5 subjects (recordings): r01, r04, r07, r08, r10
    # To guarantee zero data leakage, we perform a strict subject-wise split.
    # We will use r01, r04, r07, r08 for filter tuning/validation (train/val)
    # and strictly reserve r10 for final unseen testing.
    
    splits = {
        "train": ["r01", "r04", "r07"],
        "val": ["r08"],
        "test": ["r10"]
    }
    
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    
    with open(os.path.join(os.path.dirname(__file__), "adfe_cgdb_split.json"), "w") as f:
        json.dump(splits, f, indent=4)
        
    print("Created strict subject-wise split for ADFECGDB in adfe_cgdb_split.json")
    print(json.dumps(splits, indent=2))

if __name__ == "__main__":
    create_splits()
