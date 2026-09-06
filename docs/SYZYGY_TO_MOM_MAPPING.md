# Syzygy to MOM/W-NETR Mapping Matrix

This document explicitly defines how the Syzygy orchestration methodology maps onto the W-NETR PyTorch architecture within the MOM project. 

**CRITICAL AXIOM**: Syzygy is an orchestration and methodology layer. W-NETR is the actual PyTorch-based sequence-to-sequence deep learning model for FECG extraction. Syzygy does not contain W-NETR. W-NETR is not an LLM, and it does not use LoRA/QLoRA.

## 1. Architectural Distinction

| Concept | Syzygy Paradigm | MOM / W-NETR Adaptation |
| :--- | :--- | :--- |
| **Model** | Often generic LLM/Transformer workflows. | Strict preservation of the W-NETR biomedical transformer. No generative LLM layers added. |
| **Data Flow** | Generic chunking. | Strict physiological segment windowing (ADFECGDB/FECGSYNDB) standardized to 1000 Hz, 4-channel. |
| **Orchestration** | CLI-driven multi-stage execution. | Executed via `scripts/train_wnetr_syzygy.py`, managing the PyTorch Dataloader and Checkpoint cycles. |
| **Configuration** | Dynamic JSON/YAML configs. | Hardcoded loops replaced with `configs/wnetr_training.yaml` to govern epochs, seeds, datasets, and learning rates. |
| **Validation** | Automated LLM benchmarks. | Multi-seed validation on locked test sets, evaluating RMSE and MAE against the 32-tap NLMS baseline. |

## 2. Engineering Workflow Lifecycle Mapping

1. **AUDIT**: Handled by `WNETR_TRAINING_AUDIT.md` (this phase).
2. **CONFIGURE**: Parameters shifted out of PyTorch files into `configs/wnetr_training.yaml`.
3. **VALIDATE**: Checking PyTorch forward/backward pass integrity without NaNs.
4. **SCAFFOLD**: Datasets extracted from nested W-NETR repo into top-level `MOM/data/`.
5. **THROUGHPUT TEST**: Hardware benchmark execution ensuring RTX/CPU throughput estimates.
6. **BASELINE TRAIN**: Running the canonical 32-tap NLMS as the anchor point.
7. **CONVERGENCE TRAINING**: The ~45 hour run, monitored via loss plateau (Early Stopping).
8. **MULTI-SEED VALIDATION**: Repetition across seeds 42, 123, 2026.
9. **LOCKED TEST & CROSS-DATASET**: Final RMSE/MAE evaluations injected into `experiments/registry.csv`.

## 3. Strict Boundary Enforcement
- Syzygy methodology controls **how** W-NETR is trained (logging, epochs, metrics, reproducibility).
- Syzygy does **not** change the mathematical convolution or transformer patch embeddings of W-NETR. W-NETR's mathematical fidelity is fully maintained.
