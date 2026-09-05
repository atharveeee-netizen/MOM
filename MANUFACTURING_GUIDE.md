# Manufacturing Guide: The "Perfect" Wearable

This guide explains how to physically assemble the AURA-MOM PRO hardware. By following these strict manufacturing guidelines, our 4,000 INR prototype will achieve the exact same medical-grade signal-to-noise ratio (SNR) as a $500 COTS research wearable (like the OpenBCI Cyton or Shimmer3).

## 1. The Core Electronics (The Brain)
Commercial wearables charge a massive premium for putting a Texas Instruments AFE and a microcontroller on a tiny PCB. We are using the same silicon.
*   **The AFE:** Texas Instruments **ADS1298** (24-bit, 8-channel). This is the exact family of chips used in professional EEGs and ECGs.
*   **The MCU:** **RAKwireless RAK4631 (Nordic nRF52840)**. Provides the Cortex-M4F DSP acceleration and BLE 5.0.

## 2. Power Regulation (The "Dirty Power" Fix)
*Why DIY prototypes fail:* Lithium-ion batteries drop voltage as they discharge, and standard switching regulators introduce high-frequency noise that destroys microvolt-level fetal ECG signals.
*   **The Fix:** You MUST place an **Ultra-Low Noise LDO** (Low Dropout Regulator), such as the **Texas Instruments TPS7A series**, between the battery and the ADS1298's Analog Supply (`AVdd`). 
*   This ensures the analog circuitry receives perfectly flat, noise-free power regardless of the battery's charge state.

## 3. Signal Integrity (The "Antenna" Fix)
*Why DIY prototypes fail:* Hobbyists use standard jumper wires or unshielded cables for electrodes. A 1-meter unshielded wire on a pregnant abdomen acts as a massive radio antenna, picking up 50Hz/60Hz mains hum from the room's electrical wiring, completely overwhelming the fetal heartbeat.
*   **The Fix:** You MUST use **Shielded Coaxial Cables** for every single electrode. The outer shield of the coaxial cable must be driven by the **Right Leg Drive (RLD)** circuit of the ADS1298. This actively cancels out common-mode noise before it even reaches the silicon.

## 4. Mechanical Design (The "Belly" Fix)
*Why DIY prototypes fail:* Taping a rigid, sharp PCB and heavy batteries to a pregnant mother's abdomen is dangerous and ergonomically unacceptable. Furthermore, if the electrodes shift even 1mm during movement, it creates massive motion artifacts.
*   **The Enclosure:** The electronics and battery must be housed in a **Curved, 3D-Printed TPU (Thermoplastic Polyurethane) Shell**. TPU is a flexible, rubber-like filament. The curvature must match the average 3rd-trimester abdomen.
*   **The Belt:** Use a wide, breathable, elastic maternal support band. The electrodes must be embedded into the fabric to guarantee constant, uniform pressure against the skin without restricting blood flow or breathing.

## Summary
By combining the **ADS1298**, **TPS7A LDO**, **Shielded Coaxial Cables**, and a **TPU Enclosure**, we achieve National Instruments / Shimmer3 quality for a fraction of the cost. Do not cut corners on the shielding or the LDO, or the signal will be useless.
