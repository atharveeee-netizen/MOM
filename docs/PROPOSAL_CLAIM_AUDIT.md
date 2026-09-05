# AURA-MOM PRO: Proposal Claim Audit & Lexicon Enforcement
**Vishwakarma Awards 2026 — Stage-1 Red-Team Review**

This audit report documents the comprehensive Red-Team claim verification executed on the **AURA-MOM PRO Stage-1 Proposal (22-Page Engineering Dossier)**. Every technical claim, metric, and architectural description has been cross-referenced against the active repository codebase, executable scripts, and raw experimental data to guarantee 100% adherence to the Vishwakarma Awards Absolute Truth Policy.

---

## 1. Zero-Tolerance Buzzword & Over-Claim Sweep

The proposal source code (`generate_stage1_proposal.py`) was subjected to automated lexical auditing (`experiments/audit_proposal_text.py`) targeting marketing hyperbole, ungrounded medical claims, and unsubstantiated deployment assertions:

| Audited Keyword / Category | Occurrences in Proposal | Audit Finding & Action Taken | Red-Team Verdict |
| :--- | :---: | :--- | :---: |
| `"medical-grade"` | 0 | Prohibited. Replaced with *"high-precision biopotential acquisition"* and *"biocompatible ABS polymer"*. | ✅ PASS (0 Matches) |
| `"99%"` | 0 | Prohibited. Arbitrary percentage accuracy claims completely removed. | ✅ PASS (0 Matches) |
| `"world's first"` / `"first ever"` | 0 | Prohibited. No unfounded priority claims made. | ✅ PASS (0 Matches) |
| `"revolutionary"` / `"breakthrough"` | 0 | Prohibited. Replaced with *"core mathematical foundation"* and *"deterministic DSP architecture"*. | ✅ PASS (0 Matches) |
| `"production AI"` | 0 | Prohibited. W-NETR is strictly labeled as a *"preliminary research benchmark"*. | ✅ PASS (0 Matches) |
| `"deployed on nRF52840"` | 0 | Prohibited. Memory and latency are explicitly classified as *"projected"* and *"software-in-the-loop estimate"*. | ✅ PASS (0 Matches) |
| `"clinically validated AI"` | 0 | Prohibited. AI results are explicitly noted as inferior to NLMS on the current benchmark. | ✅ PASS (0 Matches) |
| `"patient trial"` / `"hospital trial"` | 0 | Prohibited. All future clinical studies are labeled as *"planned Stage 4-5 roadmap pending IEC clearance"*. | ✅ PASS (0 Matches) |

---

## 2. Mandatory Vocabulary & Replacement Matrix

| Unsubstantiated / High-Risk Phrasing | Why It Fails Engineering Red-Team Review | Mandatory Proposal Replacement Wording | Enforcement in 22-Page Dossier |
| :--- | :--- | :--- | :---: |
| *"Our clinical trial / Real clinical study"* | ADFECGDB is an open research database recorded by Jezewski et al., not a trial conducted by this team. | **"Real physiological dataset: ADFECGDB"** | Enforced across all pages (Pages 2, 8, 9, 10, 21) |
| *"592 segments evaluated"* (without context) | Formal primary-lead baseline evaluated 148 physiological time segments; 592 represents 4-channel batching. | **"148 physiological segments (held-out subject `r10`)"** | Reconciled and explicitly explained in Page 8 & Evidence Index |
| *"NLMS is 4.3x more accurate than AI"* | Oversimplified interpretation of RMSE ratio on initial feasibility benchmark. | **"Under the current evaluation configuration, NLMS produced lower extraction error than the preliminary W-NETR benchmark"** | Enforced on Pages 13, 14, 21 |
| *"> 200 Hours Measured Battery Life"* | Calculated from datasheet current draw and nominal capacity; not measured with a physical coulomb counter. | **"> 200 h projected battery autonomy (datasheet power-budget estimate)"** | Enforced on Pages 2, 6, 15, 20, 21 |
| *"$31.25 Total Manufacturing Cost"* | Aggregated supplier single-unit component pricing; not a turnkey contract manufacturing invoice. | **"$31.25 estimated BOM (component/datasheet-based estimate)"** | Enforced on Pages 2, 6, 20, 21 |
| *"7.5 µs latency on ARM Cortex-M4F"* | Measured on host x86 CPU via Python simulation loop mimicking interrupt schedule. | **"7.5 µs/sample software-in-the-loop timing estimate"** | Enforced on Pages 2, 6, 7, 9, 15, 21 |
| *"Physically validated on nRF52840"* | Silicon hardware validation scheduled for Stage 2. | **"Projected working-memory requirement: < 1 KB, well within nRF52840 RAM budget"** | Enforced on Pages 6, 13, 15, 21 |
| *"Clinical alarms"* | Software dashboard has not undergone medical device software (IEC 62304) validation. | **"Research/demo alert visualization"** | Enforced on Pages 11, 21 |
| *"Medical-grade diagnostic device"* | No ISO 13485 or CDSCO/FDA medical device regulatory clearance. | **"Low-cost non-invasive maternal and fetal monitoring platform"** | Enforced on Cover, Pages 2, 5, 18 |

---

## 3. Claim Classification & Traceability Matrix

Every technical claim in the proposal is categorized into one of seven formal truth classes:

| Subsystem / Metric | Proposal Value | Formal Classification | Reproducibility Script / Source | Audit Sign-Off |
| :--- | :--- | :--- | :--- | :---: |
| **NLMS Extraction Error** | RMSE = 0.1005 mV, MAE = 0.0810 mV | **VALIDATED (REAL DATA)** | `python ml/classical/nlms.py` | ✅ VERIFIED |
| **Evaluation Scope** | 148 physiological segments (r10) | **VALIDATED (REAL DATA)** | `experiments/data_split/adfe_cgdb_split.json` | ✅ VERIFIED |
| **Fetal Heart Rate Extraction** | Mean FHR = 135.36 BPM | **COMPUTED ALGORITHM OUTPUT** | `python ml/classical/fecg_analysis.py` | ✅ VERIFIED |
| **Signal Quality Index (SQI)** | Mean SQI = 2.556 | **COMPUTED ALGORITHM OUTPUT** | `python ml/classical/fecg_analysis.py` | ✅ VERIFIED |
| **Uterine EHG Contraction Energy** | TKEO = 0.009465 | **COMPUTED ALGORITHM OUTPUT** | `python ml/classical/ehg_analysis.py` | ✅ VERIFIED |
| **Per-Sample Execution Latency** | 7.5 µs / sample | **SIMULATED (Software-in-Loop)**| `python experiments/run_signal_injection.py` | ✅ VERIFIED |
| **Working Memory (SRAM)** | < 1 KB state buffer | **ESTIMATED (ALGORITHMIC ANALYSIS)** | Algorithmic state analysis (10 taps $\times$ 4 bytes) | ✅ VERIFIED |
| **W-NETR Transformer Error** | RMSE = 0.43398 mV, MAE = 0.35313 mV | **PRELIMINARY BENCHMARK** | `python experiments/evaluate_ai.py` | ✅ VERIFIED |
| **W-NETR FHR MAE** | 18.551 BPM | **PRELIMINARY BENCHMARK** | `python experiments/evaluate_ai.py` | ✅ VERIFIED |
| **Unit Prototype BOM** | $31.25 USD (~₹2,600 INR) | **ESTIMATED (BOM MODEL)** | `docs/BOM.md` catalog pricing model | ✅ VERIFIED |
| **Battery Operating Autonomy** | > 200 h on 2000 mAh Li-Po cell | **ESTIMATED (POWER BUDGET)** | `docs/BOM.md` current draw integration | ✅ VERIFIED |
| **Clinical Telemetry Visualizer** | 60 FPS Canvas replay interface | **FUNCTIONAL SOFTWARE** | `dashboard/index.html` | ✅ VERIFIED |
| **Physical PCB Prototype** | 4-layer ADS1298 + nRF52840 PCB | **PROPOSED (STAGE 2)** | Schematics & Gerbers drafted | ✅ VERIFIED |
| **Clinical Trial Efficacy** | Diagnostic sensitivity & specificity | **NOT YET VALIDATED** | Institutional Ethics Committee clearance pending | ✅ VERIFIED |

---

## 4. Final Red-Team Sign-Off

The final 22-page proposal document (`AURA_MOM_PRO_Vishwakarma_Stage1_Proposal.pdf`) adheres 100% to the Vishwakarma Stage-1 Absolute Truth Policy. It presents genuine engineering accomplishments, demonstrates rigorous DSP validation on real physiological data, transparently discloses the limitations of preliminary AI experiments, and provides a feasible, staged roadmap to physical hardware and clinical validation.
