# AURA-MOM PRO — AI VALIDATION

## 1. Goal
To validate the Deep Learning source separation pipeline against the baseline classical NLMS algorithm, providing transparent, non-fabricated metrics on true maternal-fetal non-invasive ECG recordings.

## 2. Experimental Setup
*   **Model**: 1D W-NETR (Vision Transformer + UNETR structure adapted for 1D time-series).
*   **Dataset**: ADFECGDB (Abdominal and Direct Fetal ECG Database).
*   **Training Strategy**: 
    *   **Loss Function**: L1 Loss + 0.1 * Pearson Correlation Loss. This forces the network to preserve both amplitude sparsity (crucial for peak detection) and waveform morphology (crucial for interval measurements).
    *   **Data Leakage Prevention**: We enforce a strict subject-level split:
        *   Train: r01, r04, r07
        *   Validation: r08
        *   Test: r10 (Held-out).

## 3. Overnight Training Mission Results
The W-NETR model was trained from scratch over the specified 8 PM to 8 AM mission window. Checkpoints were saved based on minimizing the combined loss on the `r08` validation set. 

Upon completion, `experiments/evaluate_ai.py` was executed strictly on `r10`. The metrics are automatically dumped to `results/proposal_metrics.json`.

## 4. Final Claim Status
Refer to `results/proposal_metrics.json` for the exact calculated values on the Test set.
*   **If AI metrics outperform NLMS (RMSE < 0.1005 mV)**: The W-NETR pipeline becomes the primary cloud-tier inference engine.
*   **If AI metrics underperform NLMS**: The results are **KEPT AS EVIDENCE** of engineering rigor. The Vishwakarma proposal will highlight our dual-tier architecture where the robust NLMS runs on the edge MCU, while deep learning acts as a supplementary experimental tier. We do not invent numbers to make the AI look better.
