# Datasets and References

## Training & Validation Datasets
To validate our Hybrid Adaptive Filtering (RLS/NLMS) and PVDF sensor outputs without premature human testing, we will use the following gold-standard public datasets:

1. **PhysioNet Non-Invasive Fetal ECG Database (NIFECG)**
   - **Link:** [https://physionet.org/content/nifecgdb/1.0.0/](https://physionet.org/content/nifecgdb/1.0.0/)
   - **Use Case:** Validating the extraction of fetal QRS complexes from maternal abdominal ECG mixtures.

2. **PhysioNet Term-Preterm EHG Database (TPEHG)**
   - **Link:** [https://physionet.org/content/tpehgdb/1.0.1/](https://physionet.org/content/tpehgdb/1.0.1/)
   - **Use Case:** Validating uterine contraction tracking and preterm birth risk algorithms using abdominal electrohysterography.

3. **Shiraz University Fetal Heart Sounds Database (SUFHS)**
   - **Link:** [https://physionet.org/content/sufhsdb/1.0.1/](https://physionet.org/content/sufhsdb/1.0.1/)
   - **Use Case:** Validating our acoustic PVDF contact sensor pipeline for fetal phonocardiogram (PCG) analysis.

## Open Source Inspirations (GitHub)
Instead of building the software stack from scratch, we will fork or take heavy inspiration from these existing repositories to fit within hackathon timelines:

- **Patient Mobile App (Flutter):**
  - [Remote-pregnancy-monitor](https://github.com/Bhargavi-hash/Remote-pregnancy-monitor)
  - [Pregcare](https://github.com/shree-10/Pregcare)

- **Clinician Dashboard (React):**
  - [Smart Health Monitoring System](https://github.com/vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzHsYDxSMegNeuwBgy1693IeO1BNXnlOoqxCeDgTIT2ev4ISpkoSozIS0oZbdgkT2XMcUCaPROuyoSOUm4hQUBBxlgQKpKKorOekKcm4O69MhyoLgHZ4mZZwSjhzRuGYzpnqMiXNhedxaeDkvv) (For Recharts live-streaming integration).
