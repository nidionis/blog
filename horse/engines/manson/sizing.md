# Manson sizing

> **Status:** canonical · **Owns:** volume, diameter and power table · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../2cheval/engines/manson/sizing.md)

This page derives swept volume and diameter from power, efficiency, `ΔT` and frequency. **All rows use the same 5 % baseline**; other efficiencies are covered by the [efficiency lever](../../levers/efficiency.md).

## Assumptions

See the [glossary](../../GLOSSARY.md) for baseline values:

- Overall efficiency **η = 5 %** (initial tier, see [thermodynamics](thermodynamics.md)).
- Temperature difference **ΔT = 180 K** — `T_hot = 200 °C`, `T_cold = 20 °C`.
- Frequency **f = 2 Hz**.
- Air heat capacity **Cp = 1 005 J/(kg·K)**, density **ρ = 1.2 kg/m³**.
- Geometry: cylinder with **D = L** (a table convention, not a manufacturing rule).

## Formulas

$$P_{th} = \frac{P_m}{\eta} \qquad \dot m = \frac{P_{th}}{C_p \cdot \Delta T} \qquad V_a = \frac{\dot m / \rho}{f}$$

For a cylinder of diameter `D` and length `L = D`:

$$V_c = 2 V_a = \frac{\pi D^2}{4} \cdot D \quad\Rightarrow\quad D = \left(\frac{4 V_c}{\pi}\right)^{1/3}$$

The factor 2 is the displacer rule: the working air is half the geometric chamber. See [steady state](thermodynamic-steady.md).

## Results at 5 %

<!-- calc:sizing:en -->
| Mechanical power | Thermal power | Mass flow | Air volume `V_a` | Chamber `V_c` | Diameter `D` |
|---:|---:|---:|---:|---:|---:|
| **1.47 kW** (2 ch) | 29.4 kW | 0.1626 kg/s | 67.76 L | 135.53 L | **55.67 cm** |
| **2.94 kW** (4 ch) | 58.8 kW | 0.3253 kg/s | 135.53 L | 271.05 L | **70.14 cm** |
| **4.41 kW** (6 ch) | 88.3 kW | 0.4879 kg/s | 203.29 L | 406.58 L | **80.29 cm** |
| **5.88 kW** (8 ch) | 117.7 kW | 0.6505 kg/s | 271.05 L | 542.10 L | **88.38 cm** |
| **8.83 kW** (12 ch) | 176.5 kW | 0.9758 kg/s | 406.58 L | 813.16 L | **101.16 cm** |
| **14.71 kW** (20 ch) | 294.2 kW | 1.6263 kg/s | 677.63 L | 1,355.26 L | **119.94 cm** |
<!-- /calc:sizing:en -->

A better efficiency reduces the volume in proportion to `1/η`: at 15 %, the 2 hp chamber is about 45 L instead of 135.5 L. Diameter falls only as the cube root. See [levers](../../levers/README.md).

## Fuel limit

The heat source adds a second cap: **30 kg of biomass in 20 min** = 90 kg/h at **12 MJ/kg** ([biomass](../../energy/rocket-stove/biomass-calorific.md)):

$$P_{th,max} = 90 \times \frac{12\,000}{3\,600} = 300\ \text{kW} \qquad P_{m,max} = 0.05 \times 300 = 15\ \text{kW} \approx 20.4\ \text{ch}$$

The 20 ch row consumes **29.4 kg per 20 min**, exactly at the feed limit **at 5 %**. At 15 % the same feed allows 45 kW, but the chamber and materials must still support it. The retained power is `min(P_air, P_fuel)`; for 15 kW, `V_a` ≈ 0.691 m³, `V_c` ≈ 1.382 m³ and `D` ≈ 1.207 m (D = L). See [fuel](fuel.md) and [efficiency](../../levers/efficiency.md).

## Geometry note

`D = L` is only a convention. A flat chamber can reach the same volume with a larger diameter and a shorter stroke. At `D = 135 cm`, 70 mm of chamber height gives ≈ 1.5 hp, 118–142 mm gives 2–3 hp, and 947 mm gives 20 hp. See [volume and weight](../../levers/volume-weight.md) and the [first prototype](costs/prototype.md).

The old table `sizing.diametre.md` mixed units and volume assumptions; it is archived in [archive/deprecated/sizing.diametre.md](../../archive/deprecated/sizing.diametre.md).

## See also

- [Thermodynamics](thermodynamics.md) — Carnot ceiling and tiers
- [Steady state](thermodynamic-steady.md) — CAD check
- [Fuel](fuel.md) — consumption table
- [Levers](../../levers/README.md) — pressure, temperature, frequency, efficiency
- [SCAD model](scad/README.md)
- [Nuclear variant](../../energy/nuclear/README.md)
