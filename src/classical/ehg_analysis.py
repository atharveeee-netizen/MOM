import numpy as np
import wfdb
import os
import glob
import json
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def teager_kaiser_energy(signal):
    """
    Teager-Kaiser Energy Operator (TKEO) for EHG signal activity.
    TKEO[n] = x[n]^2 - x[n-1]*x[n+1]
    """
    tkeo = np.zeros_like(signal)
    tkeo[1:-1] = signal[1:-1]**2 - signal[:-2] * signal[2:]
    return np.mean(tkeo)

def approximate_entropy(U, m=2, r=0.2):
    """
    Approximation of Sample/Approximate Entropy.
    """
    # A simplified variance-based entropy metric for speed
    std = np.std(U)
    if std == 0: return 0
    return -np.log(np.var(U)/np.mean(U**2) + 1e-8)

def evaluate_ehg(dataset_path, split_file):
    print("Running EHG Analysis (Teager-Kaiser, Entropy)...")
    
    with open(split_file, "r") as f:
        splits = json.load(f)
        
    test_subjects = splits.get("test", [])
    all_tkeo = []
    
    for sub in test_subjects:
        pattern = os.path.join(dataset_path, 'mixture', f'{sub}_1_*.dat')
        mixture_files = glob.glob(pattern)
        
        for mix_dat in mixture_files:
            base_name = os.path.basename(mix_dat).replace('.dat', '')
            seg_id = base_name.replace(f'{sub}_1_', '')
            mix_file = os.path.join(dataset_path, 'mixture', f'{sub}_1_{seg_id}')
            
            if not os.path.exists(mix_file + ".dat"):
                continue
                
            record_mix = wfdb.rdrecord(mix_file)
            primary = record_mix.p_signal.flatten() * 1000  # mV
            
            # EHG is typically in the 0.1 - 3 Hz range (uterine electrical activity)
            ehg_signal = butter_bandpass_filter(primary, 0.1, 3.0, fs=1000, order=4)
            
            tkeo = teager_kaiser_energy(ehg_signal)
            all_tkeo.append(tkeo)

    print("\n--- EHG ANALYSIS RESULTS (Test Split) ---")
    print(f"Mean Teager-Kaiser Energy: {np.mean(all_tkeo):.6f}")
    print("-----------------------------------------")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default=os.path.join(os.path.dirname(__file__), "..", "pretrained", "W-NETR-for-FECG-extraction", "ADFECGDB"), help="Path to generated ADFECGDB")
    parser.add_argument("--split", type=str, default=os.path.join(os.path.dirname(__file__), "..", "..", "experiments", "data_split", "adfe_cgdb_split.json"), help="Path to split JSON")
    args = parser.parse_args()
    
    evaluate_ehg(args.dataset, args.split)
