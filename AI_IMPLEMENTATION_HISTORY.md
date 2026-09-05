# Implementation Plan: Finalized Budget & Fabrication Strategy

You raised a brilliant point: custom Flexible PCBs (FPCs) are notoriously expensive and risky to manufacture on the first try. 

Based on deep GitHub research and current PCB fabrication costs (JLCPCB/PCBWay), here is the reality and the proposed strategic pivot to finalize our budget.

## User Review Required
Please review the research findings and the proposed "Hybrid" fabrication pivot. If you approve, I will generate the final `BUDGET_ANALYSIS.md` and update our manufacturing guidelines.

---

### 1. The GitHub FPC Reality
I searched GitHub for open-source Flexible PCB designs for the ADS1298.
*   **The Reality:** There are **zero** ready-to-manufacture 8-channel flexible patches. Repositories like `OpenElectronicsLab/ads1298-breakout` or `uECG` exist, but they are designed for standard Rigid FR4 boards. Designing an FPC from scratch is a massive undertaking because you must design "serpentine" traces so the copper doesn't snap when the mother moves.
*   **The Fabrication Cost:** While raw FPC film is cheap ($20), paying a factory to do Surface Mount Assembly (SMT) to precisely solder the tiny ADS1298 and Nordic chip onto a flexible substrate involves high tooling/stencil fees. A single prototype run will cost you roughly **$150 - $200 (12,000 - 16,000 INR)**. If there is a design flaw, you have to pay it again.

### 2. The Strategic Pivot (Hybrid Rigid-Fabric)
To guarantee we stay under the 30,000 INR limit and drastically reduce hardware risk, we should abandon the "All-in-One FPC" idea. Instead, we adapt the industry standard used by the $90 Polar H10 heart rate strap:

*   **The "Brain" (Rigid PCB):** We print the MCU, LDO, and ADS1298 on a tiny, standard Rigid FR4 PCB. This costs **< 1,000 INR** to manufacture and assemble at JLCPCB.
*   **The "Arms" (Textile Belt):** The rigid brain snaps into a washable, stretchable maternity belt that has the conductive Graphene/PEDOT:PSS electrodes printed directly into the fabric. 
*   **Why this wins:** We get the exact same flexibility and comfort as an FPC patch, but we reduce the PCB fabrication cost by **90%**.

### 3. The Finalized Budget Preview (30,000 INR Grant)
*(Assuming you already own the RAK4631, SX1262 LoRa, TMP117, LIS3DH, and Solar Board)*

*   **Rigid PCB Fab & Assembly (JLCPCB):** ~2,500 INR
*   **TI ADS1298 (8-Channel AFE):** ~3,500 INR
*   **TI TPS7A (Ultra-Low Noise LDOs):** ~500 INR
*   **ADPD4101 (Optical cNIBP sensor):** ~3,000 INR
*   **Active Electrode Op-Amps (OPA333 x8):** ~3,000 INR
*   **Graphene/Conductive Textile Materials:** ~5,000 INR
*   **TPU/PHA 3D Printing (Enclosure):** ~1,000 INR
*   **Total Estimated Cost:** **~18,500 INR**

We have an **11,500 INR buffer** remaining from the 30k grant for shipping, taxes, and inevitable hardware mistakes!

---

## Open Questions
> [!IMPORTANT]
> Do you approve abandoning the expensive Kapton FPC in favor of the **Hybrid Rigid-Fabric (Polar H10 style)** design? This cuts our fabrication costs by 90% and guarantees we stay well under the 30,000 INR limit.
