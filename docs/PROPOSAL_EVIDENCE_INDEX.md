# AURA-MOM PRO: Proposal Evidence Index & Provenance Reconciliation
**Vishwakarma Awards 2026 — Stage-1 Open Applications**

This document catalogues every piece of empirical evidence, mathematical metric, evaluation script, and dataset slice utilized in the **AURA-MOM PRO Vishwakarma Stage-1 Proposal (22-Page Engineering Dossier)**.

---

## 1. Critical Metric Provenance Reconciliation (148 Segments vs 592 Chunks)

Prior engineering discussions in the repository referenced both "148 physiological segments" and "592 test chunks/segments". Below is the formal mathematical and structural reconciliation:

### Mathematical & Topological Reconciliation:
1. **The Dataset Structure:**
   - Database: PhysioNet Abdominal and Direct Fetal Electrocardiogram Database (ADFECGDB).
   - Recordings: 5-channel recordings sampled at 1,000 Hz (1 kHz) over 5 minutes (300 seconds = 300,000 samples per subject).
   - Channels: 4 differential abdominal surface leads (`Direct ECG 1..4`) + 1 invasive fetal scalp lead (`Direct ECG fetal` = ground truth reference).
2. **The Held-Out Test Split:**
   - Formal Subject Split: `r10` is strictly isolated as the held-out subject (zero data leakage from training subjects `r01`, `r04`, `r07`, `r08`).
   - Windowing: 300 seconds are segmented into 2.0-second non-overlapping windows (each containing 2,000 samples).
   - Segments per Channel: $\frac{300 \text{ s}}{2.0 \text{ s}} \approx 150$ segments (specifically 148 valid physiological segments after excluding edge boundary transients).
3. **The Derivation of 592 Chunks:**
   - Multi-Channel Expansion: The ADS1298 front-end simultaneously captures **4 abdominal channels**.
   - $148 \text{ physiological time windows} \times 4 \text{ abdominal channels} = \mathbf{592 \text{ channel-segment evaluation chunks}}$.
4. **Primary Headline Metric Rule:**
   - The primary headline benchmark metric (**RMSE = 0.1005 mV, MAE = 0.0810 mV**) represents the formal, subject-wise, primary-lead evaluation across the **148 temporal physiological segments** of held-out subject `r10`.
   - The 592 figure refers to the multi-channel batch evaluation across all 4 abdominal leads simultaneously.
   - **Audit Decision:** The proposal exclusively cites **148 physiological segments (held-out subject `r10`)** for the primary headline metric to maintain absolute scientific conservatism.

---

## 2. Master Empirical Evidence Registry

| Metric | Source File | Dataset | Split | Number of Subjects | Number of Segments / Chunks | Calculation Method | Claim Classification | Safe Proposal Wording |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NLMS Reconstruction Error (RMSE)** | `ml/classical/nlms.py` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject (`r10`) | 148 physiological segments (2,000 samples/seg @ 1 kHz) | $\sqrt{\frac{1}{N}\sum (e[n] - s_{fetal}[n])^2}$ | **VALIDATED (REAL PHYSIOLOGICAL DATA)** | "0.1005 mV RMSE obtained on real physiological recordings from the ADFECGDB research dataset under the documented evaluation protocol." |
| **NLMS Mean Absolute Error (MAE)** | `ml/classical/nlms.py` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject (`r10`) | 148 physiological segments | $\frac{1}{N}\sum \|e[n] - s_{fetal}[n]\|$ | **VALIDATED (REAL PHYSIOLOGICAL DATA)** | "0.0810 mV MAE achieved on held-out subject r10 from the ADFECGDB physiological dataset." |
| **Multi-Channel Evaluation Scope** | `experiments/data_split/adfe_cgdb_split.json` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject | 592 channel-segments (148 windows $\times$ 4 leads) | Batch evaluation across all 4 differential abdominal leads | **COMPUTED FROM REAL DATASET** | "592 multi-channel evaluation chunks (148 physiological time segments across 4 abdominal electrode pairs)." |
| **Fetal Heart Rate (FHR)** | `ml/classical/fecg_analysis.py` | ADFECGDB extraction output | Held-out Test (`r10`) | 1 subject | 148 segments | Pan-Tompkins QRS detection on extracted residual $e[n]$ | **COMPUTED ALGORITHM OUTPUT** | "Mean calculated FHR of 135.36 BPM from reconstructed signal (algorithmic demonstration; clinical diagnostic accuracy not yet validated)." |
| **Signal Quality Index (SQI)** | `ml/classical/fecg_analysis.py` | ADFECGDB extraction output | Held-out Test (`r10`) | 1 subject | 148 segments | QRS energy vs out-of-band noise ratio | **COMPUTED ALGORITHM OUTPUT** | "Algorithmic SQI score of 2.556 (relative heuristic metric; requires clinical threshold tuning)." |
| **Uterine EHG Energy** | `ml/classical/ehg_analysis.py` | ADFECGDB abdominal leads | Held-out Test (`r10`) | 1 subject | 148 segments | 0.1–4.0 Hz bandpass + Teager-Kaiser Energy Operator (TKEO) | **COMPUTED ALGORITHM OUTPUT** | "TKEO energy metric of 0.009465 demonstrating electrohysterographic contraction tracking feasibility." |
| **Per-Sample Execution Latency** | `experiments/run_signal_injection.py` | Simulated 1 kHz stream | Bench simulation | N/A | 100,000 samples | Python host CPU time-per-sample loop measurement | **SIMULATED (Software-in-the-Loop)** | "7.5 µs/sample software-in-the-loop timing estimate (measured in Python SIL; bare-metal MCU timing pending physical flashing)." |
| **Working Memory (SRAM)** | `ml/classical/nlms.py` | Algorithmic state analysis | N/A | N/A | 10-tap FIR filter vector | State vector size: $N \times 4\text{ bytes} = 40\text{ bytes}$ | **ESTIMATED (ALGORITHMIC ANALYSIS)** | "Projected working-memory requirement: < 1 KB, well within the nRF52840's available 256 KB RAM budget." |
| **W-NETR Transformer Error (RMSE)** | `experiments/evaluate_ai.py` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject (`r10`) | 148 segments | Model inference forward pass vs scalp ground truth | **PRELIMINARY AI BENCHMARK** | "0.43398 mV RMSE achieved by preliminary 1D-W-NETR Vision Transformer benchmark (feasibility study; did not outperform NLMS)." |
| **W-NETR Mean Absolute Error (MAE)** | `experiments/evaluate_ai.py` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject (`r10`) | 148 segments | Mean absolute difference on test split | **PRELIMINARY AI BENCHMARK** | "0.35313 mV MAE on preliminary W-NETR benchmark." |
| **W-NETR FHR Error (MAE)** | `experiments/evaluate_ai.py` | PhysioNet ADFECGDB | Held-out Test (`r10`) | 1 subject (`r10`) | 148 segments | Pan-Tompkins on Transformer output vs scalp R-peaks | **PRELIMINARY AI BENCHMARK** | "18.551 BPM FHR MAE on preliminary W-NETR benchmark (unacceptable for clinical deployment; confirms DSP superiority)." |
| **Unit Prototype BOM Cost** | `docs/BOM.md` | Supplier catalog pricing | Single-unit prototype | N/A | 1 bill of materials | Sum of component prices (TI ADS1298, nRF52840, PMIC, etc.) | **ESTIMATED (BOM MODEL)** | "$31.25 ESTIMATED BOM (Component/datasheet-based estimate; manufacturing cost not yet physically validated)." |
| **Battery Operating Autonomy** | `docs/BOM.md` | Datasheet current integration | Constant streaming | N/A | 1 power model | $\frac{2000\text{ mAh}}{9.82\text{ mA}} \approx 203.7\text{ hours}$ | **ESTIMATED (POWER BUDGET)** | "> 200 h PROJECTED BATTERY AUTONOMY (Datasheet / power-budget estimate; physical battery discharge curve not yet measured)." |
| **Physical PCB Validation** | Hardware design files | Altium / KiCad schematics | N/A | N/A | Revision 1.0 schematic | Schematic review & DRC | **PROPOSED (STAGE-2 ROADMAP)** | "Physical hardware prototype in development; bare-metal MCU validation and bench phantom testing scheduled for Stage 2." |
| **Clinical Performance & Efficacy** | Prospective clinical study | Pregnant human subjects | N/A | N/A | 0 patients enrolled | Clinical trial protocol drafted | **NOT YET VALIDATED** | "Clinical feasibility and diagnostic efficacy not yet studied; requires formal Institutional Ethics Committee (IEC) approval." |

---

## 3. Ground Truth Data Integrity Protocols

1. **Source Citation:** PhysioNet Abdominal and Direct Fetal Electrocardiogram Database (`ADFECGDB`), DOI: 10.13026/C2X019.
2. **Recording Verification:** Recorded in clinical labor wards by J. Jezewski et al. Invasive scalp electrode provided gold-standard fetal cardiac electrical activity simultaneously with 4 abdominal surface biopotential leads.
3. **Data Preprocessing Verification:** All signals bandpass filtered (0.5–100 Hz), notch filtered (50 Hz), normalized to millivolts (mV).
4. **Reproducibility Guarantee:** Executing `python ml/classical/nlms.py` regenerates identical RMSE (0.1005 mV) and MAE (0.0810 mV) outputs from raw PhysioNet records in < 5 seconds.
