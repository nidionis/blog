> **Status:** canonical BOM · **Owns:** binder-jetting component cost · **Up:** [Binder jetting](README.md)

Component BOM for an 8 m³ binder-jetting machine: €46,000–78,000. The ~€100,000 figure adds R&D and integration.

This is the component BOM (46 000 – 78 000 €). The ~100 000 € figure in [business costs](../../business/costs.md) adds R&D and integration.

To estimate the cost of building such a machine (8 m³ binder jetting), separate the investment in **material/raw components (BOM)** from the cost of **R&D / machining**. At this industrial scale, the budget is dominated by the heavy mechanical structure, the actuators and the high-speed printing system.

Here is an indicative budget estimate for a high-end functional prototype (excluding design and assembly hours):

---

### 1. Structure & Frame & Tank (8 m³)

* **XXL machined-welded steel frame** for vibration support and 15 tons of load.
* **4-column lift system**: oversized ball screws, bearings, transmission shafts and synchronised industrial reducers (with integrated brakes).
* **Tank walls & tray**: thick stainless-steel/aluminium sheet metal with fine powder sealing gaskets.
* *Estimate: **15 000 € to 25 000 €*** (depending on access to in-house or outsourced machining).

### 2. Printing System (Heads, Electronics, Fluid)

* **Industrial printing heads** (e.g., Ricoh or Xaar multi-nozzle heads) + dedicated control cards (Meteor Inkjet type or equivalent).
* **Ink/binder circuit**: peristaltic pumps, negative pressure regulators (meniscus), pressurised reservoirs and automatic purge systems.
* **Gantry and X/Y axes**: high-precision guideways, heavy industrial aluminium profiles or carbon beams, brushless servomotors with absolute encoders.
* *Estimate: **20 000 € to 35 000 €*** (the industrial ink jet core is the most expensive, most sensitive item).

### 3. Scraping & Sand Distribution System

* **Mobile sand hopper** with motorised metering traps.
* **Scraping blade** mounted on cylinders or eccentric with vibration control system.
* **Level sensors** and powder flow management.
* *Estimate: **5 000 € to 8 000 €***.

### 4. Automation, Safety & Power Electronics

* **Industrial Programmable Logic Controller (PLC)** or industrial PC + multiaxis motion cards (LinuxCNC / EtherCAT type).
* **Electrical cabinet**: frequency converters, secured power supplies, emergency stop safety and limit switch sensors.
* *Estimate: **6 000 € to 10 000 €***.

---

### Global estimate (excluding R&D)

| Item | Low range | High range |
| --- | --- | --- |
| **Structure & Lift (8 m³)** | 15 000 € | 25 000 € |
| **Heads & Jet System** | 20 000 € | 35 000 € |
| **Distribution & Scraping** | 5 000 € | 8 000 € |
| **Electronics & Automation** | 6 000 € | 10 000 € |
| **Total components (BOM)** | **46 000 €** | **78 000 €** |

*Note: This amount covers raw materials, mechanical components, power electronics and printing heads only. It does not include intermediate prototypes, head driving software licenses, nor engineering time.*
