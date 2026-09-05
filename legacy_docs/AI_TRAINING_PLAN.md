# AI Training Plan (Edge AI / TinyML)

This document defines the exact methodology for training and deploying the AURA-MOM PRO Edge AI algorithms onto the Nordic nRF52840 (Cortex-M4F) processor.

## 1. Data Ingestion & Preprocessing
To train our models without requiring premature human trials, we will ingest the public datasets (`NIFECG`, `TPEHG`) using the **Edge Impulse Data Forwarder** or Python scripts.
*   **Windowing:** Time-series data must be sliced into **2-second windows** at a **500Hz sampling rate**.
*   **Filtering (Pre-ML):** Before feeding data into any neural network, it must pass through an NLMS (Normalized Least Mean Squares) adaptive filter to remove maternal baseline wander and 50Hz mains noise.

## 2. Feature Engineering
Raw waveforms are too large for TinyML. The DSP block must extract features before inference:
*   **For Fetal ECG:** Extract R-R intervals and QRS amplitude.
*   **For Uterine EHG:** Extract Sample Entropy and Teager-Kaiser Energy.
*   **CRITICAL CONSTRAINT:** Do **NOT** oversample the EHG dataset (e.g., using SMOTE) before splitting into train/test folds. This causes "data leakage." Oversampling must only occur on the training fold.

## 3. Neural Network Architecture (TinyML)
*   **Model Type:** 1D-CNN (Convolutional Neural Network) or lightweight Autoencoder for anomaly detection.
*   **Constraint:** The model must be compiled using **TensorFlow Lite for Microcontrollers**.
*   **Quantization:** The model **MUST be quantized to INT8**. Float32 models will exceed the RAM capacity of the nRF52840.

## 4. Deployment
Deploy the trained model as a **C++ Library** (via Edge Impulse or TFLite) and integrate it directly into the Zephyr RTOS firmware loop. Inference must execute within the sampling interval window (e.g., < 2ms execution time) to prevent dropping BLE packets.
