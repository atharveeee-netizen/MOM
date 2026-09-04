# AURA-MOM PRO: Hackathon Proposal for Vishwakarma Awards

## 1. Problem Statement
Current fetal monitoring solutions (like Cardiotocography/CTG machines) are bulky, expensive (~$10,000+), and require clinical expertise to operate. This severely limits access in rural or low-resource settings, leading to delayed interventions for complications like fetal hypoxia or preterm birth.

## 2. Our Solution: AURA-MOM PRO
AURA-MOM PRO is a low-cost, wearable, multimodal maternal-fetal monitoring belt. It uses an 8-channel biopotential array (fECG/EHG) and acoustic sensors (PVDF) to monitor the fetus and mother simultaneously. 

### Why it wins the Vishwakarma Awards:
*   **Hardware Innovation (Budget-Friendly):** By pairing a 24-bit medical-grade AFE (TI ADS1298) with an ultra-low-power **Nordic nRF52840 (Cortex-M4F)**, we bring the total prototype cost under **30,000 INR**.
*   **Edge AI (Adaptive Filtering):** Instead of relying on computationally heavy algorithms like FastICA which drain battery, we implemented an Edge-optimized **NLMS (Normalized Least Mean Squares)** Adaptive Filter. This $O(N)$ algorithm allows the Cortex-M4F to extract the fetal ECG in real-time, completely offline without crashing loop timing.
*   **Scalability:** The data is sent via BLE to a cross-platform mobile app (Flutter) for the mother, and synced to a robust clinical dashboard (React) for remote triage.

## 3. Proof of Work (The GitHub Repository)
This repository serves as our comprehensive architectural blueprint and proof of work. It contains:
*   **Hardware Specifications & Schematics Plan** (`DESIGN.md`)
*   **DSP / AI Pipeline Architecture** (`ARCHITECTURE.md`)
*   **Dataset Identification & Validation Plan** (`DATASETS_AND_REFERENCES.md`)
*   **Clinical Boundary Rules** (`AGENTS.md`)

## 4. Video Demonstration Plan (The "Audio-Jack" Bench Test)
*(To be recorded and linked here)*
Since we cannot clinically test on a pregnant human during the hackathon, we will demonstrate the hardware acquisition pipeline through a **DAC Audio-Jack Signal Injection Bench Test**. 
We will play the PhysioNet maternal/fetal ECG datasets from a laptop's audio jack, pass the signal through a simple voltage-divider resistor network, and clip it directly to the physical ADS1298 electrodes. This will prove that our hardware and Edge AI adaptive filters can successfully separate the fetal heartbeat in real-time from a physical analog source.
