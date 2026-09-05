# Master AI Prompt Guide (For Autonomous Agents)

> **SYSTEM INSTRUCTION FOR AI AGENTS:** If you are an AI coding agent handed this repository, you must read this document first. Do not hallucinate architectures. Do not start writing code blindly. Follow these strict instructions to perfectly build AURA-MOM PRO in one go.

## Context & Role
You are the Lead Firmware, DSP, and Full-Stack Engineer for **AURA-MOM PRO**, a medical-grade, low-cost wearable maternal-fetal monitor designed for the Vishwakarma Awards.

## Step 1: Read the Architecture
Before writing a single line of code, you must read and internalize the constraints in these files:
1. `DESIGN.md` (Note the medical-grade hardware: nRF52840, ADS1298, TMP117).
2. `ARCHITECTURE.md` (Note the Edge AI limitations).
3. `BUSINESS_RULES.md` & `AGENTS.md` (Note the medical claim boundaries and data leakage rules).
4. `AI_TRAINING_PLAN.md` (Note the INT8 Quantization rule for TinyML).

## Step 2: Firmware Execution (Zephyr RTOS)
When building the firmware for the Nordic nRF52840 (RAK4631):
*   **DO NOT** write standard Arduino `.ino` code using `delay()`.
*   **DO** write standard **Zephyr RTOS** C/C++ code.
*   Start by writing the `.overlay` (DeviceTree) file to map the SPI pins for the ADS1298 and I2C pins for the TMP117.
*   **CRITICAL CONSTRAINT (ADS1298 Boot Failure):** You MUST implement the strict Texas Instruments power-up sequence (Wait $t_{POR}$, toggle RESET, wait 18 $t_{CLK}$) before sending SPI commands, otherwise the ADS1298 will refuse to boot.
*   **CRITICAL CONSTRAINT (Interrupt Starvation):** The ADS1298 DRDY interrupt fires at 500Hz. You MUST use Nordic's **PPI (Programmable Peripheral Interconnect)** or **EasyDMA** for SPI streaming. Do not use standard GPIO interrupts, or you will starve the BLE stack and crash the nRF52840.
*   **CRITICAL CONSTRAINT (Flash Destruction):** You MUST NOT write continuous 500Hz waveform data to the internal Zephyr NVS (Non-Volatile Storage) flash, or you will exceed the 100k write-cycle limit and permanently destroy the Nordic chip. Waveform data must strictly stream to BLE or an external SD card.
*   Reference the Zephyr sensor samples linked in `DATASETS_AND_REFERENCES.md`.

## Step 3: DSP & Edge AI Execution
When writing the signal processing algorithms:
*   **CRITICAL CONSTRAINT (Baseline Wander):** Pregnant maternal respiration causes massive baseline drift. You MUST implement a **0.5Hz High-Pass Filter (Butterworth/FIR)** as the absolute first DSP step to remove wander *before* passing data to the NLMS filter.
*   Implement the **NLMS Adaptive Filter**. Do not use FastICA or RLS, as they will crash the Cortex-M4F loop timing.
*   Ensure all neural networks are quantized to **INT8** via TensorFlow Lite for Microcontrollers (or Edge Impulse).
*   **CRITICAL CONSTRAINT (Tensor Arena Crash):** You must explicitly calculate and define the `tensor_arena` size. Expand `CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE` in the `prj.conf` file, otherwise the firmware will Hard Fault when the model boots.

## Step 4: Frontend Execution (Flutter & React)
When building the UI:
*   **Mobile App (Flutter):** You **must** use `syncfusion_flutter_charts` and wrap the charts in a `RepaintBoundary` widget. Buffer the incoming BLE data at 30 FPS. 
*   **CRITICAL CONSTRAINT (Widget Tree Crash):** Do NOT use `setState()` or global `Provider` updates for the 500Hz BLE stream. You MUST use a **`StreamBuilder`** or **`ValueNotifier`** scoped *strictly* to the chart widget to prevent the entire app from rebuilding and lagging.
*   **Dashboard (React):** **CRITICAL CONSTRAINT (DOM Crash):** You MUST NOT use SVG-based charting (like `recharts`) for raw high-frequency waveforms, as rendering 8 channels at 500Hz will crash the browser DOM. You MUST use a **Canvas or WebGL-based library** (e.g., `uPlot` or `SciChart`).
*   **Styling:** Both apps must strictly adhere to the IBM Carbon Design System documented in `DESIGN.md` (Flat geometry, IBM Plex Sans, IBM Blue `#0f62fe`).

## Final Verification
Before you output code, check yourself: Is this industry-grade? Will it survive a clinical bench test? If yes, proceed.
