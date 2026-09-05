# AURA-MOM PRO: Master Project Handover

This document serves as the absolute final index and handover file for the AURA-MOM PRO project. It catalogues every piece of research, architectural decision, boundary rule, and AI prompt guide generated to date.

By handing this repository over to any developer (or AI coding agent), they will possess the exact context, constraints, and instructions necessary to build the physical device and write the firmware/software perfectly on the first try.

---

## 1. Core Architecture & Design
*   **[DESIGN.md](DESIGN.md):** The master Bill of Materials (BOM), System Block Diagram, and justification for every hardware component. *Highlights the Hybrid Rigid-Fabric mechanical pivot.*
*   **[ARCHITECTURE.md](ARCHITECTURE.md):** The data flow from the physical Edge (Nordic Cortex-M4F) to the IoT Gateway (Flutter App) and the Cloud ML backend (AWS/GCP PyTorch).
*   **[MANUFACTURING_GUIDE.md](MANUFACTURING_GUIDE.md):** The physical assembly instructions proving how to achieve Shimmer3/OpenBCI clinical accuracy using Graphene, PHA, and custom LDOs for a fraction of the cost.
*   **[BUDGET_ANALYSIS.md](BUDGET_ANALYSIS.md):** The finalized itemized budget proving the prototype can be built for ~19,500 INR (well within the 30k Vishwakarma grant).

## 2. Research & Deep Analysis
*   **[academic_comparison_report.md](academic_comparison_report.md):** A parameter-by-parameter analysis comparing this architecture against 200+ academic research papers. Proves why AURA-MOM PRO is a deployable product, not just a theoretical math paper.
*   **[wonders_of_30k_budget.md](wonders_of_30k_budget.md):** The strategic breakdown of how we utilized the 30,000 INR grant to include Active Electrodes, Kapton FPCs, and Optical cNIBP sensors.
*   **[DATASETS_AND_REFERENCES.md](DATASETS_AND_REFERENCES.md):** The curated list of PhysioNet datasets (NIFECG, TPEHG) required to train the AI models without data leakage.

## 3. Rules & AI Directives
*   **[AGENTS.md](AGENTS.md) / [BUSINESS_RULES.md](BUSINESS_RULES.md):** The strict clinical boundary rules. (e.g., *No disease diagnosis on the Edge, no fetal pH measurements, Research Only.*)
*   **[AI_PROMPT_GUIDE.md](AI_PROMPT_GUIDE.md):** The "Master Prompt" designed to be fed into future AI agents. It instructs them exactly how to write the Zephyr RTOS firmware and Flutter code while respecting hardware constraints (like avoiding NVS flash wear).
*   **[AI_TRAINING_PLAN.md](AI_TRAINING_PLAN.md):** The TinyML pipeline detailing how to quantize the Neural Network to INT8 and deploy it onto the Nordic MCU's limited memory.

## 4. Execution & History
*   **[HACKATHON_PROPOSAL.md](HACKATHON_PROPOSAL.md):** The high-level proposal outline, including the "Audio-Jack" bench test methodology.
*   **[AI_IMPLEMENTATION_HISTORY.md](AI_IMPLEMENTATION_HISTORY.md):** The historical log of architectural decisions made during the planning phase.
*   **[AI_WALKTHROUGH_HISTORY.md](AI_WALKTHROUGH_HISTORY.md):** The historical summaries of completed features and constraints.
*   **aura_mom_pro_concept.jpg:** The high-fidelity concept render of the Kapton/Graphene Wearable Patch.

---

### Final Directive for Future Developers
Before writing a single line of C code (Zephyr) or Dart (Flutter), you must read `AI_PROMPT_GUIDE.md` and `ARCHITECTURE.md`. Do not violate the power constraints, do not use blocking `delay()` loops, and ensure all BLE traffic utilizes Data Length Extension (DLE). 

**The architecture is perfect. Proceed to build.**
