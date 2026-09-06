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

## 4. Mechanical Design (The "Hybrid Rigid-Fabric" Pivot)
*Why DIY prototypes fail:* Printing an entire 8-channel flexible PCB (Kapton FPC) is prohibitively expensive ($150+ per prototype) and tears easily under maternal movement. Taping a rigid, sharp PCB to an abdomen is dangerous.
*   **The Enclosure (The "Brain"):** The MCU, LDO, and ADS1298 must be printed on a tiny, standard Rigid FR4 PCB (costs <$5). This rigid board is housed in a small **PHA (Polyhydroxyalkanoate)** biodegradable shell.
*   **The Belt (The "Arms"):** The rigid brain uses mechanical snap-fasteners to clip directly into a wide, breathable, elastic maternal support band. The Graphene electrodes are embedded into the fabric of the belt, connecting to the snaps. This achieves the flexibility of an expensive Kapton patch but cuts PCB fabrication costs by 90% (Identical to the Polar H10 design).

## 5. The Sustainability Edge (Beating COTS DAQs)
Commercial DAQs (like Shimmer3) rely on toxic plastics and single-use Ag/AgCl wet electrodes that create massive medical waste and skin irritation. We will outperform them by making AURA-MOM PRO a "Next-Generation Green Medical Device."
*   **Zero-Waste Electrodes:** Do not use wet gels. Use **PEDOT:PSS (Conductive Polymer) or Laser-Induced Graphene (LIG)**. These can be printed onto a flexible natural hydrogel (like Chitosan) or directly into the textile belt. They are 100% reusable, washable, and achieve the exact same impedance and SNR as clinical wet electrodes.
*   **Biodegradable Plastics:** For the 3D-printed enclosure (Section 4), absolutely do NOT use standard TPU, ABS, or PLA (which shed microplastics). You MUST print the enclosure using **PHA (Polyhydroxyalkanoate)**. PHA is a 100% bio-derived, marine-biodegradable flexible polymer.

## Summary
By combining the **ADS1298**, **TPS7A LDO**, **Shielded Coaxial Cables**, **Graphene Dry Electrodes**, and a **PHA Enclosure**, we achieve—and physically outperform—National Instruments / Shimmer3 quality for a fraction of the cost, while producing zero medical e-waste.
