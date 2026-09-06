# AURA-MOM PRO: Red-Team Results Audit

**Objective:** A merciless line-by-line categorization of every numerical claim in the AURA-MOM PRO repository to ensure strict Vishwakarma Awards defensibility.

## Audit Matrix

| Claim | Value | Metric | Dataset | Subjects | Script | Raw Evidence | Status |
| ----- | ----: | ------ | ------- | -------- | ------ | ------------ | ------ |
| NLMS FECG Extraction Error (RMSE) | 0.1005 mV | RMSE | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` (148 segments) | `nlms.py` | `0.1005` stdout | **COMPUTED FROM REAL DATA** |
| NLMS FECG Extraction Error (MAE) | 0.0810 mV | MAE | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` (148 segments) | `nlms.py` | `0.0810` stdout | **COMPUTED FROM REAL DATA** |
| NLMS Previous RMSE Claim (0.0368 mV) | 0.0368 mV | RMSE | Local evaluation windows derived from PhysioNet ADFECGDB | Unknown / Subset | - | - | **INVALID (REPLACED BY 0.1005)** |
| Mean Fetal Heart Rate (FHR) | 135.36 BPM | BPM | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` (148 segments) | `fecg_analysis.py` | `135.36` stdout | **COMPUTED FROM REAL DATA (UNVALIDATED AGAINST GROUND TRUTH QRS)** |
| Signal Quality Index (SQI) | 2.556 | SNR-est | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` (148 segments) | `fecg_analysis.py` | `2.556` stdout | **COMPUTED FROM REAL DATA (UNVALIDATED THRESHOLD)** |
| EHG Teager-Kaiser Energy | 0.009465 | Energy | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` (148 segments) | `ehg_analysis.py` | `0.009465` stdout | **COMPUTED FROM REAL DATA (UNVALIDATED FEATURE)** |
| Processing Time (Latency) | ~0.0075 ms / sample | Latency | Local evaluation windows derived from PhysioNet ADFECGDB | N/A | `run_signal_injection.py` | `7.5µs` avg | **SIMULATED (SOFTWARE-IN-THE-LOOP)** |
| Processing Time per Segment | 0.0068 s | Latency | Local evaluation windows derived from PhysioNet ADFECGDB | `r10` | `nlms.py` | `0.0068` stdout | **SIMULATED (x86 CPU)** |
| Battery Life (Continuous) | > 200 Hours | Time | Theoretical | N/A | `BOM.md` | `2000 mAh / 10 mA` | **ESTIMATED** |
| Total Manufacturing Cost | $31.25 USD | Cost | Supplier Listings | N/A | `BOM.md` | BOM Table | **ESTIMATED** |
| Deep Learning (1D-W-NETR) FECG Error (RMSE) | 0.43398 mV | RMSE | PhysioNet ADFECGDB (Held-out test set) | `r10` (592 segments) | `experiments/evaluate_ai.py` | `results/proposal_metrics.json` | **COMPUTED FROM REAL DATA (EXPERIMENTAL / BENCHMARK)** |
| Deep Learning (1D-W-NETR) FECG Error (MAE) | 0.35313 mV | MAE | PhysioNet ADFECGDB (Held-out test set) | `r10` (592 segments) | `experiments/evaluate_ai.py` | `results/proposal_metrics.json` | **COMPUTED FROM REAL DATA (EXPERIMENTAL / BENCHMARK)** |
| Deep Learning (1D-W-NETR) FHR Error (MAE) | 18.551 BPM | MAE | PhysioNet ADFECGDB (Held-out test set) | `r10` (592 segments) | `experiments/evaluate_ai.py` | `results/proposal_metrics.json` | **COMPUTED FROM REAL DATA (EXPERIMENTAL / BENCHMARK)** |

## Discrepancy Resolutions
1. **0.0368 mV vs 0.1005 mV RMSE:** The 0.0368 mV claim originated from an earlier baseline script evaluating only 2 segments. The mathematically rigorous evaluation across all 148 test segments of subject `r10` yields `0.1005 mV` RMSE and `0.0810 mV` MAE. The 0.0368 mV claim has been purged.
2. **Classical NLMS vs 1D-W-NETR Feasibility:** The 1D-W-NETR architecture was implemented and evaluated on the exact held-out subject `r10` test split (592 segments across 4 channels). Its feasibility run yielded an RMSE of `0.43398 mV` and MAE of `0.35313 mV`. The classical NLMS adaptive filter achieves an RMSE of `0.1005 mV` (over 4x lower error) while executing in 7.5 µs per sample on CPU with zero transformer parameter overhead. This empirical proof cements NLMS as the primary edge DSP algorithm for AURA-MOM PRO, with W-NETR cataloged as an experimental secondary benchmark.
3. **FHR / SQI Validity:** The script uses `scipy.signal.find_peaks` to compute FHR and SQI from the NLMS output. While computationally functional, the actual TP/FP FQRS detection has not been scored against a gold-standard clinician annotation. Thus, it is flagged as UNVALIDATED.
4. **Hardware Execution:** The `0.0075 ms` latency is derived from a Python SIL simulation loop mimicking the nRF52840's 1000 Hz interrupt schedule, not physical bare-metal execution on the ARM Cortex-M4F.

## Baseline Hierarchy Verified
1. **Raw Mixture:** Primary Input (Maternal ECG + Fetal ECG + Noise).
2. **Cancellation Signal:** NLMS Adaptive estimate of Maternal ECG using the abdominal reference.
3. **NLMS Extracted FECG:** Error signal `e[n]`, serving as the isolated fetal ECG.
*(Math implementation in `nlms.py` verified against standard adaptive filter equations).*
