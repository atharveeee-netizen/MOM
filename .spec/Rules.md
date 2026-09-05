# Agent & Development Directives (Rules.md)
## Project: AURA-MOM PRO

### 1. ASD-STE100 Technical English Standard
- Eliminate generic AI buzzwords ("revolutionize", "delve", "seamlessly integrate", "cutting-edge").
- Write procedural instructions under 20 words per sentence.
- Use active voice with clear subjects.

### 2. Clinical Rules & Machine Learning Boundaries (CRITICAL)
- **Zero Data Leakage:** When training ML models for EHG preterm detection, you must NEVER oversample the dataset before splitting into train/test sets. All synthetic oversampling (e.g., SMOTE) must occur strictly on the training fold.
- **Strict Claims:** Output is a triage state (`NORMAL` / `REVIEW` / `URGENT ASSESSMENT`), not a medical diagnosis. Do not claim to measure fetal oxygen saturation or blood pH directly.
- **Firmware Safety:** Do NOT save continuous waveform data to internal Flash NVS to avoid hardware destruction; use external SD or RAM ring buffers.

### 3. Anti-Slop Code Directives
- No placeholder variables or mockup dummy text.
- 100% type-annotated code (TypeScript strict / Python typing).
- Zero hardcoded credentials.
