# Architecture & Pipeline: AURA-MOM PRO

## DSP / AI Pipeline
1. Hardware anti-aliasing and synchronized acquisition.
2. 50-Hz mains interference suppression for the India deployment context, with care not to distort fetal QRS morphology.
3. Separate digital branches for ECG/fECG, EHG and acoustic signals.
4. IMU-driven motion/artifact quality index; reject or down-weight corrupted windows.
5. Maternal QRS detection/template estimation and spatial separation of maternal vs fetal components.
6. Adaptive Filtering specifically using **NLMS (Normalized Least Mean Squares)** combined with modified Pan-Tompkins. NLMS is chosen over RLS due to $O(N)$ complexity, ensuring efficient real-time fECG extraction on edge hardware (Nordic nRF52840 / Cortex-M4F) without crashing the loop timing.
7. Fetal QRS detection → fetal heart-rate series → signal-quality score.
8. EHG feature extraction: contraction timing, spectral features and inter-channel propagation/conduction features.
9. PVDF feature extraction: heart-sound/acoustic periodicity and signal-quality features.
10. Maternal PPG features: pulse rate, HRV-related features and SpO₂ where supported.
11. Fuse validated features against a personalized baseline.
12. Output a triage state: `NORMAL` / `REVIEW` / `URGENT ASSESSMENT` rather than a disease diagnosis.

## Sampling / Processing Strategy
*   Use the highest sampling rate required by the fetal-ECG/acoustic branch.
*   A practical prototype can acquire the full biopotential channels at approximately **500–1000 samples/s**.
*   Create a much lower-rate EHG branch after digital anti-alias filtering/decimation.
*   Exact rates, filter cutoffs and decimation factors must be verified experimentally against the selected AFE and target datasets.

## Software / Data Architecture Layers
| Layer | Responsibilities |
| :--- | :--- |
| **Firmware** | AFE driver (Strict TI Boot Sequence), IMU, battery. **CRITICAL:** Must enforce BLE Data Length Extension (DLE) and 2M PHY. **CRITICAL:** Do NOT save continuous waveform data to internal Flash NVS to avoid hardware destruction; use external SD or RAM ring buffers. |
| **DSP (Edge)** | **CRITICAL:** 0.5Hz High-Pass Filter (Butterworth) for maternal baseline wander removal. Mains rejection, motion gating, Adaptive Filtering (NLMS), QRS detection, EHG/PVDF feature extraction. |
| **Edge AI (TinyML)** | Real-time lightweight inference: Feature fusion, personalized baseline, and immediate "Signal Quality Index" / Confidence Score. |
| **Mobile app (IoT Gateway)** | Pairing, belt-placement guidance, live signal quality, trends. **NEW:** Acts as an IoT Gateway. Buffers the pre-filtered BLE data and streams it via **MQTT / WebSockets** to the Cloud Backend. |
| **Cloud AI (Backend)** | Heavy Deep Learning (PyTorch/TensorFlow). Processes the aggregated MQTT data through massive Transformer/LSTM models for exact preterm-birth prediction and complex anomaly detection that cannot fit on the Edge. |
| **Clinician dashboard** | Web UI (React/WebGL). Displays FHR/MHR/EHG trends, Cloud AI predictions, maternal vitals, event timeline and raw-waveform review. |
| **Dataset layer** | PhysioNet NIFECG + Term-Preterm EHG datasets for algorithm development; versioned experiments and reproducible metrics. |
