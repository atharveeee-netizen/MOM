import numpy as np
import wfdb
import os
import glob
import time
import json
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.signal import find_peaks

def nlms_filter(primary, reference, mu=0.05, filter_order=32):
    """
    Normalized Least Mean Squares (NLMS) adaptive filter.
    Benchmark configuration: 32-tap FIR filter, mu = 0.05, epsilon = 1e-8.
    """
    n = len(primary)
    w = np.zeros(filter_order)
    y = np.zeros(n)
    e = np.zeros(n)
    
    # Pad reference signal to handle the first few samples
    ref_padded = np.pad(reference, (filter_order - 1, 0), 'constant')
    
    for i in range(n):
        x = ref_padded[i:i+filter_order][::-1]  # Get current window (reversed)
        norm_factor = np.dot(x, x) + 1e-8       # Avoid division by zero
        
        y[i] = np.dot(w, x)
        e[i] = primary[i] - y[i]
        
        w = w + (mu / norm_factor) * e[i] * x
        
    return e, y

def evaluate_split(dataset_path, split_file):
    print("Running Classical NLMS Baseline Evaluation...")
    
    with open(split_file, "r") as f:
        splits = json.load(f)
        
    test_subjects = splits.get("test", [])
    print(f"Test subjects: {test_subjects}")
    
    all_rmse = []
    all_mae = []
    all_times = []
    mqrs_counts = []
    
    for sub in test_subjects:
        # Find all segments for this subject (channel 1 as primary, channel 2 as reference)
        pattern = os.path.join(dataset_path, 'mixture', f'{sub}_1_*.dat')
        mixture_files = glob.glob(pattern)
        
        print(f"Found {len(mixture_files)} segments for subject {sub}")
        
        for mix_dat in mixture_files:
            base_name = os.path.basename(mix_dat).replace('.dat', '')
            seg_id = base_name.replace(f'{sub}_1_', '')
            
            mix_file = os.path.join(dataset_path, 'mixture', f'{sub}_1_{seg_id}')
            ref_file = os.path.join(dataset_path, 'mixture', f'{sub}_2_{seg_id}')
            fecg_file = os.path.join(dataset_path, 'fecg_ground', f'{sub}_1_{seg_id}')
            
            if not os.path.exists(ref_file + ".dat") or not os.path.exists(fecg_file + ".dat"):
                continue
                
            record_mix = wfdb.rdrecord(mix_file)
            record_ref = wfdb.rdrecord(ref_file)
            record_ground = wfdb.rdrecord(fecg_file)
            
            primary = record_mix.p_signal.flatten() * 1000  # Convert to mV
            reference = record_ref.p_signal.flatten() * 1000
            ground_truth = record_ground.p_signal.flatten() * 1000
            
            # Simple Maternal QRS detection on reference signal
            # Thresholding above a certain amplitude in mV
            peaks, _ = find_peaks(reference, height=0.5, distance=100)
            mqrs_counts.append(len(peaks))
            
            # Run NLMS with timing
            start_time = time.time()
            fecg_est, mecg_est = nlms_filter(primary, reference, mu=0.05, filter_order=32)
            end_time = time.time()
            
            # Metrics
            rmse = np.sqrt(mean_squared_error(ground_truth, fecg_est))
            mae = mean_absolute_error(ground_truth, fecg_est)
            
            all_rmse.append(rmse)
            all_mae.append(mae)
            all_times.append(end_time - start_time)
            
    if all_rmse:
        print("\n--- NLMS EVALUATION RESULTS (Test Split) ---")
        print(f"Total segments evaluated: {len(all_rmse)}")
        print(f"Average Maternal QRS detected per segment: {np.mean(mqrs_counts):.2f}")
        print(f"Mean RMSE: {np.mean(all_rmse):.4f} mV")
        print(f"Mean MAE:  {np.mean(all_mae):.4f} mV")
        print(f"Mean Processing Time per segment: {np.mean(all_times):.4f} seconds")
        print("---------------------------------------------")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default=os.path.join(os.path.dirname(__file__), "..", "pretrained", "W-NETR-for-FECG-extraction", "ADFECGDB"), help="Path to generated ADFECGDB")
    parser.add_argument("--split", type=str, default=os.path.join(os.path.dirname(__file__), "..", "..", "experiments", "data_split", "adfe_cgdb_split.json"), help="Path to split JSON")
    args = parser.parse_args()
    
    evaluate_split(args.dataset, args.split)
