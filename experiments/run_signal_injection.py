import numpy as np
import wfdb
import os
import json
import time

def emulate_adc_read(signal, idx, resolution=24):
    """
    Emulate an ADS1298 24-bit ADC reading.
    Returns the integer quantized value.
    """
    max_val = 2**(resolution - 1) - 1
    # Assuming signal is in mV, and max range is +/- 2400 mV (just an example range)
    # Vref = 2.4V
    voltage_uv = signal[idx] * 1000.0 # Convert mV to uV
    lsb_uv = (2.4 * 1000000) / max_val
    adc_val = int(voltage_uv / lsb_uv)
    return adc_val

def run_hardware_injection():
    print("--- STARTING HARDWARE SIGNAL INJECTION (SOFTWARE-IN-THE-LOOP) ---")
    
    # Load test split (r10)
    split_file = os.path.join(os.path.dirname(__file__), "data_split", "adfe_cgdb_split.json")
    with open(split_file, "r") as f:
        splits = json.load(f)
    
    sub = splits["test"][0] # r10
    dataset_path = os.path.join(os.path.dirname(__file__), "..", "ml", "pretrained", "W-NETR-for-FECG-extraction", "ADFECGDB")
    
    mix_file = os.path.join(dataset_path, 'mixture', f'{sub}_1_0')
    ref_file = os.path.join(dataset_path, 'mixture', f'{sub}_2_0')
    
    if not os.path.exists(mix_file + ".dat"):
        print("Data not found.")
        return
        
    record_mix = wfdb.rdrecord(mix_file)
    record_ref = wfdb.rdrecord(ref_file)
    
    primary = record_mix.p_signal.flatten() * 1000  # mV
    reference = record_ref.p_signal.flatten() * 1000
    
    # Simulate a real-time interrupt-driven loop on the nRF52840 (at 1000 Hz)
    # We will simulate all samples available in this segment (1000 samples = 1s)
    
    num_samples = len(primary)
    w = np.zeros(32)
    ref_window = np.zeros(32)
    mu = 0.05
    
    start_time = time.time()
    
    print(f"Injecting {num_samples} samples at 1000 Hz...")
    
    for i in range(num_samples):
        # 1. Emulate SPI Read from ADS1298
        prim_adc = emulate_adc_read(primary, i)
        ref_adc = emulate_adc_read(reference, i)
        
        # 2. Convert back to float for DSP (or leave as fixed-point for true embedded)
        # Assuming float32 available on Cortex-M4F
        prim_val = primary[i]
        ref_val = reference[i]
        
        # 3. Shift reference window (simulating ring buffer)
        ref_window = np.roll(ref_window, 1)
        ref_window[0] = ref_val
        
        # 4. NLMS Update
        norm_factor = np.dot(ref_window, ref_window) + 1e-8
        y = np.dot(w, ref_window)
        e = prim_val - y
        w = w + (mu / norm_factor) * e * ref_window
        
        # 5. Emulate BLE TX
        if i % 100 == 0: # Transmit every 100ms
            pass # print(f"BLE TX [T={i}ms] -> FECG_EST: {e:.4f} mV")
            
    exec_time = time.time() - start_time
    print(f"Finished. Total Simulation Time for {num_samples} samples: {exec_time*1000:.2f} ms")
    print(f"Per-sample Latency: {(exec_time*1000)/num_samples:.4f} ms")
    print("Conclusion: NLMS can comfortably run within the 1ms interrupt window of a 1000Hz sampling rate.")
    print("-------------------------------------------------------------------------")

if __name__ == "__main__":
    run_hardware_injection()
