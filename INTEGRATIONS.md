# Integrations & Ecosystem: AURA-MOM PRO

## Target Hardware ICs
*   **Biopotential AFE:** TI ADS1298 / ADS1298R (8-channel, 24-bit).
*   **IMU:** Bosch BMI270 or equivalent.
*   **Temperature:** MAX30205 or equivalent.
*   **Optical Front End:** ADPD4100 or MAX30102-class prototype module.
*   **MCU / Edge Compute:** nRF5340 or ESP32-S3.

## External Modules / Companion Devices
*   **Maternal Blood Pressure:** Validated Bluetooth upper-arm cuff. Must be integrated into the app for hypertensive-risk surveillance.
*   **Optional Home Tests:** Urine protein / Hb / glucose. (To be entered via app).

## Datasets for Algorithm Development
*   **Fetal ECG:** PhysioNet NIFECG (Non-Invasive Fetal ECG) dataset.
*   **EHG:** Term-Preterm EHG dataset (TPEHG).
*   **Acoustic / PCG:** Shiraz University Fetal Heart Sounds (SUFHS) dataset for PVDF sensor validation.

_Note: Preprocessing scripts for these public datasets must be prepared to benchmark algorithms._

## Software Stack & Frontend Frameworks
*   **Patient App:** Flutter (Cross-platform iOS/Android deployment for accessibility).
*   **Clinician Dashboard:** React (Web-based dashboard with robust charting libraries like Recharts for live signal monitoring).
