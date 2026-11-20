# Temperature — the ΔT lever

> **Status:** canonical lever · **Owns:** hot-source temperature sensitivity · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/temperature.md)

The engine runs on a temperature difference. At fixed efficiency, power is linear in `ΔT`; the Carnot ceiling rises more slowly. The baseline keeps the working air at a mild **200 °C hot / 20 °C ambient**, which is why the chamber is large.

## Law

$$P \propto \Delta T \qquad \Delta T = T_{hot} - T_{ambient}$$

The Carnot ceiling is `1 - T_cold / T_hot` (kelvin). It is an upper bound, not a prediction: the real open cycle is far from Carnot.

| Hot source | `ΔT` | Power at constant `η` | 2 hp chamber `D` | Carnot ceiling |
|---:|---:|---:|---:|---:|
| 200 °C | 180 K | 1.00× | 55.7 cm | 38 % |
| 400 °C | 380 K | 2.11× | 43.4 cm | 56 % |
| 600 °C | 580 K | 3.22× | 37.7 cm | 66 % |
| 800 °C | 780 K | 4.33× | 34.1 cm | 73 % |

One lever at a time: efficiency stays at the pessimistic 5 %, so the table isolates the `ΔT` effect. In reality a hotter source may also raise `η`; that would shrink the engine further, but it is unproven and must not be banked.

## What it costs

- **Material** — aluminium is comfortable near 200–300 °C, not at 800 °C. Higher temperatures need steel, stainless steel or ceramics, with creep, oxidation and expansion.
- **Heat exchange** — a hotter gas is not automatically a hotter working air. The exchanger area, flow and insulation decide the real `ΔT`.
- **Losses** — radiation and exhaust losses grow with temperature; the simple linear law ignores them.
- **Combustion** — the [rocket stove](../energy/rocket-stove/README.md) can be hotter than the engine, but the engine's hot side must stay within its material limit.

**Do not confuse source and working fluid.** Straw flames can exceed 800 °C; the Manson piston and chamber cannot. The project baseline uses a modest working-air temperature on purpose.

## Pessimistic reading

Size at 200 °C. Treat 400 °C as an improved build and 600–800 °C as a laboratory or ceramic-engine study. The lever is real, but it moves the problem from thermodynamics to materials.

## See also

- [Thermodynamics](../engines/manson/thermodynamics.md) — Carnot table and efficiency tiers
- [Sizing](../engines/manson/sizing.md) — baseline volumes
- [Fuel](../engines/manson/fuel.md) — heat input for a given power
- [Insolation](insolation.md) — solar concentration can reach these temperatures
