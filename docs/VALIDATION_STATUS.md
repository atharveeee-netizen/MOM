# Validation Status (Red-Team Audit)

This document tracks the objective execution state of the AURA-MOM PRO engineering prototype following the strict Red-Team Validation Audit. It strips away aspirational claims and distinguishes between what is merely proposed or simulated versus what has been experimentally validated with reproducible evidence.

## Status Definitions
*   **EXPERIMENTALLY VALIDATED (EV):** Implementation is complete, tested against ground truth or real-world data, and produces mathematically defensible metrics.
*   **COMPUTED/UNVALIDATED (CU):** Code runs on real data and outputs a number, but has not been checked against a gold-standard reference (e.g. no cardiologist labels).
*   **SIMULATED (SIM):** Tested using software-in-the-loop (SIL) or generated testbenches, not physical embedded hardware.
*   **ESTIMATED (EST):** Based on supplier listings, datasheets, or theoretical projections.
*   **BLOCKED (BLK):** Blocked by missing external dependencies, invalid architectures, or missing hardware.
*   **NOT IMPLEMENTED (NI):** No code, no simulation, no validation.

## Red-Team Audit Matrix

| Component | Status | Evidence | Reproducible Command |
| :--- | :--- | :--- | :--- |
| **Hardware PCB & AFE** | ESTIMATED | `docs/BOM.md` | N/A (Fabrication pending) |
| **NLMS DSP Math** | EXPERIMENTALLY VALIDATED | `ml/classical/nlms.py` | `python ml/classical/nlms.py` |
| **FECG Extraction (RMSE 0.1mV)** | EXPERIMENTALLY VALIDATED | `ml/classical/nlms.py` | `python ml/classical/nlms.py` |
| **FHR Calculation** | COMPUTED/UNVALIDATED | `ml/classical/fecg_analysis.py` | `python ml/classical/fecg_analysis.py` |
| **FQRS Detection (TP/FP)** | NOT IMPLEMENTED | - | Missing evaluation against GT QRS |
| **EHG Feature Extraction** | COMPUTED/UNVALIDATED | `ml/classical/ehg_analysis.py` | `python ml/classical/ehg_analysis.py` |
| **Embedded MCU Latency** | SIMULATED (SIL) | `experiments/run_signal_injection.py` | `python experiments/run_signal_injection.py` |
| **Deep Learning (W-NETR)** | BLOCKED | `docs/BENCHMARK_RESULTS.md` | N/A (Missing weights/incompatible) |
| **BLE Telemetry** | NOT IMPLEMENTED | `dashboard/index.html` (Mocked UI) | N/A (Web UI mock only) |
| **Clinical Dashboard** | SIMULATED (DEMO UI) | `dashboard/index.html` | Open `dashboard/index.html` in browser |

*Note: Any prior claims implying live, physical hardware validation have been downgraded to "Software-in-the-Loop Simulation" or "Estimated" in accordance with strict engineering protocols.*
