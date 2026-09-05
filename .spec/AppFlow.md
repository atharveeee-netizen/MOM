# Application Flow (AppFlow.md)
## Project: AURA-MOM PRO

### 1. Execution Sequence & Signal Flow
1. **Acquisition:** 8-channel abdominal array + PVDF + IMU + temperature acquire raw physiological data.
2. **Pre-processing (Edge):** 0.5Hz HPF, mains rejection, and motion gating (via IMU data).
3. **Signal Separation (Edge AI):** NLMS Adaptive Filter extracts fetal QRS complexes from maternal signals.
4. **Feature Extraction:** Compute FHR, MHR, EHG contraction timing, and acoustic periodicity locally.
5. **BLE Transmission:** Formatted telemetry sent to the Flutter mobile app acting as an IoT gateway.
6. **Cloud Aggregation:** Mobile app streams pre-filtered BLE data via MQTT/WebSockets to the Cloud Backend.
7. **Cloud AI & Risk Stratification:** Heavy Deep Learning processes historical and aggregated data for trend anomalies and complex predictive modeling.
8. **Clinical Triage:** Results push to the Next.js clinical dashboard displaying triage states (Normal / Review / Urgent).

### 2. The "Audio-Jack" Bench Test Flow
To demonstrate the hardware without clinical testing on humans:
1. Play PhysioNet maternal/fetal ECG datasets from a laptop's audio jack.
2. Pass the signal through a simple voltage-divider resistor network.
3. Clip directly to the physical ADS1298 electrodes.
4. Prove that the hardware and Edge AI adaptive filters separate the fetal heartbeat in real-time from an analog source.
