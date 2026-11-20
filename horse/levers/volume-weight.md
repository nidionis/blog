# Volume and weight — the size lever

> **Status:** canonical lever · **Owns:** volume, geometry and mass scaling · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/volume-poids.md)

The engine is a large, slow, low-pressure machine. Volume is the main design variable: power is proportional to working air volume, and cast material is proportional to chamber volume. This is the lever the baseline already uses.

## Definitions

- `V_c` — total geometric chamber volume (both chambers).
- `V_a` — working air volume, `V_a = V_c / 2` because of the piston displacer.
- `D = L` — a **convention** for the tables, not a manufacturing rule. A flat or tall chamber can hold the same volume.

## Power, volume, mass at the baseline

| Target | `V_a` | `V_c` | `D` (`D = L`) | Cast Al mass at 66 % | Mechanical specific power |
|---:|---:|---:|---:|---:|---:|
| 2 hp | 67.8 L | 135.5 L | 55.7 cm | 242 kg | 6.1 W/kg |
| 4 hp | 135.5 L | 271.1 L | 70.1 cm | 483 kg | 6.1 W/kg |
| 6 hp | 203.3 L | 406.6 L | 80.3 cm | 725 kg | 6.1 W/kg |
| 20 hp | 677.6 L | 1 355.3 L | 119.9 cm | 2 415 kg | 6.1 W/kg |

At constant technology, **power and chamber mass grow together**. Four times the power means four times the aluminium, but only `4^(1/3) ≈ 1.59` times the diameter. That is the cube-root law: big engines are not proportionally wider, they are heavier.

The mass column is the cast chamber only, at 66 % fill. It excludes walls, piston, rod, insulation, stove and alternator, so it is a lower bound.

## Flat or tall: the same volume

At `D = 135 cm` the cross-section is 1.431 m², so chamber height sets the power:

| Chamber height | `V_c` | Power at 5 % | Equivalent |
|---:|---:|---:|---:|
| 70 mm | 0.100 m³ | 1.09 kW | 1.5 hp |
| 118 mm | 0.169 m³ | 1.84 kW | 2.5 hp |
| 142 mm | 0.203 m³ | 2.21 kW | 3 hp |
| 947 mm | 1.355 m³ | 14.71 kW | 20 hp |

The **1.5 m³ PLA envelope** is a print envelope, not a 1.5 m³ chamber. The first 2–3 hp build uses only 118–142 mm of chamber height inside that envelope; the same diameter can later host 20 hp with a taller chamber. See [prototype](../engines/manson/costs/prototype.md).

## The lever

- **Volume** is linear in power: easy to scale, expensive in material.
- **Mass** is linear in volume: the engine's specific power stays near 6 W/kg mechanical unless pressure, frequency or temperature changes.
- **Higher pressure / frequency / temperature** shrink the chamber for the same power, but add seals, speed or material cost. The mass optimum is not the volume optimum.

## Pessimistic reading

Use the 2 hp row. It is the smallest engine that meets the market promise, and its 242 kg of cast aluminium is already a two-person handling problem. Do not assume a lightweight engine: the project trades mass for simplicity.

## See also

- [Sizing](../engines/manson/sizing.md) — the canonical table
- [Recycled material](../business/recycled-material.md) — aluminium mass and can count
- [Pressure](pressure.md) · [Frequency](frequency.md) · [Temperature](temperature.md) — the compactness levers
