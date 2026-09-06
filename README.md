<div align="center">
  <img src="docs/assets/aura_mom_pro_concept.jpg" alt="AURA-MOM PRO Logo" width="100%" style="border-radius: 12px; margin-bottom: 20px;" />
  
  # AURA-MOM PRO: Non-Invasive Fetal ECG Extraction at the Edge
  
  **Submission Entity:** Team Netizen | **Event:** Vishwakarma Stage 1
  
  [![Status: Ongoing Evaluation](https://img.shields.io/badge/Status-Ongoing_Evaluation-blue.svg)](#)
  [![Hardware: nRF52840](https://img.shields.io/badge/Hardware-Nordic_nRF52840-00A9CE.svg)](#)
  [![DSP: 32-tap NLMS](https://img.shields.io/badge/Classical_DSP-32--tap_NLMS-brightgreen.svg)](#)
  [![DL: W-NETR](https://img.shields.io/badge/Research_Track-W--NETR_PyTorch-orange.svg)](#)
  [![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](#)

</div>

---

## 📖 Executive Overview

AURA-MOM PRO is an advanced biomedical engineering initiative focused on extracting **non-invasive fetal electrocardiography (NI-FECG)** from mixed maternal abdominal signals. Designed for edge deployment, the system captures complex electrical biosignals and cleanly isolates the fetal heartbeat, bypassing the need for invasive scalp electrodes.

<div align="center">
  <img src="docs/assets/diagram_system_edge_cloud.png" alt="System Architecture Diagram" width="90%" />
  <br><em>High-Level Edge-to-Cloud System Architecture</em>
</div>

---

## 🎛️ Hardware & Signal Acquisition

Our physical edge device is meticulously engineered to capture microvolt-level fetal signals while filtering out ambient noise and maternal interference.

<div align="center">
  <img src="docs/assets/diagram_power_afe_mcu_subsystem.png" alt="Power AFE MCU Subsystem" width="48%" style="display:inline-block;" />
  <img src="docs/assets/diagram_analog_filter_chain.png" alt="Analog Filter Chain" width="48%" style="display:inline-block;" />
</div>

* **Analog Front-End (AFE):** High-CMRR instrumentation amplifiers extract the raw trans-abdominal signal.
* **MCU Subsystem:** The Nordic nRF52840 handles real-time data ingestion and runs our ultra-low power DSP pipeline.
* **Analog Filter Chain:** Active bandpass and notch filters pre-condition the signal before it reaches the ADC.

---

## ⚡ The Dual-Track Algorithm Evaluation

We rigorously evaluate our production baseline against our research hypothesis to ensure we deploy the most optimal solution to the edge:

<div align="center">
  <img src="docs/assets/slide_03_signal_processing_pipeline.png" alt="Signal Processing Pipeline" width="85%" />
</div>

### 1. Production Baseline: Classical DSP (Submitted)
The core embedded solution is a highly optimized, deterministic **32-tap Normalized Least Mean Squares (NLMS)** adaptive filter. It is designed to run directly on the nRF52840 SoC.

* **Memory Footprint:** `< 1 KB (SRAM)`
* **Compute Cost:** `32 MACs / sample`
* **Latency:** `7.5 µs / sample`
* **Real-world Performance:** `RMSE 0.1005 mV` (ADFECGDB subject r10)

### 2. Research Track: Deep Learning (Ongoing)
To discover the absolute ceiling of signal clarity, we are actively evaluating the **W-NETR** (Wavelet-inspired U-Net Transformer) architecture using the Syzygy Methodology.

<div align="center">
  <img src="docs/assets/wnetr_architecture.png" alt="W-NETR Architecture" width="80%" />
  <br><em>W-NETR Deep Learning Architecture for Feature Extraction and Signal Reconstruction</em>
</div>

* **Memory:** `~15 MB (DRAM)`
* **Parameters:** `10.2M`
* **Framework:** `PyTorch`

---

## 📈 Real-World Extraction Results

Below is a visualization of the signal extraction quality on clinical human data (ADFECGDB). Notice how the system successfully isolates the tiny fetal QRS complexes from the overwhelming maternal baseline.

<div align="center">
  <img src="docs/assets/waveform_extraction_real_data.png" alt="Signal Extraction Waveform" width="95%" />
</div>

---

## 💻 Clinical Dashboard

Extracted physiological data is transmitted securely to our interactive web dashboard for real-time obstetric monitoring.

<div align="center">
  <img src="docs/assets/dashboard_screenshot.png" alt="Clinical Dashboard" width="90%" style="border-radius: 8px; border: 1px solid #ccc;" />
</div>

---

## 🔍 The 60-Second Judge Path

Evaluating this repository for Vishwakarma Stage-1? Please prioritize the following documents:

1. 📄 **Frozen Stage-1 Submissions**:
   * [`AURA_MOM_PRO_Vishwakarma_Stage1_Proposal.pdf`](./AURA_MOM_PRO_Vishwakarma_Stage1_Proposal.pdf)
   * [`MOM_Vishwakarma_Stage1_Proposal.pdf`](./MOM_Vishwakarma_Stage1_Proposal.pdf)
2. 🕵️ **Claim Verification**: All numerical and hardware claims are audited in [`docs/PROPOSAL_CLAIM_AUDIT.md`](./docs/PROPOSAL_CLAIM_AUDIT.md).
3. 🔬 **Ongoing Research**: Review our strict, post-submission evaluation of DL vs DSP in [`docs/POST_SUBMISSION_RESEARCH_UPDATE.md`](./docs/POST_SUBMISSION_RESEARCH_UPDATE.md).
4. 🛡️ **Data Integrity**: We enforce a zero-fabrication clinical data handling policy, detailed in [`docs/DATA_LEAKAGE_AUDIT.md`](./docs/DATA_LEAKAGE_AUDIT.md).

---

## 📂 Repository Architecture

```text
MOM/
├── configs/            # Syzygy-compliant YAML hyperparameter definitions
├── data/
│   ├── manifests/      # Dataset provenance (ADFECGDB, FECGSYNDB, etc.)
│   └── splits/         # Strict Subject-level train/val/test CSV definitions
├── docs/               # Engineering audits, methodology mappings, and verdicts
│   └── assets/         # Diagrams and visual assets (Hardware & Software)
├── experiments/        # Checkpoint registry and execution tracking
├── ml/
│   └── pretrained/     # Raw unmodified W-NETR PyTorch architecture 
└── scripts/            # Orchestrator scripts (e.g., train_wnetr_syzygy.py)
```

## 🚀 Running the Evaluation

To initiate the full convergence Syzygy-orchestrated W-NETR PyTorch run (~45 hours on CPU):

```bash
python scripts/train_wnetr_syzygy.py
```

> **Note:** The hardware deployment firmware (C/C++) for the nRF52840 SoC executing the canonical NLMS filter resides in the designated hardware firmware repository.
