# Context: AURA-MOM PRO

## Core System Architecture
AURA-MOM should be built as a modular multimodal monitoring platform rather than trying to put every sensor into one belt. The abdominal belt is the core physiological acquisition unit; maternal optical sensing and validated home measurements are companion modules.

### Modules
*   **ABDOMINAL BELT:** 8× biopotential electrodes, 2× PVDF acoustic sensors, 6-axis IMU, Temperature sensor (Baby + uterus + maternal ECG + motion)
*   **MATERNAL MODULE:** PPG / SpO₂, HR / HRV, Respiratory-rate context (Maternal cardiovascular context)
*   **COMPANION HOME DEVICES:** Validated Bluetooth upper-arm BP cuff, Optional urine protein / Hb / glucose (Clinical context; not inferred from PPG alone)
*   **EDGE + PHONE:** AFE → filtering → artifact rejection → signal separation → features → multimodal fusion → trend/risk flag (Local processing + clinician-facing telemetry)

### Core Signal Flow
8-channel abdominal array + PVDF + IMU + temperature + maternal PPG/BP → signal-quality assessment → maternal/fetal/uterine signal separation → FHR/MHR/EHG/acoustic/movement features → personalized baseline → multimodal risk stratification → normal / needs review / urgent clinical assessment.

## Medical-Claim Boundaries
*   The prototype should be presented as a multimodal maternal-fetal monitoring and triage platform. It should not be presented as independently diagnosing fetal hypoxia, preterm birth or preeclampsia until those claims are clinically validated.
*   Do not claim that AURA directly measures fetal oxygen saturation or fetal blood pH.
*   Do not claim that PPG/SDPTG alone diagnoses preeclampsia. Pair risk monitoring with actual BP and clinician assessment.
*   Do not claim exact early-warning times (for example, 2–6 hours, 7–14 days or 2–4 weeks) without prospective validation.
*   Do not claim automated fetal-kick counting is 100% accurate. Use 'movement-event detection' until validated.
*   The system should support clinical review, not replace CTG, ultrasound, BP assessment or emergency medical care.

## Immediate Engineering Checklist
- [ ] Freeze the V1 sensor list and channel map.
- [ ] Create KiCad schematic for ADS1298 + electrode inputs + RLD/reference.
- [ ] Design PVDF charge-amplifier stage and verify noise floor.
- [ ] Define synchronized timestamp format across ECG/EHG/PVDF/IMU.
- [ ] Create a signal-injection test fixture before any human testing.
- [ ] Prepare dataset preprocessing scripts for NIFECG and TPEHG.
- [ ] Define objective acceptance metrics for every subsystem.
- [ ] Document every hardware revision and firmware/DSP version.
- [ ] Keep all clinical-alert thresholds configurable and clearly marked as research until validated.
