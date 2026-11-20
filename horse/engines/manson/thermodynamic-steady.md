# Steady-state check — CAD sketch and flat geometry

> **Status:** canonical check · **Owns:** steady-state cross-check · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../2cheval/thermodynamic-steady.md)

The canonical power table is in [sizing](sizing.md). This page only checks two things: that the parametric CAD sketch is consistent with the `V_a = V_c / 2` rule, and what the same volume means at the prototype diameter `D = 135 cm`.

## Basis

$$P = \eta \rho f V_a C_p \Delta T \qquad V_a = \frac{V_c}{2}$$

Pessimistic baseline: `η` = 5 %, `ΔT` = 180 K, `f` = 2 Hz, `ρ` = 1.2 kg/m³, `Cp` = 1 005 J/(kg·K). See [thermodynamics](thermodynamics.md) and [glossary](../../GLOSSARY.md).

## CAD sketch

The [piston sketch](scad/piston.scad) uses `inner_r = 70 mm` and a chamber height of about 70 mm. It is illustrative, not the product drawing.

| Quantity | Value |
|---|---:|
| Chamber volume `V_c` | ≈ 1.06 L |
| Chamber diameter `D` | ≈ 13.9 cm |
| Chamber height `L` | ≈ 70 mm |
| Working air `V_a = V_c / 2` | ≈ 0.53 L |
| Power at the pessimistic baseline | ≈ 12 W |

A 12 W sketch is not the marketing engine. It exists to test the geometry and the parametric code; the product chamber is 135.5 L for 2 hp.

## Flat geometry at `D = 135 cm`

At `D = 135 cm` the cross-section is 1.431 m². The chamber height sets the power:

| Chamber height | `V_c` | Power at 5 % | Equivalent |
|---:|---:|---:|---:|
| 70 mm | 0.100 m³ | 1.09 kW | 1.5 hp |
| 118 mm | 0.169 m³ | 1.84 kW | 2.5 hp |
| 142 mm | 0.203 m³ | 2.21 kW | 3 hp |
| 947 mm | 1.355 m³ | 14.71 kW | 20 hp |
| 1 048 mm | 1.500 m³ | 16.3 kW | ~22 hp |

The **1.5 m³ PLA envelope** is a print envelope, not a 1.5 m³ chamber. The first 2–3 hp build uses 118–142 mm of chamber height; the same diameter can later host 20 hp with a taller chamber. See [volume and weight](../../levers/volume-weight.md) and [first prototype](costs/prototype.md).

## What this check does not do

It is a static, first-order model. It ignores mechanical losses, real piston stroke, port timing and heat exchange. It is a consistency check, not a cycle simulation.

## See also

- [Sizing](sizing.md) — canonical table
- [Thermodynamics](thermodynamics.md) — efficiency and `ΔT`
- [Volume and weight](../../levers/volume-weight.md) — flat/tall geometry
- [CAD model](scad/README.md)
- [First prototype](costs/prototype.md)
