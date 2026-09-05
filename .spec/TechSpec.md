# Technical Specification (TechSpec)
## Project: AURA-MOM PRO

### 1. Technology Stack Selection
- **Hardware Tier:** Texas Instruments ADS1298 (24-bit, 8-channel AFE) + RAKwireless RAK4631 (Nordic nRF52840 Cortex-M4F).
- **Power Regulation:** Ultra-Low Noise LDO (Texas Instruments TPS7A series) for clean analog supply (`AVdd`).
- **Signal Integrity:** Shielded Coaxial Cables with Right Leg Drive (RLD) active noise cancellation.
- **Sensors:** 8× biopotential electrodes (PEDOT:PSS/LIG dry electrodes), 2× PVDF acoustic sensors, 6-axis IMU, Temperature sensor, PPG / SpO2 module.
- **Edge AI (DSP):** C/C++ TinyML implementing Normalized Least Mean Squares (NLMS) and O(N) Adaptive Filters.
- **Edge AI (Offline Triage):** Cactus Needle (14MB SLM) running on the Flutter mobile app for offline NLP triage alerts.
- **Frontend Layer (Mobile):** Flutter (BLE IoT Gateway & Federated Learning node).
- **Frontend Layer (Dashboard):** Next.js 16 + React 19 + ThreeUI (SYZYGY Hackathon Stack).
- **Backend Services:** FastAPI + MQTT / WebSockets for live telemetry.
- **Data & Storage:** Supabase Free Tier.

### 2. Mechanical & Manufacturing
- **Enclosure:** Rigid FR4 PCB housed in a PHA (Polyhydroxyalkanoate) biodegradable shell.
- **Belt:** Elastic maternal support band with embedded Graphene electrodes and snap-fasteners.

### 3. Runtime Environment
- **Firmware:** C/C++ on Cortex-M4F, utilizing BLE Data Length Extension (DLE) and 2M PHY. (Do NOT save continuous waveform data to internal Flash NVS).
- **Cloud Backend (AI/ML):** Python (PyTorch/Transformers) utilizing SYZYGY's Unsloth + TRL for Time-Series Transformer training (RoPE, RMSNorm, SwiGLU).
- **Federated Orchestrator:** Aggregates LoRA adapter weights from edge mobile devices.
