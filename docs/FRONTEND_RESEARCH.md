# AURA-MOM PRO: Frontend Design Research & Information Architecture

This document synthesizes interaction patterns from leading clinical monitors to inform the visual engineering of the AURA-MOM PRO dashboard, ensuring a professional, scientifically literate interface.

## 1. Reference Product Analysis

| Reference | Strength | Pattern Worth Borrowing | AURA-MOM Adaptation |
| --------- | -------- | ----------------------- | ------------------- |
| **Philips Avalon (FM Series)** | High density touch-interface; dedicated numeric zones decoupled from waveforms. | "SmartKeys" for quick context switching. Separation of FHR and Uterine Activity. | Sidebar navigation for fast switching between "Overview" and "Settings". Distinct panel for FHR and Maternal HR. |
| **GE Corometrics 250cx** | Strict hierarchical display; physiological waveforms are heavily prioritized in the center. | Waveform & Messaging area distinct from Primary Labor Parameters. | A central, multi-layer waveform stack (Abdominal → NLMS → Fetal) taking up 60% of horizontal real estate. |
| **Mindray BeneVision N-Series** | Flat UI, extremely high contrast, absence of decorative gradients. | Strict color-coding for status (Red=Urgent, Yellow=Review, Blue=Normal). | Adopt a deep-dark theme (`#0b0c10`) with stark high-contrast accent colors for actual physiological values, avoiding "SaaS" aesthetics. |

## 2. AURA-MOM Information Architecture (IA)

The dashboard is structured around the objective AURA-MOM hardware pipeline rather than clinical diagnostics (which are unvalidated). 

### Navigation (Left Sidebar)
- **OVERVIEW**: The primary triage view (Vitals + Stacked Waveforms).
- **SIGNALS**: Detailed exploration of individual channels.
- **MONITORING**: Longitudinal trends (24-hour view).
- **DEVICE**: nRF52840 connection status, battery, BLE latency.
- **RESULTS**: DSP benchmarking (MAE, RMSE, Processing Time).

### Core View (Overview)
- **Top Header**: Device Status (CONNECTED/DISCONNECTED) and Operating Mode (REAL DATASET REPLAY / LIVE / DEMO).
- **Vitals Column (Left/Right)**: Large, high-readability integers for FHR and MHR. Text-based metrics for Signal Quality and EHG.
- **Center Canvas**: The objective proof of the engineering system:
  1. RAW ABDOMINAL (Input)
  2. MATERNAL COMPONENT (Cancellation)
  3. FETAL ECG (NLMS Output)

### Alert & Review System
Alerts are treated strictly as signal-processing or hardware status flags, not medical diagnoses.
- **NORMAL**: Hardware acquiring, NLMS converging.
- **REVIEW**: "Low signal quality detected" or "High motion artifact".
- **URGENT**: "Sensor disconnected" or "BLE timeout".
