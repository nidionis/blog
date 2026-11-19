# Manson sizing

> **Status:** canonical · **Owns:** volume, diameter and power table · **Up:** [M Reloaded](README.md)

This page derives swept volume and diameter from power, efficiency, ΔT and frequency. All values share the same assumptions.

## Assumptions

See the [glossary](../../GLOSSARY.md) for baseline values:

- Overall efficiency: **η = 5 %** (tier initial, see [thermodynamics](thermodynamics.md)).
- Temperature difference: **ΔT = 180 K** — Carnot cycle at 200°C: `T_hot = 200°C`, `T_cold = 20°C` (ambient, see [thermodynamics](thermodynamics.md), table row 200 °C → 180 °C).
- Frequency: **f = 2 Hz**
- Air heat capacity: **Cp = 1 005 J/(kg·K)**
- Air density: **ρ = 1.2 kg/m³**
- Geometry: cylinder with **D = L**

## Formulas

$$P_{th} = \frac{P_m}{\eta}$$

$$\dot m = \frac{P_{th}}{C_p \cdot \Delta T}$$

$$V_{cycle} = \frac{\dot m / \rho}{f}$$

For a cylinder of diameter `D` and length `L = D`:

$$V = \frac{\pi D^2}{4} \cdot D \quad\Rightarrow\quad D = \left(\frac{4V}{\pi}\right)^{1/3}$$

## Results

2 ch = marketing, 6 ch = lab need, 20 ch = lab extreme.

| Mechanical power (kW) | Mechanical power (ch) | Thermal power | Mass flow | Air volume `V_cycle` | Chamber volume `V_c = 2·V_cycle` | Diameter (D = L) |
|---:|---:|---:|---:|---:|---:|---:|
| **1.47 kW** | 2 ch | 29.4 kW | 0.1626 kg/s | 67.76 L | 135.53 L | **55.67 cm** |
| **2.94 kW** | 4 ch | 58.8 kW | 0.3253 kg/s | 135.53 L | 271.05 L | **70.14 cm** |
| **4.42 kW** | 6 ch | 88.5 kW | 0.4890 kg/s | 203.75 L | 407.50 L | **80.35 cm** |
| **5.88 kW** | 8 ch | 117.7 kW | 0.6506 kg/s | 271.10 L | 542.20 L | **88.38 cm** |
| **8.83 kW** | 12 ch | 176.6 kW | 0.9762 kg/s | 406.76 L | 813.52 L | **101.18 cm** |
| **14.71 kW** | 20 ch | 294.2 kW | 1.6263 kg/s | 677.63 L | 1355.26 L | **119.94 cm** |

The air volume (`V_cycle`) is half the chamber volume: displacer rule (see [Thermodynamic steady state](thermodynamic-steady.md)).

## Notes

- Diameter depends on the `D = L` assumption. A flatter cylinder is possible; only the volume relation changes.
- The old table `sizing.diametre.md` mixed units and volume assumptions and is archived in [archive/deprecated/sizing.diametre.md](../../archive/deprecated/sizing.diametre.md).
- The matching fuel flow is in [fuel](fuel.md).

## See also

- [Thermodynamics](thermodynamics.md)
- [Fuel](fuel.md)
- [SCAD model](scad/README.md)
- [Nuclear variant](../../energy/nuclear/README.md)
