# Manson thermodynamics

> **Status:** canonical · **Owns:** efficiency, Carnot ceiling and `ΔT` · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../2cheval/engines/manson/thermodynamics.md)

The Manson converts heat into work by air expansion. Theoretical efficiency is bounded by Carnot; realistic tiers run from 5 % to 20 %. The project **sizes at 5 %** and treats the rest as upside.

## Carnot ceiling

The theoretical efficiency depends mainly on the temperature difference. Combustion volume does not directly affect efficiency.

With an ambient at **20 °C (293 K)**:

| Hot temperature | `ΔT` | Carnot ceiling |
|---:|---:|---:|
| 200 °C | 180 K | 38 % |
| 400 °C | 380 K | 56 % |
| 600 °C | 580 K | 66 % |
| 800 °C | 780 K | 73 % |
| 1 000 °C | 980 K | 77 % |

This is an upper bound. The real open cycle is far from Carnot, and the engine materials may not survive the high rows. See the [temperature lever](../../levers/temperature.md).

## Real efficiency tiers

Overall efficiency includes the combustor:

- **5 %** — initial target, artisanal build; **sizing and price baseline**.
- **8–12 %** — advanced design, better materials, more wear.
- **15 %** — new, optimal conditions; **customer promise upper bound**.
- **20 %** — new, laboratory superheat; not a sales number.

## `ΔT` required per cycle

From mechanical power `P_m`, frequency `f` and efficiency `η`:

$$W_{cycle} = \frac{P_m}{f} \qquad Q_{in} = \frac{W_{cycle}}{\eta} \qquad m_{air} = \rho V_a \qquad \Delta T = \frac{Q_{in}}{m_{air} C_p}$$

With the baseline (2 ch, 2 Hz, 67.76 L air, η = 5 %, ρ = 1.2 kg/m³, Cp = 1 005 J/(kg·K)):

- `W_cycle` ≈ 735 J
- `Q_in` ≈ 14.7 kJ
- `m_air` ≈ 0.0813 kg
- **`ΔT` ≈ 180 K**

This matches the [sizing](sizing.md) model. The old note claiming ~1,785 K used work instead of heat and treated m³ as kg; it is [archived](../../archive/deprecated/temperature.md).

## What the model does not say

- A larger combustion volume does **not** raise efficiency; it raises available power.
- A higher `ΔT` does not automatically raise `η`; it raises the Carnot ceiling and stresses materials.
- Efficiency improvements are not independent: pressure, speed and temperature all stress seals and bearings.

## See also

- [Sizing](sizing.md) — volume for a given power
- [Fuel](fuel.md) — thermal input and feed limit
- [Efficiency lever](../../levers/efficiency.md) — what each tier buys
- [Rocket stove combustion](../../energy/rocket-stove/combustion.md)
- [Glossary](../../GLOSSARY.md)
