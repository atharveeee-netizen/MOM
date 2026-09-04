# AURA-MOM PRO: Hackathon Proposal for Vishwakarma Awards

## 1. Problem Statement
Current fetal monitoring solutions (like Cardiotocography/CTG machines) are bulky, expensive (~$10,000+), and require clinical expertise to operate. This severely limits access in rural or low-resource settings, leading to delayed interventions for complications like fetal hypoxia or preterm birth.

## 2. Our Solution: AURA-MOM PRO
AURA-MOM PRO is a low-cost, wearable, multimodal maternal-fetal monitoring belt. It uses an 8-channel biopotential array (fECG/EHG) and acoustic sensors (PVDF) to monitor the fetus and mother simultaneously. 

### Why it wins the Vishwakarma Awards:
*   **Hardware Innovation (Budget-Friendly):** By pairing a 24-bit medical-grade AFE (TI ADS1298) with an ultra-low-cost ESP32-S3 microcontroller, we bring the total prototype cost under **30,000 INR**.
*   **Edge AI (Adaptive Filtering):** Instead of relying on computationally heavy algorithms like FastICA which drain battery, we implemented an Edge-optimized **NLMS (Normalized Least Mean Squares)** Adaptive Filter. This $O(N)$ algorithm allows the ESP32-S3 to extract the fetal ECG in real-time, completely offline without crashing loop timing.
*   **Scalability:** The data is sent via BLE to a cross-platform mobile app (Flutter) for the mother, and synced to a robust clinical dashboard (React) for remote triage.

## 3. Proof of Work (The GitHub Repository)
This repository serves as our comprehensive architectural blueprint and proof of work. It contains:
*   **Hardware Specifications & Schematics Plan** (`DESIGN.md`)
*   **DSP / AI Pipeline Architecture** (`ARCHITECTURE.md`)
*   **Dataset Identification & Validation Plan** (`DATASETS_AND_REFERENCES.md`)
*   **Clinical Boundary Rules** (`AGENTS.md`)

## 4. Video Demonstration Plan
*(To be recorded and linked here)*
We will demonstrate the hardware acquisition pipeline through a **Signal-Injection Bench Test**. By injecting known maternal and fetal ECG signals into our ADS1298 board, we will prove that our Edge AI adaptive filters can successfully separate the fetal heartbeat in real-time.
