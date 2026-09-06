# Post-Submission Research & Architecture Update

This document delineates the strict boundary between the frozen Stage-1 submission artifacts and the ongoing post-submission research evaluating deep learning (W-NETR) vs classical DSP (NLMS).

## 1. Frozen Submission Artifacts

The Vishwakarma Stage-1 proposal has been formally submitted. The following artifacts are considered **historical and frozen**. They must not be modified, rewritten, or recalibrated to reflect new findings.

- `AURA_MOM_PRO_Vishwakarma_Stage1_Proposal.pdf`
- `MOM_Vishwakarma_Stage1_Proposal.pdf`
- `AURA_MOM_PRO_Final_Proposal.pdf`
- `docs/PROPOSAL_EVIDENCE_INDEX.md` (historical index)
- `docs/PROPOSAL_CLAIM_AUDIT.md` (historical audit)

The headline metrics submitted in these PDFs reflect the canonical 32-tap NLMS baseline at the time of submission (RMSE = 0.1005 mV).

## 2. Post-Submission Scope (Ongoing Research)

The ongoing work in the repository concerns the rigorous scientific evaluation of the W-NETR PyTorch architecture against the submitted NLMS baseline. 

### Core Ongoing Mandates:
1. **Multi-Dataset Expansion**: Expanding evaluation from the single ADFECGDB dataset to a multi-dataset matrix (ADFECGDB, FECGSYNDB, NInFEA, and PCDB).
2. **Domain Generalization Check**: Measuring performance degradation when models trained on simulated physiological data (FECGSYNDB) are applied to clinical human data.
3. **Syzygy Orchestration**: Wrapping W-NETR in the strict tracking, multi-seed validation, and checkpoint reproducibility layers of the Syzygy methodology.
4. **Hardware Validation Tracking**: Replacing theoretical (software-in-the-loop) timing claims with exact bare-metal/MCU metrics as the hardware prototype matures.

All updates to code, configurations, data manifests, and research metrics generated post-submission belong to this ongoing research tier and are documented in `experiments/registry.csv`.
