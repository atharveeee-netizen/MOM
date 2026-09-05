# AURA-MOM PRO: Claim-Evidence Matrix

**Objective:** Trace every claim in the Vishwakarma proposal to its exact underlying evidence script/artifact.

| Proposal Claim | Location in Proposal | Evidence Source | Reproducibility Status |
| :--- | :--- | :--- | :--- |
| **"Evaluated offline using local extraction windows... (ADFECGDB)"** | Section 3 | `experiments/data_split/adfe_cgdb_split.json` (Subject `r10`, 148 segs) | **REPRODUCIBLE** |
| **"FECG Extraction Error (RMSE): 0.1005 mV"** | Section 3.1 | `ml/classical/nlms.py` | **REPRODUCIBLE** |
| **"FECG Extraction Error (MAE): 0.0810 mV"** | Section 3.1 | `ml/classical/nlms.py` | **REPRODUCIBLE** |
| **"Mean Fetal Heart Rate (FHR): 135.36 BPM"** | Section 3.1 | `ml/classical/fecg_analysis.py` | **REPRODUCIBLE BUT UNVALIDATED (Against Gold Standard)** |
| **"Signal Quality Index (SQI): 2.556"** | Section 3.1 | `ml/classical/fecg_analysis.py` | **REPRODUCIBLE BUT UNVALIDATED** |
| **"Latency (Per Sample): ~0.0075 ms"** | Section 3.1 | `experiments/run_signal_injection.py` | **REPRODUCIBLE (Software Simulation Only)** |
| **"Total Estimated BOM: $31.25 USD"** | Section 3.2 | `docs/BOM.md` | **ESTIMATED (Supplier Listings)** |
| **"Estimated Power Efficiency: ~10 mA"** | Section 3.2 | `docs/BOM.md` | **ESTIMATED (Datasheet projections)** |
| **"Deep Learning (1D-W-NETR): 0.4340 mV RMSE (vs 0.1005 mV NLMS)"** | Section 3.1 / 4 | `experiments/evaluate_ai.py` (`results/proposal_metrics.json`) | **REPRODUCIBLE (Feasibility run on r10; proven inferior to NLMS)** |
| **"Bluetooth Low Energy (BLE 5.0) transmits telemetry"** | Section 2 | `dashboard/index.html` (Mocked in UI) | **MOCKED IN DEMO (Not implemented on hardware)** |
