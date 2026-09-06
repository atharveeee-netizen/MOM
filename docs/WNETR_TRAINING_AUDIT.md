# W-NETR Training & Repository Audit

**Date of Audit**: 2026-09-06
**Scope**: AURA-MOM PRO Project Repository (`MOM`) and Orchestration Layer (`Syzygy`)

## 1. Component State & Status

### A. Classical NLMS Baseline (`ml/classical/nlms.py`)
- **Status**: Validated & Canonical.
- **Configuration**: 32-tap NLMS filter, $\mu = 0.05$.
- **Evaluation Target**: ADFECGDB (Subject r10).
- **Scope**: 148 physiological windows (592 channel-level chunks).
- **Reported Metrics**: RMSE = 0.1005 mV, MAE = 0.0810 mV.
- **Audit Findings**: The baseline is stable. Stale README references to "10-tap" and older metrics must be purged to respect this single canonical ground truth.

### B. W-NETR Implementation (`ml/pretrained/W-NETR-for-FECG-extraction/`)
- **Status**: Research in progress (Untrained / Pre-trained verification state).
- **Architecture**: 1D-Transformer for biomedical signal extraction, preserving the original un-altered research topology.
- **Audit Findings**: 
  - Code was previously tested with a fast-exit `if i > 1: break` loop.
  - Hardcoded variables existed. 
  - Model is not an LLM or LoRA architecture; it is a specialized biomedical signal sequence-to-sequence transformer.
  - Requires migration from hardcoded scripts to a Syzygy-compliant orchestrator logic (`train_wnetr_syzygy.py`).

### C. Syzygy Framework
- **Status**: Engineering Scaffold / Orchestration Layer.
- **Audit Findings**:
  - Syzygy provides the methodological workflow (audit → configure → validate → scaffold → train → checkpoint → evaluate).
  - It does **not** contain the W-NETR architecture. It must orchestrate the training lifecycle of W-NETR while preserving W-NETR's raw PyTorch implementation.

## 2. Structural & Quality Deviations Found
- **Marketing Slop**: References to "clinical-grade", "immediate deployment", and unsupported claims ("4.3x lower error") found in the README.
- **Data Mixing**: W-NETR data and structure were nested arbitrarily under `ml/pretrained/`. Data directories must be elevated to a global `data/` tier to prevent leakage and support cross-dataset splits.

## 3. Corrective Action Plan
1. Isolate the W-NETR PyTorch architecture from its dataset handlers.
2. Establish global `data/splits` CSV manifests.
3. Replace hardcoded W-NETR loops with a configurable Syzygy-style YAML pipeline.
4. Cleanse the README and UI of non-verified marketing language, replacing them with a strict `CLAIM_EVIDENCE_MATRIX.md`.
