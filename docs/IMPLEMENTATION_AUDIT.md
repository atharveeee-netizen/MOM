# Implementation Audit

This document tracks the current reality of the AURA-MOM PRO repository. Everything listed here represents what is currently *implemented and validated* in the repository, separated from what is missing or proposed.

| Component | Status | Evidence | Missing |
| :--- | :--- | :--- | :--- |
| ADS1298 acquisition | NOT STARTED | None | Hardware schematics, firmware drivers |
| nRF52840 firmware | NOT STARTED | None | RTOS/bare-metal project, sensor reading |
| NLMS | COMPLETED | `ml/classical/nlms.py` runs on real ADFECGDB data (RMSE: 0.0368 mV) | Hardware deployment |
| FQRS | NOT STARTED | None | Fetal QRS peak detection algorithm |
| FHR | NOT STARTED | None | Heart rate calculation from RR intervals |
| EHG | NOT STARTED | None | Teager-Kaiser / Sample Entropy pipeline |
| DL benchmark | FAILED | W-NETR code exists (`ml/pretrained/`); Weights are unavailable (gdown failure) | Valid pretrained `.pkl` weights |
| BLE | NOT STARTED | None | nRF52840 BLE stack, GATT server |
| Dashboard | NOT STARTED | None | PC/Mobile UI, BLE parsing |
| Hardware | NOT STARTED | None | BOM, schematic, PCB layout |
| Dataset Prep | COMPLETED | `generate_dataset_real.py` correctly extracts real EDFs | Subject-wise train/test split lists |

## Audit Summary
- **What actually works?** The offline dataset generation from PhysioNet ADFECGDB, and the offline Classical NLMS simulation.
- **What was experimentally measured?** The Classical NLMS algorithm achieves an RMSE of `0.0368 mV` on real fetal ECG abdominal mixtures.
- **What dataset was actually used?** PhysioNet Non-Invasive Fetal ECG Database (ADFECGDB) (`r01`, `r04`, `r07`, `r08`, `r10`).
- **Were subjects separated correctly?** No formal subject-wise split lists are documented yet (data was just extracted).
- **What are the actual FQRS results?** Unknown / Not built.
- **What are the actual FHR errors?** Unknown / Not built.
- **Did a valid pretrained DL model actually run?** No. The weights provided by W-NETR authors are unreachable (Google Drive permissions/rate limit).
- **Were any random weights accidentally evaluated?** Yes, the fallback to random weights yielded a garbage MSE of `28.0`. This will NOT be reported as the model's capability.
- **What does the hardware actually demonstrate?** Nothing yet. No hardware files exist.
- **What is measured vs estimated?** NLMS RMSE is measured. Everything else is unmeasured.
- **Can the core signal path be demonstrated live?** No.
