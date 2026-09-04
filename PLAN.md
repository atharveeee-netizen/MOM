# Project Plan: AURA-MOM PRO

## Purpose
This document hands over the proposed AURA-MOM architecture to the hardware, firmware, DSP/AI, mechanical and clinical-research team. It defines the V1 prototype architecture, sensing roles, signal-processing pipeline, data flow, validation plan and key safety/claim boundaries.

## Domain
Health Tech • Maternal, Adolescent & Menstrual Health Tech • Emergency Response & Remote Monitoring

## V1 Monitoring Targets
| What to monitor | How | Priority |
| :--- | :--- | :--- |
| **Fetal heart rate** | 8-channel abdominal ECG / fECG | Primary V1 target |
| **Maternal ECG / heart rate** | Same abdominal biopotential array + optional PPG | Primary V1 target |
| **Uterine electrical activity** | EHG from abdominal electrodes | Primary V1 target |
| **Fetal acoustic activity** | 2× PVDF contact sensors | Supporting modality |
| **Motion / artifact** | 6-axis IMU | Essential for signal-quality gating |
| **Maternal blood pressure** | Validated Bluetooth upper-arm cuff | Companion measurement; important for hypertensive-risk surveillance |
| **Temperature** | Skin/body-contact temperature sensor | Context / fever trend |
| **SpO₂ / pulse** | PPG optical module | Maternal context, not standalone diagnosis |
| **Fetal movement events** | IMU + acoustic/biopotential context | Trend/event detection; validate before clinical claim |

## Prototype Build Order
1. Build ADS1298-based 8-channel acquisition first.
2. Prove clean maternal ECG acquisition and channel synchronization.
3. Add controlled fetal-ECG signal injection and validate separation.
4. Add EHG branch and verify contraction-like waveforms.
5. Add two PVDF channels with charge amplifiers.
6. Add IMU and implement motion/artifact gating.
7. Add PPG/temperature module as a separate maternal module.
8. Integrate BLE + phone dashboard.
9. Add validated Bluetooth BP cuff integration.
10. Only then implement multimodal risk scoring and the final belt enclosure.
