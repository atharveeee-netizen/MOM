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

4. **Induced Cesarean EHG DataSet (ICEHG DS)**
   - **Use Case:** Advanced evaluation of uterine activity models, offering a newer validation benchmark alongside TPEHG.

## Open Source Inspirations (GitHub)
Instead of building the software stack from scratch, we will fork or take heavy inspiration from these existing repositories to fit within hackathon timelines:

- **Patient Mobile App (Flutter):**
  - [Remote-pregnancy-monitor](https://github.com/Bhargavi-hash/Remote-pregnancy-monitor)
  - [Pregcare](https://github.com/shree-10/Pregcare)

- **Clinician Dashboard (React):**
  - [Smart Health Monitoring System](https://github.com/vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzHsYDxSMegNeuwBgy1693IeO1BNXnlOoqxCeDgTIT2ev4ISpkoSozIS0oZbdgkT2XMcUCaPROuyoSOUm4hQUBBxlgQKpKKorOekKcm4O69MhyoLgHZ4mZZwSjhzRuGYzpnqMiXNhedxaeDkvv) (For Recharts live-streaming integration).

## Advanced Firmware & Edge AI References (For Autonomous Coding Agents)
When developing the C++ firmware and Edge AI models for the Nordic nRF52840, refer to these repositories for architectural guidance:

1. **Zephyr RTOS ECG Integration:**
   - [Zephyr Project Sensor Samples](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/sensor) (Use as reference for writing DeviceTree `.overlay` files and I2C/SPI sensor ingestion).
2. **TinyML / Edge Impulse on Cortex-M4F:**
   - [Official Edge Impulse Nordic Firmware](https://github.com/edgeimpulse/firmware-nordic-nrf52840dk-nrf5340dk) (Reference for Data Forwarder ingestion and C++ model deployment).
   - [Tinycardia](https://github.com/infinesm/Tinycardia) (Reference for lightweight ECG anomaly detection and R-R interval feature extraction on Cortex-M4).
