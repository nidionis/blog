# coil-estimation — Stirling Beta (source note, not normative)

> **Status:** source note · **Not normative** · **Canonical summary:** [linear alternator](../linear-alternator.md)

This is an in-depth analysis and recommended parameter ranges for the design of the coils and magnets of a free-piston Beta Stirling engine.

The main challenge with a linear alternator coupled to a Stirling engine (particularly at low frequencies like 2 Hz) is to maximize the magnetic flux density to compensate for the low piston displacement speed, while avoiding blocking the mechanics with unwanted magnetic forces (cogging torque).

---

## 1. Magnetic Circuit Design (Magnets and Piston)

The motor piston is the moving part here (the mover). Its mass is critical because it participates, with the gas pressure, in the system's resonance frequency.

* **Magnetic Material:**
  * **Neodymium-Iron-Boron (NdFeB):** Grades **N42 to N52**. This is the standard for maximizing magnetic field ($B_r$ of $1{,}3$ to $1{,}45\text{ T}$).
  * *Thermal note:* Ensure the alternator is located in the cold zone of the Stirling. If the temperature at the magnets exceeds 80°C, prefer high-temperature magnets (grades ending in SH, UH, EH) or switch to **Samarium-Cobalt (SmCo)**, though it is more fragile and expensive.

* **Dimensions of cylindrical/annular magnets:**
  * **Outer diameter:** **40 mm to 150 mm** (depends on the bore of your power cylinder).
  * **Thickness per magnet:** **5 mm to 20 mm**. Thicker magnets avoid demagnetization under heavy load, but drastically increase the moving mass.

* **Magnetic Topology:**
  * **Stack of alternating poles (N-S / S-N):** The classic approach. Magnets are separated by soft iron disks (3–10 mm thick) that redirect the flux radially toward the coils.
  * **Cylindrical Halbach network (advanced):** Orients the magnetic field almost exclusively outward (toward the coils), increasing flux by ~20–30% and removing the need for a heavy central iron core.

* **Air gap:**
  * **0.5 mm to 1.5 mm.** One of the most critical parameters. The larger the gap, the more the magnetic field collapses. This requires extremely rigorous mechanical guidance (dry or aerostatic bearings).

---

## 2. Stator Design (Generator and Mover Coils)

You have two subsystems: a generator coil (energy recovery on the motor piston) and a mover coil (displacer control).

### A. Generator Coil (Motor Piston)

Since induced voltage ($E$) depends on the rate of flux change ($E = N \cdot d\Phi/dt$), low frequency (e.g. 2 Hz) forces compensation with huge turn counts and very powerful magnets.

* **Conductor size:** 0.5–4 mm².
* **Wire type:** For 2–10 Hz, standard enamelled copper wire (Grade 2, 200°C) is sufficient.

* **Turn count ($N$):** Typical 500–5000 turns per phase.

* **Iron in stator (Coreless vs. Iron Core):**
  * *Coreless:* No cogging torque. Major advantage for a low-inertia Stirling.
  * *Iron core:* Maximizes flux, but magnets will "cog" against stator teeth.

### B. Mover Coil (Displacer)

The displacer only moves the gas between zones (no compression). The required force is minimal.

* **Target force:** 10 N to 50 N.
* **Winding:** 200–600 turns of fine wire.
* **Control:** H-bridge or inverter, providing a phase-shifted signal (~90° advance on the motor piston) to optimize the PV cycle.

---

## 3. Synthesis Matrix for Sizing

| Parameter | "Micro-generator" range (10W - 50W) | "Heavy generator" range (~1kW - 2kW @ 2Hz) |
| --- | --- | --- |
| **Magnet outer dia.** | 20 mm - 40 mm | 80 mm - 150 mm |
| **Magnet grade** | N42 | N52 (or mass Halbach) |
| **Mover mass** | 0.1 kg - 0.5 kg | 5 kg - 20 kg |
| **Stroke** | 10 mm - 30 mm | 100 mm - 200 mm |
| **Air gap** | 0.3 mm - 0.5 mm | 0.8 mm - 1.5 mm |
| **Admissible current density** | 4–6 A/mm² | 2–4 A/mm² |
| **Turn count** | 300 - 800 | 3000 - 6000+ |
| **Copper wire dia.** | 0.4 mm - 0.8 mm | 1.5 mm - 2.5 mm |
| **Stator type** | Coreless | Strongly recommended laminated iron |

### Final recommendations for integration

At very low frequency (2 Hz) and high power (1.5 kW), the naturally generated voltage is low and the current extremely high, generating lots of heat (Joule losses, $P = R \cdot I^2$). It is often strategic to **wind several independent sections** along the cylinder travel and connect them in series.

Moreover, an active electronic load control system is essential: by varying the current pulled through the coil in real time, a magnetic damping driven by the system is created that acts exactly like a virtual gearbox, keeping the Stirling oscillation perfectly stable.
