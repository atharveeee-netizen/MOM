# AI Agent Instructions for AURA-MOM PRO

When generating code, designing algorithms, or providing technical advice for this project, AI agents must strictly adhere to the following rules:

## 1. Clinical Claim Boundaries (CRITICAL)
- **Do not diagnose.** Output a triage state: `NORMAL` / `REVIEW` / `URGENT ASSESSMENT` rather than a disease diagnosis.
- **Do not hard-code disease thresholds** from concept documents into the first prototype. Thresholds such as specific entropy, conduction-velocity or SDPTG cut-offs require clinical validation and should initially be treated as research features.
- Avoid using terminology that implies 100% accuracy (e.g., use "movement-event detection" instead of "automated fetal-kick counting").
- Never claim the device directly measures fetal oxygen saturation or fetal blood pH.
- Never claim that PPG/SDPTG alone diagnoses preeclampsia.

## 2. Safety & Power
- Ensure the hardware design remains a **battery-only patient-connected prototype**. Do NOT propose mains-connected patient operation designs.
- Prevent raw PVDF from connecting directly to a low-impedance MCU ADC; always include a high-impedance charge amplifier in schematics/discussions.

## 3. Signal Processing Constraints
- Mains interference suppression must target the **50-Hz India deployment context**. Ensure filters do not distort fetal QRS morphology.
- Base sampling strategy on the highest rate required by the fetal-ECG/acoustic branch (approx. 500-1000 samples/s). EHG and lower-rate branches should be derived digitally via decimation after anti-alias filtering.

## 4. Development Workflow
- Follow the exact 10-step "Prototype Build Order" outlined in `PLAN.md`.
- Ensure all clinical-alert thresholds in firmware/software are exposed as configurable parameters and clearly marked with a `TODO(research)` or `RESEARCH_ONLY` tag.
