# Power from displaced air

> **Status:** reference · **Owns:** air-power formulas and their limits · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../2cheval/engines/manson/power-from-air.md)

This page records the standard “power from displaced air” formulas and explains which one the atmospheric Manson actually uses.

## 1. Standard engine formulas

### 1.1 Mean effective pressure (MEP)

$$P = \frac{p_{me} \times V_d \times N}{2 \times 60}$$

| Symbol | Meaning | Unit |
|---|---|---:|
| `p_me` | Mean effective pressure | Pa |
| `V_d` | Total displacement | m³ |
| `N` | Engine speed | rpm |
| `P` | Power | W |

The factor **2** is the four-stroke cycle (one working cycle every two revolutions); use **1** for a two-stroke. Typical `p_me`: atmospheric gasoline 8–12 bar, diesel 7–10 bar, boosted 15–30 bar.

Example: 2.0 L at 6,000 rpm with `p_me` = 10 bar gives ≈ **100 kW ≈ 136 hp**.

### 1.2 Mass airflow

$$\dot m_{air} = \frac{V_d \times N \times \rho_{air} \times \eta_v}{2 \times 60} \qquad P_{th} = \dot m_{air} \times \frac{PCI}{AFR} \qquad P_{eff} = P_{th} \times \eta_{cyl}$$

- `ρ_air` ≈ 1.2 kg/m³ at 20 °C; `η_v` = volumetric efficiency (0.8–0.95 atmospheric, > 1 boosted).
- `PCI` = lower heating value (gasoline ≈ 44 MJ/kg, diesel ≈ 43 MJ/kg).
- `AFR` = stoichiometric air/fuel ratio (gasoline ≈ 14.7 kg air/kg fuel).
- `η_cyl` = cylinder conversion efficiency, typically 0.30–0.40.

### 1.3 Comparison

| Approach | Advantage | Limit |
|---|---|---|
| MEP | Simple, one engine datum | `p_me` must be known |
| Airflow | Physical, links filling and fuel | Needs `η_v`, PCI, AFR, `η_cyl` |

The key relation is `P ∝ V_d × N × p_me`: power is proportional to displacement, speed and mean effective pressure.

## 2. Why the Manson is different

- **Atmospheric pressure** — no boost, so `p_me` stays low.
- **Open cycle with external combustion** — straw burns in the [rocket stove](../../energy/rocket-stove/README.md); air is the working fluid, not a fuel-air mixture.
- **Piston displacer** — `V_a = V_c / 2`.
- **Reference frequency 2 Hz** — not an rpm-scale engine.
- **Low overall efficiency** — 5 % baseline, `ΔT` = 180 K.

The MEP formula assumes a pressure cycle and a four-stroke; the airflow formula assumes a fuel-air mixture. Neither describes the Manson directly. They are useful for comparison, not sizing.

**Order-of-magnitude check.** For the 2 hp engine, `V_d` = 135.5 L. At 2 Hz (120 rpm), 1.47 kW through the MEP formula implies `p_me` ≈ **0.11 bar**, about 1 % of a gasoline engine's 8–12 bar. The atmospheric Manson cannot build a high-pressure cycle; it extracts work from a small temperature swing, hence the large volume at low frequency.

## 3. Project formula

$$P = \eta \cdot \rho \cdot f \cdot V_a \cdot C_p \cdot \Delta T$$

At the baseline, `P = 21,708 × V_a` (W, `V_a` in m³):

| Target | Air volume `V_a` | Chamber `V_c` | Diameter `D` (D = L) |
|---|---:|---:|---:|
| 2 ch | 67.76 L | 135.53 L | 55.67 cm |
| 6 ch | 203.3 L | 406.6 L | 80.3 cm |
| 20 ch | 677.63 L | 1 355.26 L | 119.94 cm |

The full table and geometry are in [sizing](sizing.md). The formula is first-order; it ignores port timing, leakage and heat exchange.

## 4. Fuel-side limit

At 5 %, 30 kg / 20 min at 12 MJ/kg gives **15 kW ≈ 20.4 hp**. At 15 % the same feed gives **45 kW**. The retained power is the minimum of the air-volume power and the fuel power. See [fuel](fuel.md) and [efficiency](../../levers/efficiency.md).

## 5. What the standard formulas still teach

- MEP explains why boost and high rpm matter for cars; the Manson cannot use boost and runs at 2 Hz, so it needs volume.
- The airflow relation links air mass, fuel and power; in the Manson the working air and combustion air are separate, but the heat source must still match the working-air flow.
- For a conventional engine, use MEP or airflow. For the atmospheric Manson, use the project formula and check the fuel cap.

## See also

- [Sizing](sizing.md)
- [Thermodynamics](thermodynamics.md)
- [Fuel](fuel.md)
- [Pressure lever](../../levers/pressure.md) — what a sealed variant would change
- [Biomass calorific capacity](../../energy/rocket-stove/biomass-calorific.md)
- [Glossary](../../GLOSSARY.md)
