# AURA-MOM PRO — AI LIMITATIONS

## 1. Known Architectural Weaknesses
While the W-NETR architecture is capable of 1-dimensional signal translation preserving morphological integrity, it inherently relies on absolute scaling provided by standard Normalization during inference. Its translation maps are brittle against unseen maternal phenotypes (e.g. extreme maternal tachycardia) that were not present in the ADFECGDB training distribution.

## 2. Hardware Compute Boundaries
Because this is a Transformer-based architecture, the parameter count (O(~10M)) far exceeds the local RAM capabilities of the nRF52840 (256 KB RAM). 
*   **Result**: The W-NETR ML solution is classified as **Cloud-Assisted / Edge-Tethered** (requires Bluetooth streaming to a mobile/edge compute node), whereas the classical NLMS baseline is fully **On-Device Edge Deployable**.
*   **Impact**: Future efforts must employ post-training quantization (int8) or distillation into a simpler 1D-CNN (like ANC-TCN) if the model is ever to run locally on the wearable MCU itself.

## 3. Dataset Constraints
The ADFECGDB dataset contains only 5 subjects. While we have strictly adhered to non-leakage splitting (Train: r01, r04, r07, Val: r08, Test: r10), the absolute variance of fetal physiology represented is infinitesimally small.
*   **Recommendation**: The model requires fine-tuning on a larger clinical corpus (e.g. multi-site clinical trials) prior to any true diagnostic use.

## 4. Evaluation Constraints
SQI (Signal Quality Index) for the ML extraction is currently derived directly using standard morphological heuristics, but AI-extracted FECG waveforms sometimes produce "phantom QRS complexes" when maternal interference is overwhelming, which a classical filter might simply suppress as noise. This limits specificity in low-SNR environments.
