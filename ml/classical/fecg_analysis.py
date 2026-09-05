import numpy as np
import wfdb
import os
import glob
import json
from scipy.signal import find_peaks
import time

def calculate_fhr(peaks, fs=1000):
    """
    Calculate Fetal Heart Rate from R-peaks.
    peaks: indices of detected peaks
    fs: sampling frequency (default 1000 Hz for ADFECGDB)
    """
    if len(peaks) < 2:
        return 0, 0
    rr_intervals = np.diff(peaks) / fs  # RR in seconds
    hr = 60.0 / rr_intervals
    mean_hr = np.mean(hr)
    return mean_hr, rr_intervals

def signal_quality_index(signal, peaks):
    """
    Simple Signal Quality Index (SQI): Peak amplitude vs standard deviation of the signal.
    """
    if len(peaks) == 0:
        return 0.0
    peak_amps = signal[peaks]
    snr_est = np.mean(peak_amps) / (np.std(signal) + 1e-8)
    return snr_est

def evaluate_analysis(dataset_path, split_file):
    print("Running Classical FECG Analysis (FQRS, FHR, SQI)...")
    
    with open(split_file, "r") as f:
        splits = json.load(f)
        
    test_subjects = splits.get("test", [])
    
    # We will need the NLMS filter from the same directory to get the FECG signal first
    from nlms import nlms_filter
    
    all_fhr = []
    all_sqi = []
    
    for sub in test_subjects:
        pattern = os.path.join(dataset_path, 'mixture', f'{sub}_1_*.dat')
        mixture_files = glob.glob(pattern)
        
        for mix_dat in mixture_files:
            base_name = os.path.basename(mix_dat).replace('.dat', '')
            seg_id = base_name.replace(f'{sub}_1_', '')
            
            mix_file = os.path.join(dataset_path, 'mixture', f'{sub}_1_{seg_id}')
            ref_file = os.path.join(dataset_path, 'mixture', f'{sub}_2_{seg_id}')
            
            if not os.path.exists(ref_file + ".dat"):
                continue
                
            record_mix = wfdb.rdrecord(mix_file)
            record_ref = wfdb.rdrecord(ref_file)
            
            primary = record_mix.p_signal.flatten() * 1000  # Convert to mV
            reference = record_ref.p_signal.flatten() * 1000
            
            # Get FECG using NLMS
            fecg_est, _ = nlms_filter(primary, reference, mu=0.05, filter_order=32)
            
            # 1. FQRS Detection
            # A simple dynamic threshold based on signal std
            threshold = 1.5 * np.std(fecg_est)
            peaks, _ = find_peaks(fecg_est, height=threshold, distance=300) # Assuming > 300ms between fetal beats (max 200 BPM)
            
            # 2. FHR Calculation
            mean_hr, _ = calculate_fhr(peaks, fs=1000)
            if mean_hr > 0:
                all_fhr.append(mean_hr)
                
            # 3. SQI Calculation
            sqi = signal_quality_index(fecg_est, peaks)
            all_sqi.append(sqi)

    print("\n--- FECG ANALYSIS RESULTS (Test Split) ---")
    print(f"Mean Fetal Heart Rate (FHR): {np.mean(all_fhr):.2f} BPM")
    print(f"Mean Signal Quality Index (SQI): {np.mean(all_sqi):.4f}")
    print("------------------------------------------")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default=os.path.join(os.path.dirname(__file__), "..", "pretrained", "W-NETR-for-FECG-extraction", "ADFECGDB"), help="Path to generated ADFECGDB")
    parser.add_argument("--split", type=str, default=os.path.join(os.path.dirname(__file__), "..", "..", "experiments", "data_split", "adfe_cgdb_split.json"), help="Path to split JSON")
    args = parser.parse_args()
    
    evaluate_analysis(args.dataset, args.split)
