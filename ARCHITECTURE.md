# Architecture & Pipeline: AURA-MOM PRO

## DSP / AI Pipeline
1. Hardware anti-aliasing and synchronized acquisition.
2. 50-Hz mains interference suppression for the India deployment context, with care not to distort fetal QRS morphology.
3. Separate digital branches for ECG/fECG, EHG and acoustic signals.
4. IMU-driven motion/artifact quality index; reject or down-weight corrupted windows.
5. Maternal QRS detection/template estimation and spatial separation of maternal vs fetal components.
6. FastICA / related blind-source-separation methods as an experimental V1 approach.
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
| **Firmware** | AFE driver, synchronized sampling, IMU, battery, BLE, local storage, sensor diagnostics. |
| **DSP** | Filtering, mains rejection, motion gating, ICA/separation, QRS detection, EHG and PVDF feature extraction. |
| **Edge AI** | Feature fusion, personalized baseline, confidence score and alert state. |
| **Mobile app** | Pairing, belt-placement guidance, live signal quality, trends, symptoms and BP-device integration. |
| **Clinician dashboard** | FHR/MHR/EHG trends, signal quality, maternal vitals, event timeline and raw-waveform review. |
| **Dataset layer** | PhysioNet NIFECG + Term-Preterm EHG datasets for algorithm development; versioned experiments and reproducible metrics. |
