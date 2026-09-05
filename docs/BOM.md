# Bill of Materials (BOM) & Estimated Prototype Cost (Unverified Hardware)
**Project:** AURA-MOM PRO (Vishwakarma Prototype)
**Version:** 1.0 (Embedded NLMS Variant)

This BOM details the *estimated* prototype cost of the proposed AURA-MOM PRO hardware based on supplier listings. *Note: This represents a software-in-the-loop validated design; physical hardware assembly has not yet been completed.*

| Item | Description | Part Number | Qty | Unit Cost (USD) | Total Cost (USD) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Microcontroller (SoC)** | Cortex-M4F with BLE 5.0 (1MB Flash, 256KB RAM) | nRF52840-QIAA | 1 | $3.50 | $3.50 |
| **Analog Front End (AFE)** | 8-Channel, 24-Bit ADC for ECG/EHG (SPI) | ADS1298IPAG | 1 | $14.20 | $14.20 |
| **Power Management** | LDO Regulator (3.3V out) | TPS73633DBVR | 1 | $1.15 | $1.15 |
| **Battery Management** | Li-Po Charger IC | BQ24075 | 1 | $1.40 | $1.40 |
| **Battery** | 3.7V 2000mAh Li-Po Cell | Generic 2000mAh | 1 | $4.50 | $4.50 |
| **Passive Components** | Resistors, Capacitors (0402/0603) | Various | ~50 | $0.01 | $0.50 |
| **Connectors** | 10-pin Snap connectors for ECG leads | ECG Snap | 4 | $0.25 | $1.00 |
| **PCB Manufacturing** | 4-Layer FR4 (Prototype Run - JLCPCB/PCBWay) | Custom | 1 | $2.00 | $2.00 |
| **Enclosure** | 3D Printed Medical-Grade PLA/Resin | Custom | 1 | $3.00 | $3.00 |

### Cost Analysis
- **Total Estimated BOM Cost (1 Unit):** $31.25 USD (~₹2,600 INR)
- **Estimated BOM Cost (Volume > 10,000):** ~$18.50 USD (~₹1,500 INR)

### Battery Life Estimation (nRF52840 + ADS1298)
- **ADS1298 Active Current (1kSPS):** ~6 mA
- **nRF52840 Active Current (NLMS processing + BLE TX):** ~8 mA (Peak), ~4 mA (Avg)
- **Total System Current:** ~10 mA
- **Battery Capacity:** 2000 mAh
- **Estimated Continuous Runtime:** ~200 Hours (>8 Days of continuous fetal monitoring on a single charge)
