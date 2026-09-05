# AURA-MOM PRO — ML RESEARCH SELECTION

## 1. Objective
Select an optimal machine learning architecture for Edge-Deployable non-invasive fetal ECG (NI-FECG) extraction, utilizing purely REAL clinical data with gold-standard validation, discarding all synthetic approaches.

## 2. Dataset Selection
We reviewed available datasets for non-invasive fetal ECG:
*   **FECGSYNDB**: Rejected. Purely synthetic; violates the Vishwakarma non-synthetic real-world mandate.
*   **NInFEA**: Rejected. Small sample size and lacks direct fetal scalp ECG reference.
*   **ADFECGDB**: **SELECTED**. Contains 5 subjects (r01, r04, r07, r08, r10) with 4 channels of abdominal ECG and 1 channel of direct fetal scalp ECG, providing an absolute gold standard for supervised source separation.

## 3. Model Architecture Candidates
*   **fECG_cGAN (Pix2Pix)**: Translates spectrograms. Rejected due to the loss of phase information (morphological preservation required for FHR and clinical SQI).
*   **Temporal Convolutional Networks (ANC-TCN)**: Relies heavily on hyperparameter tuning and noise estimation thresholds.
*   **W-NETR (1D Vision Transformer + UNETR)**: **SELECTED**. Treats 1D signal vectors as patches, mapping abstract temporal dependencies between maternal and fetal morphological structures. Suitable for direct signal-to-signal source separation without losing phase data.

## 4. Strict Non-Leakage Data Split
To prevent data leakage (a common reason for inflated accuracies in literature), we enforce a strict subject-wise split:
*   **Train Set**: r01, r04, r07
*   **Validation Set**: r08
*   **Test Set**: r10

The Test Set (r10) is strictly locked and only accessed during `evaluate_ai.py` after the `best_model.pkl` is finalized.
