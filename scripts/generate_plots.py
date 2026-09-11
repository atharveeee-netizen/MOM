import os
import numpy as np
import matplotlib.pyplot as plt

def generate_ecg_train(t, rate_hz, fs):
    ecg = np.zeros_like(t)
    period_samples = int(np.round(fs / rate_hz))
    pulse = np.array([0]*10 + [0.1, -0.15, 1.0, -0.2, 0.1] + [0]*10)
    p_len = len(pulse)
    
    idx = 100 # start offset
    while idx + p_len < len(ecg):
        ecg[idx:idx+p_len] = pulse
        idx += period_samples
        
    # Add baseline wander
    ecg += 0.05 * np.sin(2 * np.pi * 0.5 * t)
    return ecg

def run_simulation():
    fs = 1000
    L = 10
    mu = 0.05
    epsilon = 1e-4

    t = np.arange(4000) / fs
    
    m_rate = 80 / 60
    f_rate = 140 / 60
    
    m_ecg = generate_ecg_train(t, m_rate, fs)
    f_ecg = generate_ecg_train(t, f_rate, fs) * 0.15
    
    noise = 0.02 * np.random.randn(len(t))
    
    # Simulate maternal transfer to abdomen (slight delay & scale)
    m_abd = np.roll(m_ecg, 2) * 0.8
    abd_sig = m_abd + f_ecg + noise
    ref_sig = m_ecg
    
    N = len(abd_sig)
    w = np.zeros(L)
    e = np.zeros(N)
    
    # NLMS
    for n in range(L, N):
        x_n = ref_sig[n:n-L:-1]
        y_n = np.dot(w, x_n)
        e[n] = abd_sig[n] - y_n
        
        norm_x = np.dot(x_n, x_n)
        w = w + (mu * e[n] * x_n) / (epsilon + norm_x)

    os.makedirs('../results', exist_ok=True)
    
    plt.figure(figsize=(10, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, abd_sig, 'b')
    plt.title('Abdominal Mixture (Maternal + Fetal + Noise)')
    plt.ylabel('Amplitude (mV)')
    plt.xlim([1, 4])
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(t, ref_sig, 'k')
    plt.title('Thoracic Reference (Maternal ECG)')
    plt.ylabel('Amplitude (mV)')
    plt.xlim([1, 4])
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(t, e, 'r')
    plt.title('Extracted Fetal ECG (NLMS Residual)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (mV)')
    plt.xlim([1, 4])
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('../results/nlms_convergence_results.png', dpi=300)
    print("Graph saved to results/nlms_convergence_results.png")

if __name__ == '__main__':
    run_simulation()
