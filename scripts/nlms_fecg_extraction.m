% nlms_fecg_extraction.m
% AURA-MOM PRO
% Fetal ECG Extraction using Normalized Least Mean Squares (NLMS)
% This script demonstrates the adaptive filtering cancellation of the maternal ECG
% from an abdominal recording to reveal the fetal ECG.

function nlms_fecg_extraction()
    % Parameters
    fs = 1000; % Sample rate (Hz)
    L = 10; % Filter length (number of taps)
    mu = 0.05; % Step size
    epsilon = 1e-4; % Regularization constant

    % Generate simulated test data (since ADFECGDB requires physionet download)
    % For demonstration, we construct a synthetic maternal and fetal mixture
    t = (0:4000-1)' / fs;
    
    % Synthetic Maternal ECG (reference) - simplified
    maternal_rate = 80 / 60; % 80 BPM
    m_ecg = generate_ecg_train(t, maternal_rate, fs);
    
    % Synthetic Fetal ECG - faster rate, lower amplitude
    fetal_rate = 140 / 60; % 140 BPM
    f_ecg = generate_ecg_train(t, fetal_rate, fs) * 0.15;
    
    % Additive noise
    noise = 0.02 * randn(size(t));
    
    % Abdominal Mixture
    % Assume maternal transfer function is a simple delay/scale for simulation
    m_abd = circshift(m_ecg, 2) * 0.8; 
    abd_sig = m_abd + f_ecg + noise;
    ref_sig = m_ecg; % Chest lead
    
    % NLMS Initialization
    N = length(abd_sig);
    w = zeros(L, 1);
    e = zeros(N, 1);
    
    % NLMS Adaptive Filtering Loop
    for n = L:N
        % Input vector from reference
        x_n = ref_sig(n:-1:n-L+1);
        
        % Filter output (maternal estimate)
        y_n = w' * x_n;
        
        % Error signal (fetal estimate + noise)
        e(n) = abd_sig(n) - y_n;
        
        % Weight update
        norm_x = x_n' * x_n;
        w = w + (mu * e(n) * x_n) / (epsilon + norm_x);
    end
    
    % Plotting results
    figure('Name', 'AURA-MOM PRO: NLMS Fetal ECG Extraction', 'Position', [100, 100, 1000, 800]);
    
    subplot(3,1,1);
    plot(t, abd_sig, 'b');
    title('Abdominal Mixture (Maternal + Fetal + Noise)');
    ylabel('Amplitude (mV)');
    xlim([1, 4]);
    grid on;
    
    subplot(3,1,2);
    plot(t, ref_sig, 'k');
    title('Thoracic Reference (Maternal ECG)');
    ylabel('Amplitude (mV)');
    xlim([1, 4]);
    grid on;
    
    subplot(3,1,3);
    plot(t, e, 'r');
    title('Extracted Fetal ECG (NLMS Residual)');
    xlabel('Time (s)');
    ylabel('Amplitude (mV)');
    xlim([1, 4]);
    grid on;
    
    % Save figure
    % saveas(gcf, '../results/nlms_convergence_results.png');
end

% Helper function to generate synthetic ECG pulses
function ecg = generate_ecg_train(t, rate_hz, fs)
    ecg = zeros(size(t));
    period_samples = round(fs / rate_hz);
    pulse = [zeros(1, 10), 0.1, -0.15, 1.0, -0.2, 0.1, zeros(1, 10)]';
    p_len = length(pulse);
    
    idx = 1;
    while idx + p_len < length(ecg)
        ecg(idx:idx+p_len-1) = pulse;
        idx = idx + period_samples;
    end
    
    % Add baseline wander
    ecg = ecg + 0.05 * sin(2*pi*0.5*t);
end
