# AURA-MOM PRO: Proposal Asset Index & Visual Registry
**Vishwakarma Awards 2026 — Stage-1 Open Applications**

This document catalogues every technical schematic, real physiological waveform plot, system block diagram, dashboard screenshot, and verified QR code embedded in the **AURA-MOM PRO 22-Page Stage-1 Proposal**.

---

## 1. Registered Technical Visual Assets

| Asset Filename | Subject / Technical Content | Original Provenance | Dimensions / Format | Proposal Page Placement | Audit Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`aura_mom_pro_concept.jpg`** | Wearable 8-channel maternal-fetal monitoring belt concept illustration | Hardware industrial design concept | 1920x1080 JPEG | **Page 1 (Cover Page)** | Clean technical concept; zero stock photography or AI faces. |
| **`waveform_signal_challenge.png`** | Synchronized 4.0s snippet of raw abdominal surface potential vs true scalp FECG | PhysioNet ADFECGDB (Subject `r10`) generated via Python | 2400x1200 PNG | **Page 4 (Biophysical Breakdown)** | Exact physiological signals illustrating -15 dB to -25 dB fetal-to-maternal SNR deficit. |
| **`diagram_signal_acquisition_module.png`** | Master end-to-end signal acquisition & preamplification block diagram | Medical instrumentation reference adapted for ADS1298 | 1000x650 PNG | **Page 5 (Master Architecture)** | Depicts differential electrode inputs, instrumentation amps, and high-pass topology. |
| **`diagram_power_afe_mcu_subsystem.png`** | Complete hardware architecture: PMIC (BQ24075), LDO (TPS73633), AFE (ADS1298), MCU (nRF52840) | Altium / KiCad engineering block schematic | 1400x900 PNG | **Page 6 (Hardware Architecture)** | Verified component-to-function topology with SPI & BLE telemetry buses. |
| **`diagram_analog_filter_chain.png`** | Multi-stage analog preconditioning filter chain (anti-aliasing, bandpass, notch) | Bio-instrumentation analog front-end schematic | 1000x700 PNG | **Page 7 (Signal Processing)** | Illustrates 0.5–100 Hz bandpass and 50 Hz twin-T notch pre-ADC filtering. |
| **`diagram_wearable_dsp_storage.png`** | Circular state ring buffers, CMSIS-DSP NLMS execution loop, and flash cache | Embedded firmware architecture design | 1000x750 PNG | **Page 8 (Methodology)** | Details deterministic DMA packet handling and 32-tap FIR convolution. |
| **`waveform_extraction_real_data.png`** | 4-panel real physiological validation plot (Abdominal, Thoracic Ref, Scalp Truth, NLMS Output) | Direct output of `experiments/generate_figures.py` | 3600x3000 PNG (300 DPI) | **Page 10 (Waveform Evidence)** | Demonstrates complete maternal QRS cancellation and 0.0810 mV MAE residual. |
| **`dashboard_screenshot.png`** | Live browser-based clinical telemetry monitor with active multi-channel streaming | Direct capture from running `dashboard/index.html` server | 1280x720 PNG | **Page 11 (Software Proof)** | Displays real dataset replay, 109 BPM FHR, 82 BPM MHR, and system event log. |
| **`wnetr_architecture.png`** | 1D-W-NETR Dual U-Net Vision Transformer benchmark architecture diagram | Research benchmark documentation (`ml/pretrained/`) | 1200x550 PNG | **Page 12 (AI Investigation)** | Illustrates dual-branch 1D U-Net and cross-attention blocks evaluated on ADFECGDB. |
| **`diagram_wearable_network_flow.png`** | Low-power BLE telemetry network flow with CRC32 packet validation & lead-off safety | Wearable biomedical networking specification | 600x500 PNG | **Page 15 (Safety & Efficiency)** | Outlines galvanic isolation, human-in-the-loop oversight, and fault fallbacks. |
| **`diagram_system_edge_cloud.png`** | District-wide multi-tier telehealth architecture (PHC bed &rarr; Gateway &rarr; Civil Hospital) | Rural public health telemetry topology | 1400x1050 PNG | **Page 17 (Scalability & Cloud)** | Depicts offline-first sync, MQTT telemetry, and central obstetrician review dashboard. |

---

## 2. Verified QR Codes & Interactive Links

All QR codes embedded in the proposal were verified for destination validity and decoded via computer vision tools (`cv2.QRCodeDetector`):

| QR Code Filename | Embedded Destination URL | Verified Target Content | Page Placement |
| :--- | :--- | :--- | :--- |
| **`qr_github_repo.png`** | `https://github.com/atharveeee-netizen/MOM` | Official public Git repository containing all code, scripts, and documentation | **Page 22 (Verification Guide)** |
| **`qr_live_dashboard.png`** | `https://atharveeee-netizen.github.io/MOM/` | Hosted live web telemetry dashboard with real ADFECGDB dataset replay | **Page 11 & Page 22** |
| **`qr_results_metrics.png`** | `https://raw.githubusercontent.com/atharveeee-netizen/MOM/master/results/proposal_metrics.json` | Machine-readable canonical JSON containing verified metrics and provenance | **Page 22 (Verification Guide)** |

---

## 3. Visual Quality & Integrity Sign-Off

1. **Resolution Standard:** All raster diagrams and waveform figures are rendered at 150–300 DPI, ensuring crisp, publication-grade print clarity without visual pixelation.
2. **Provenance Guarantee:** Every waveform plot is generated directly from raw physiological binary records in the PhysioNet ADFECGDB database.
3. **No Synthetic Fakes:** No stock photography, AI hallucinated clinical environments, or fabricated device renderings are utilized anywhere in the document.
