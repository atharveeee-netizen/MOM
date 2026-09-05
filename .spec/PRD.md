# Product Requirements Document (PRD)
## Project: AURA-MOM PRO
**Domain:** HEALTH TECH / HACKATHON | **Date:** 2026-09-05 | **Status:** APPROVED

### 1. Objective & Vision
AURA-MOM PRO is a low-cost, wearable, multimodal maternal-fetal monitoring belt designed for the Maker Bhavan Foundation Vishwakarma Awards.
It solves the problem of bulky, expensive (~$10,000+) Cardiotocography (CTG) machines by providing a <30,000 INR prototype utilizing Edge AI (Adaptive Filtering) strictly on the ultra-low-power Nordic nRF52840 (Cortex-M4F).

### 2. User Personas
- **Primary Operator:** Pregnant mothers in rural or low-resource settings needing remote monitoring.
- **Clinician / Doctor:** Healthcare professionals using a remote dashboard for triage and urgent assessment.
- **Evaluator:** Hackathon judges evaluating the hardware innovation and edge-compute efficiency.

### 3. Core Functional Requirements
- **FR-1 (Hardware):** 8-channel biopotential array (fECG/EHG) and acoustic sensors (PVDF) for simultaneous maternal/fetal monitoring.
- **FR-2 (Edge AI):** NLMS (Normalized Least Mean Squares) Adaptive Filter running entirely offline on Cortex-M4F to extract fetal ECG in real-time.
- **FR-3 (Mobile/Cloud):** Data transmitted via BLE to a cross-platform mobile app (Flutter), and synced to a robust clinical dashboard (React) for remote triage.
- **FR-4 (Cost Constraint):** Total prototype cost strictly under 30,000 INR, with a target of measurable SNR improvement via DSP.

### 4. Medical-Claim & Privacy Boundaries
- **Must NOT** claim independent diagnosis of fetal hypoxia, preterm birth, or preeclampsia.
- **Must NOT** claim exact early-warning times without prospective validation.
- **Must** output a triage state: `NORMAL` / `REVIEW` / `URGENT ASSESSMENT` rather than a disease diagnosis.
- **Privacy (Federated Learning):** The system must NOT stream sensitive raw physiological waveforms (ECG/EHG) to a centralized cloud. Instead, it must utilize a Federated Learning approach where the mobile app trains a local LoRA adapter and only syncs the weight updates.
