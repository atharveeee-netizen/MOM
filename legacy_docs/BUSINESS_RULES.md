# Business Rules & Glossary: AURA-MOM PRO

## Glossary & Definitions
*   **AFE:** Analog Front End.
*   **PVDF:** Polyvinylidene fluoride. Used as acoustic/mechanical contact sensors.
*   **EHG:** Electromyography of the uterus (Electrohysterography). Used for uterine electrical activity.
*   **fECG / MHR / FHR:** Fetal Electrocardiogram / Maternal Heart Rate / Fetal Heart Rate.
*   **PPG / SpO₂:** Photoplethysmography / Peripheral oxygen saturation.
*   **FastICA:** Fast Independent Component Analysis. Used as an experimental V1 approach for blind-source separation.
*   **SDPTG:** Second derivative of the photoplethysmogram. Research feature for cardiovascular assessment.
*   **CTG:** Cardiotocography.
*   **ICEHG DS:** Induced Cesarean EHG DataSet. Newer validation dataset.

## EHG Analysis Rules (CRITICAL)
1.  **Zero Data Leakage:** When training ML models for EHG preterm detection, you must **never** oversample the dataset before splitting into train/test sets. All synthetic oversampling (e.g., SMOTE) must occur strictly on the training fold.
2.  **Core Features:** Primary EHG feature extraction must focus on **Sample Entropy** and **Teager-Kaiser Energy** operators, as validated by recent literature.

## Team Ownership Matrix
| Owner | Deliverables |
| :--- | :--- |
| **Hardware** | AFE, electrodes, PVDF front end, power, PCB, EMC/noise, connectors. |
| **Embedded** | MCU, sampling scheduler, BLE, storage, battery and diagnostics. |
| **DSP/AI** | ICA, filters, QRS, EHG, acoustic features, signal-quality index and fusion. |
| **App/Cloud** | Mobile UI, device pairing, trend visualization, clinician dashboard. |
| **Mechanical** | Belt geometry, electrode pressure, PVDF coupling, comfort and repeatable placement. |
| **Clinical/Research**| Reference measurements, dataset protocol, literature mapping, validation metrics and claim review. |

## Source Basis / Project Material
This architecture incorporates component choices documented in the AURA-MOM project material:
*   **Source:** AURA-MOM PRO Project Handover & Master Submission Kit.
*   **Budget:** ₹30,000 prototype allocation.
*   **Hardware Baseline:** 8-channel ADS1298 biopotential array, dual PVDF sensors, ADPD4100 optical front end, IMU, edge processing.
*   **Research Directions:** FastICA, EHG conduction features and SDPTG are retained as development directions but deliberately separated from validated clinical claims.
