# Budget Analysis (30,000 INR Vishwakarma Grant)

By leveraging the hardware you already own (the Nordic RAK4631 MCU, LoRa, TMP117, LIS3DH, and Solar Base Board), we have effectively eliminated ~10,000 INR from the required hackathon budget. 

By pivoting to the **Hybrid Rigid-Fabric** mechanical design, we avoid the exorbitant setup costs of custom Kapton Flexible PCBs (FPC).

This leaves us with the entire 30,000 INR grant to build a medical-grade front-end that rivals a $500 commercial DAQ.

## Finalized Itemized Budget

| Component / Subsystem | Function | Estimated Cost (INR) |
| :--- | :--- | :--- |
| **User Owned Hardware** | nRF52840 MCU, SX1262 LoRa, TMP117, LIS3DH, 18650 Battery, Solar Board | **0** (Already Owned) |
| **Rigid PCB Fab & SMT** | Manufacturing the tiny FR4 "Brain" PCB at JLCPCB/PCBWay | 2,500 |
| **TI ADS1298** | 8-Channel, 24-bit Medical AFE for ECG/EHG | 3,500 |
| **TI TPS7A LDOs** | Ultra-Low Noise voltage regulation for AFE | 500 |
| **ADPD4101 + LEDs** | Optical front-end for SpO2 and continuous NIBP | 3,000 |
| **TI OPA333 (x8)** | Active Electrode buffer amplifiers for zero-noise | 3,000 |
| **Conductive Materials** | Graphene/PEDOT:PSS textiles and shielded cables | 5,000 |
| **Mechanical Connectors** | Medical snap-fasteners for the Rigid-Fabric connection | 1,000 |
| **PHA 3D Printing** | Biodegradable filament for the enclosure shell | 1,000 |
| --- | --- | --- |
| **Total Estimated Cost** | | **~19,500 INR** |

## Budget Buffer
We have a remaining **10,500 INR buffer** from the 30,000 INR grant. This buffer is critical for:
1. Shipping costs from Mouser/DigiKey (which can be high for specialized ICs).
2. Import duties/taxes.
3. Spare parts (It is highly recommended to order 3-5 PCBs in case you burn out a chip during soldering or debugging).
