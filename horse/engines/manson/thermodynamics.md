# Manson thermodynamics

> **Status:** canonical · **Owns:** efficiency, Carnot limit and ΔT · **Up:** [M Reloaded](README.md)

The Manson engine converts heat into work by air expansion. Theoretical efficiency is bounded by Carnot; realistic tiers run from 5 % to 20 %.

## Carnot efficiency

The **theoretical efficiency** depends mainly on the temperature difference (ΔT). Combustion volume does not directly affect efficiency.

With an ambient at **20 °C (293 K)**:

| Hot temperature | ΔT | Carnot efficiency |
|---:|---:|---:|
| 200 °C | 180 °C | 38 % |
| 400 °C | 380 °C | 56 % |
| 600 °C | 580 °C | 66 % |
| 800 °C | 780 °C | 73 % |
| 1 000 °C | 980 °C | 77 % |

This is an upper bound. The real open cycle is far from Carnot.

## Real efficiencies

We use four overall performance tiers (including the combustor):

- **5 %** : initial target, artisanal build.
- **8 – 12 %** : advanced design, high-performance materials but wear.
- **15 %** : new, optimal conditions.
- **20 %** : new, laboratory superheat.

## Required ΔT per cycle

From mechanical power `P_m`, frequency `f` and efficiency `η`:

$$W_{cycle} = \frac{P_m}{f}$$

$$Q_{in} = \frac{W_{cycle}}{\eta}$$

$$m_{air} = \rho \cdot V_{cycle}$$

$$\Delta T = \frac{Q_{in}}{m_{air} \cdot C_p}$$

Example with the baseline assumptions (2 ch, 2 Hz, 67.76 L/cycle, η = 5 %, ρ = 1.2 kg/m³, Cp = 1 005 J/(kg·K)) :

- `W_cycle` ≈ 735 J
- `Q_in` ≈ 14.7 kJ
- `m_air` ≈ 0.0813 kg
- **ΔT ≈ 180 K**

This matches the sizing model: see [sizing](sizing.md). The old note claiming ~1,785 K used work instead of heat and treated m³ as kg; it is archived.

## See also

- [Sizing](sizing.md)
- [Fuel](fuel.md)
- [Rocket stove combustion](../../energy/rocket-stove/combustion.md)
- [Glossary](../../GLOSSARY.md)
