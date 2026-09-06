# Scientific Verdict: W-NETR vs NLMS

**Verdict Status**: [E — UNSTABLE / INSUFFICIENT EVIDENCE]
*(Note: This is a living document. The verdict is currently "Insufficient Evidence" pending the completion of the 45-hour full convergence multi-dataset generalization training).*

## 1. Core Research Question
"Does W-NETR genuinely justify its additional computational complexity (15 MB RAM, 10.2M parameters) over classical 32-tap NLMS (<1 KB RAM, 32 MACs) for non-invasive fetal ECG extraction at the embedded edge?"

## 2. Evaluation Matrix

| Metric | 32-tap NLMS (Baseline) | W-NETR (Current Best Checkpoint) | Delta |
| :--- | :--- | :--- | :--- |
| **Test Set** | ADFECGDB (Subject r10) | ADFECGDB (Subject r10) | N/A |
| **RMSE (mV)** | 0.1005 | *Pending* | *Pending* |
| **MAE (mV)** | 0.0810 | *Pending* | *Pending* |
| **VRAM / RAM** | < 1 KB (SRAM) | ~15 MB (DRAM) | ~150,000x |
| **Latency** | 7.5 µs / sample | ~12 ms / window | N/A |

## 3. Generalization Performance
*To be filled upon completion of Cross-Dataset Domain Shift evaluation (Train ADFECGDB -> Test NInFEA/PCDB).*

- **Best Case Scenario**: *Pending*
- **Median Case Scenario**: *Pending*
- **Worst Case Scenario**: *Pending*

## 4. Engineering Conclusion
*Pending final model convergence data.* 
Currently, NLMS remains the superior engineering choice for low-power edge deployment on the Nordic nRF52840 SoC due to extreme algorithmic efficiency, verified deterministic stability, and proven baseline RMSE of 0.1005 mV.
