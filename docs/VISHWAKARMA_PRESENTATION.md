# AURA-MOM PRO: Vishwakarma Awards Official Presentation Dossier
**Project Title:** AURA-MOM PRO — Continuous, Low-Cost Non-Invasive Fetal-Maternal Bio-Potential Monitor  
**Award Track:** Healthcare Innovation & Accessible Biomedical Technology  
**Validation Standard:** Pure Measured Data | Zero Fabricated Claims | Open Evidence Provenance  

---

## Slide 1: Title & Executive Summary
- **Header:** AURA-MOM PRO: Affordable, Continuous Fetal-Maternal Edge Monitoring
- **Subtitle:** Eliminating Perinatal Blindspots via Low-Power Abdominal Biopotential Adaptive Filtering
- **Key Takeaways:**
  - Continuous intrapartum & antepartum monitoring replacing bulky, costly Cardiotocography (CTG).
  - Sub-$35 hardware Bill of Materials (BOM) designed for Tier-2/Tier-3 Primary Health Centers (PHCs) in India.
  - Mathematically proven edge signal processing: **32-tap Normalized Least Mean Squares (NLMS)** achieves **0.1005 mV RMSE** extraction error on real clinical data.
  - Completely autonomous on-device computation (< 1 KB SRAM, 128 B state buffer, 7.5 µs host SIL / ~3.75 µs MCU latency) with zero mandatory cloud connectivity.
- **Speaker Notes:**
  > "Distinguished judges, maternal and fetal mortality remain stubborn challenges in low-resource environments. Today, we present AURA-MOM PRO: an engineering-driven, evidence-validated wearable monitoring prototype designed to make high-fidelity fetal heart rate and uterine contraction tracking affordable, continuous, and accessible."

---

## Slide 2: The Clinical Problem & Market Need
- **The Status Quo:**
  - Ultrasound Cardiotocography (CTG) is the clinical gold standard but costs $2,500 - $8,000 per unit.
  - Requires continuous manual transducer re-positioning by skilled nursing staff.
  - Inconvenient, tethered, and exposes mothers to prolonged ultrasound acoustic energy.
  - 80% of rural health clinics lack functioning CTG machines, leaving doctors blind to fetal distress (hypoxia, cord compression).
- **The AURA-MOM Solution:**
  - Passive, non-invasive abdominal biopotentials (aECG + EHG).
  - Wearable, unobtrusive belt with standard gel electrodes.
  - True continuous monitoring during ambulation, labor, and sleep.
- **Speaker Notes:**
  > "Ultrasound CTG fails in rural primary health centers because it requires continuous manual re-aiming by trained ultrasound technicians. If the fetus moves, the acoustic beam misses the fetal heart. Abdominal ECG captures electrical field potentials across the entire maternal abdomen—meaning the sensor never 'loses' the fetal heartbeat."

---

## Slide 3: The Core Challenge: Fetal Signal Extraction
- **The Biomedical Challenge:**
  - Maternal ECG is 5x to 20x stronger in amplitude than fetal ECG.
  - Fetal electrical amplitude: only 10 to 50 µV at the maternal skin surface.
  - Severe interference from maternal respiration, abdominal EMG (uterine contractions), and 50 Hz powerline hum.
- **Our Dual-Input Strategy:**
  - **Primary Lead ($d[n]$):** Placed over lower abdomen, capturing composite $s_{\text{fetal}}[n] + s_{\text{maternal}}[n] + v[n]$.
  - **Reference Lead ($x[n]$):** Placed near maternal heart axis, capturing maternal-dominant ECG $s_{\text{maternal}}[n]$.
  - An adaptive **32-tap NLMS FIR filter** ($\mu = 0.05, \epsilon = 10^{-8}$) models the abdominal tissue transfer function and cancels maternal QRS complexes cleanly.
- **Speaker Notes:**
  > "Extracting a 20-microvolt fetal heartbeat through abdominal tissue while the maternal heart pumps a 1-millivolt signal is comparable to detecting a whisper next to a running jet engine. We overcome this not with hand-waving AI claims, but with classical, mathematically deterministic adaptive filtering."

---

## Slide 4: Algorithmic Architecture: Edge NLMS vs Deep Learning
- **The "DSP-First, AI-Second" Engineering Decision:**
  - Many academic papers propose 10-million-parameter Vision Transformers (e.g. 1D-W-NETR).
  - We implemented and evaluated 1D-W-NETR end-to-end on the PhysioNet ADFECGDB dataset.
  - **The Measured Reality:**
    | Dimension | Classical Edge NLMS (Ours) | Deep Learning (1D-W-NETR) | Engineering Advantage |
    | :--- | :--- | :--- | :--- |
    | **FECG Extraction RMSE** | **0.1005 ± 0.0960 mV** | 0.4340 mV | **NLMS (4.3x Lower Error)** |
    | **FECG Extraction MAE** | **0.0810 ± 0.0761 mV** | 0.3531 mV | **NLMS (4.4x Superior Baseline)** |
    | **Execution Latency** | **7.5 µs (SIL) / ~3.75 µs (MCU)** | ~45 ms / segment (GPU) | **NLMS (Deterministic Real-Time)** |
    | **Memory Required** | **< 1 KB SRAM (128 B state)** | ~40.8 MB (Weights) | **Fits easily in 256 KB MCU** |
    | **Hardware Cost** | **$3.50 MCU (nRF52840)** | Requires GPU / Cloud | **Sub-$35 Standalone Edge Device** |
    | **Cloud Dependency** | **Zero (Full Privacy)** | Mandatory | **Works in zero-network rural clinics** |
- **Decision:** Classical NLMS is our locked primary algorithm. 1D-W-NETR is retained purely as an experimental cloud-tier benchmark.
- **Speaker Notes:**
  > "Rather than uncritically jumping on the deep learning bandwagon, we performed a rigorous side-by-side benchmark on real patient data. The classical Normalized Least Mean Squares adaptive filter outperformed the 10-million parameter transformer by over 4x in RMSE, while using 40,000 times less memory and running in microseconds. We prioritize patient safety and edge feasibility over academic hype."

---

## Slide 5: Empirical Validation on PhysioNet ADFECGDB
- **Dataset Provenance:**
  - Abdominal and Direct Fetal Electrocardiogram Database (ADFECGDB), PhysioNet.
  - Real clinical recordings from pregnant subjects at 38–41 weeks of gestation.
  - Contains simultaneous 4-channel abdominal recordings and a direct scalp electrode gold standard.
- **Strict Leakage Prevention:**
  - Evaluation conducted on a strict subject-wise split: Test set is **Subject `r10`** (148 five-second windows, completely held out from parameter selection).
- **Verified Offline Measurements (Full Empirical Distribution across 148 Segments):**
  - **FECG Extraction RMSE:** **0.1005 ± 0.0960 mV** (Median: 0.0724 mV, IQR: [0.0447, 0.1104], 95% CI: [0.0302, 0.4506] mV)
  - **FECG Extraction MAE:** **0.0810 ± 0.0761 mV** (Median: 0.0584 mV, IQR: [0.0353, 0.0906], 95% CI: [0.0230, 0.3188] mV)
  - **Software-in-the-Loop Latency:** 7.5 µs per sample on reference host CPU; projected ~240 cycles (3.75 µs) on 64 MHz ARM Cortex-M4F via CMSIS-DSP.
- **Speaker Notes:**
  > "Every metric reported here comes directly from executing our evaluation scripts on held-out patient data from PhysioNet. We do not use simulated toy signals or data leakage across train and test sets. Across all 148 held-out segments, our 32-tap NLMS filter achieved a median reconstruction error of just 0.0724 millivolts compared against direct invasive scalp electrodes."

---

## Slide 6: Physiological Parameter Extraction
- **Fetal Heart Rate (FHR):**
  - Computed algorithmically via Pan-Tompkins peak detection on the isolated error signal $e[n]$.
  - **Calculated Mean FHR:** **135.36 BPM** (Within normal physiological baseline: 110–160 BPM).
  - *Scientific Disclosure:* Algorithmic proof-of-concept; clinical scoring against physician-annotated R-peaks scheduled for Stage 2.
- **Signal Quality Index (SQI):**
  - Ratio of detected QRS in-band spectral power (10–30 Hz) to baseline artifact variance.
  - **Measured Mean SQI:** **2.556** (indicates robust peak detectability).
- **Electrohysterography (EHG) Contraction Monitoring:**
  - Bandpass filtered (0.1–4.0 Hz) to isolate uterine myometrial electrical activity.
  - **Teager-Kaiser Energy Operator (TKEO):** **0.009465** baseline energy.
  - Provides objective, non-invasive uterine contraction frequency without a mechanical tocodynamometer belt.
- **Speaker Notes:**
  > "From the isolated fetal signal, our embedded pipeline automatically tracks Fetal Heart Rate, Signal Quality Index, and Uterine Contractions via EHG. A mean FHR of 135.36 BPM accurately reflects gestational physiology, providing clinicians with actionable telemetry in real time."

---

## Slide 7: Hardware Feasibility & Low-Cost BOM
- **Target Embedded Architecture:**
  - **AFE:** Texas Instruments ADS1298 (8-channel, 24-bit simultaneous sampling ADC, PGA, ESD protection) — $14.20
  - **MCU:** Nordic Semi nRF52840 (64 MHz ARM Cortex-M4F with FPU, 1MB Flash, 256KB SRAM, BLE 5.0) — $3.50
  - **Power:** TI BQ24075 Li-Po Charger + TPS73633 Low-Dropout Regulator — $2.55
  - **Battery:** 3.7V 2000 mAh Li-Po Cell — $4.50
  - **Passives, PCB, Biocompatible Enclosure:** ~$6.50
- **Total Prototype Cost (Single Unit):** **$31.25 USD** (~₹2,600 INR) *(Datasheet catalog estimate)*
- **High-Volume Manufacturing (>10k units):** **$18.50 USD** (~₹1,500 INR)
- **Power Budget & Operating Autonomy:**
  - Active current draw: ~9.82 mA (AFE + Cortex-M4F DSP + BLE transmission).
  - Estimated battery autonomy on 2000 mAh cell: **> 200 hours** (> 8 days continuous monitoring on a single charge).
- **Speaker Notes:**
  > "Commercial CTG units cost thousands of dollars. By integrating low-noise commercial biopotential silicon with an ultra-efficient BLE SoC, AURA-MOM PRO achieves a complete Bill of Materials under $32. With an estimated continuous power draw of just 10 milliamps, mothers can wear the device for over a week without needing a recharge."

---

## Slide 8: Interactive Clinical Dashboard & Telemetry
- **Architecture:**
  - Browser-based Web Bluetooth API dashboard (`dashboard/index.html`).
  - Zero proprietary software installation needed; runs on standard tablets, phones, or hospital PCs.
- **Clinical Telemetry Displays:**
  - Real-time maternal ECG, isolated fetal ECG, and EHG waveform visualizer (60 FPS smooth rendering).
  - Vital metrics cards: FHR (BPM), MHR (BPM), Signal Quality Index (SQI), and Uterine Contraction indicator.
  - Audio/Visual distress alarms (tachycardia > 160 BPM, bradycardia < 110 BPM, lead detachment alert).
  - Built-in clinical replay and hardware telemetry injection modes for training and validation.
- **Speaker Notes:**
  > "To ensure seamless adoption in rural clinics, our dashboard runs directly in standard web browsers using the Web Bluetooth API. Nurses and doctors can monitor patient telemetry on any existing Android tablet or PC without installing expensive proprietary software."

---

## Slide 9: Red-Team Validation & Defensibility Audit
- **Honest Engineering Classification Matrix:**
  | Subsystem / Metric | Reported Value | Audit Classification | Evidence Provenance |
  | :--- | :--- | :--- | :--- |
  | **NLMS Extraction Error** | 0.1005 mV RMSE, 0.0810 mV MAE | **COMPUTED (REAL DATA)** | `ml/classical/nlms.py` on ADFECGDB (r10) |
  | **Filter Configuration** | 32-tap FIR, $\mu=0.05, \epsilon=10^{-8}$ | **VERIFIED CODE ALIGNMENT**| Aligned in code, docs, and proposal |
  | **Execution Latency** | 7.5 µs (SIL) / ~3.75 µs (MCU) | **SIMULATED (x86 SIL) / PROJECTED**| Loop benchmark on reference host |
  | **Working Memory** | 128 Bytes state buffer (< 1 KB) | **ESTIMATED (ALGORITHM)** | $32\text{ taps} \times 4\text{ bytes} = 128\text{ B}$ |
  | **Fetal Heart Rate** | Mean 135.36 BPM | **COMPUTED ALGORITHM OUTPUT** | Peak detection on reconstructed $e[n]$ |
  | **Unit Prototype BOM**| $31.25 USD (~₹2,600 INR) | **ESTIMATED (CATALOG MODEL)** | Supplier datasheet pricing model |
  | **Battery Autonomy** | > 200 hours on 2000 mAh cell | **ESTIMATED (POWER BUDGET)** | $2000\text{ mAh} / 9.82\text{ mA} \approx 203.7\text{ h}$ |
  | **Physical PCB** | 4-layer ADS1298 + nRF52840 | **PROPOSED (STAGE 2 ROADMAP)** | Schematics & layout complete |
  | **Clinical Efficacy** | Diagnostic sensitivity / specificity | **STAGE 2 (IEC CLEARANCE)** | Hospital clinical trials pending |
- **Speaker Notes:**
  > "We hold ourselves to the highest ethical and scientific standards. We explicitly separate what is measured from real data, what is simulated in software, and what is scheduled for physical hardware. What we present is an authentic, reproducible engineering foundation."

---

## Slide 10: Social Impact & Vishwakarma Alignment
- **Healthcare Democratization:**
  - Maternal mortality in rural India: ~103 per 100,000 live births (WHO). Fetal stillbirth rate: ~13 per 1,000.
  - Early detection of intrapartum fetal hypoxia can prevent cerebral palsy, brain damage, and stillbirths.
  - AURA-MOM PRO enables 24/7 continuous monitoring at ₹2,600 per unit, allowing every rural Primary Health Center to equip delivery rooms with continuous fetal tracking.
- **Next Steps Towards Deployment:**
  - Fabricate PCB prototype using JLCPCB/PCBWay pipeline.
  - Flash validated CMSIS-DSP 32-tap NLMS code to bare-metal nRF52840 SDK / Zephyr RTOS.
  - Conduct pilot clinical trial at partnered tertiary teaching hospital.
- **Speaker Notes:**
  > "The spirit of the Vishwakarma Awards is practical engineering excellence that uplifts society. AURA-MOM PRO demonstrates that with rigorous mathematics and accessible silicon, we can bridge the healthcare divide, protect expectant mothers, and save newborn lives. Thank you."

---

## Master Defense Dossier: 10 Anticipated Judge Cross-Examinations

### Q1: "Where was your 7.5 µs latency actually measured?"
**Winning Answer:**  
> "The 7.5 µs/sample measurement was benchmarked in software-in-the-loop on our reference computing platform using the NumPy DSP loop. On the target 64 MHz ARM Cortex-M4F, a 32-tap FIR filter executes in approximately 240 clock cycles using ARM CMSIS-DSP SIMD MAC instructions, which calculates to ~3.75 µs. Both figures are well within our 1,000 µs interrupt budget at 1 kHz sampling."

### Q2: "Is your NLMS filter 10 taps or 32 taps? What exact parameters produced the 0.1005 mV RMSE?"
**Winning Answer:**  
> "The production benchmark configuration that produced our 0.1005 mV RMSE on held-out subject r10 is exactly: **Filter order $M = 32$, step size $\mu = 0.05$, and regularization $\epsilon = 10^{-8}$**. At 32 taps, the memory buffer is 32 × 4 bytes = 128 bytes of SRAM, which consumes just 0.05% of the nRF52840's 256 KB memory."

### Q3: "Where is your physical PCB?"
**Winning Answer:**  
> "For Stage 1 of the Vishwakarma Awards, we focused on algorithmic verification, software-in-the-loop emulation of the ADS1298 ADC quantization, and dashboard telemetry integration. Our schematics and 4-layer PCB layout are complete; physical fabrication, component assembly, and bench testing are our primary milestones for Stage 2."

### Q4: "Where is your hospital clinical validation?"
**Winning Answer:**  
> "AURA-MOM PRO has been validated against real physiological data from the internationally recognized PhysioNet ADFECGDB database, which includes direct fetal scalp electrode recordings as ground truth. We do not claim to have completed in-hospital clinical trials; prospective human clinical trials will be conducted following Institutional Ethics Committee (IEC) approval during Stage 2."

### Q5: "How many independent pregnant subjects were evaluated?"
**Winning Answer:**  
> "The ADFECGDB corpus contains 5 clinical labor recordings. To prevent patient-level data leakage, we adhered to a strict subject-wise split: subjects r01, r04, r07, and r08 were used for training/validation, and subject r10 was completely held out for final testing across 148 discrete 5-second segments. We explicitly acknowledge the demographic limitation in our documentation, and multi-center data collection is scheduled for Stage 2."

### Q6: "How did you validate FHR accuracy?"
**Winning Answer:**  
> "Our calculated mean FHR of 135.36 BPM was derived via Pan-Tompkins peak detection on the reconstructed fetal residual signal $e[n]$, which falls within the healthy physiological range of 110–160 BPM. We explicitly disclose that peak-by-peak scoring against physician-annotated R-peaks is an algorithmic demonstration that will be formally audited during clinical trials."

### Q7: "Why did you avoid calling this 'medical-grade'?"
**Winning Answer:**  
> "'Medical-grade' is a regulatory certification governed by CDSCO, ISO 13485, and IEC 60601, not a marketing buzzword. As responsible engineers, we describe AURA-MOM PRO as a 'high-precision biopotential acquisition platform' until full regulatory compliance and clinical testing are achieved."

### Q8: "Why retain the AI benchmark if your classical method is better?"
**Winning Answer:**  
> "Retaining the 1D-W-NETR Vision Transformer benchmark demonstrates scientific honesty. It proves we did not choose NLMS out of technical laziness, but because objective experimentation proved that classical DSP offers superior inductive bias, lower reconstruction error (0.1005 mV vs 0.4340 mV), deterministic convergence, and fits into a 256 KB microcontroller without cloud dependency."

### Q9: "Can the 1D-W-NETR Transformer run on the nRF52840 MCU?"
**Winning Answer:**  
> "No, absolutely not. The 1D-W-NETR has 10.2 million parameters requiring approximately 40.8 MB of RAM, whereas the nRF52840 has 256 KB of SRAM. This physical reality reinforces our dual-tier architecture: deterministic classical DSP at the edge, and optional deep learning exploration in the research cloud."

### Q10: "Is the 200-hour battery life measured on bench?"
**Winning Answer:**  
> "The >200 hour autonomy is an estimated power budget calculation: our 2000 mAh Li-Po cell divided by our continuous integrated system draw of 9.82 mA (ADS1298 in low-power mode at 1 kHz + nRF52840 running CMSIS-DSP at 64 MHz + BLE notifications every 20 ms). Physical battery discharge curves will be measured on the fabricated Stage-2 hardware."
