# Efficiency — the multiplier lever

> **Status:** canonical lever · **Owns:** overall-efficiency sensitivity · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/rendement.md)

Overall efficiency `η` is mechanical output divided by thermal input, **including the combustor**. It is the only lever that improves power, fuel consumption and engine size at the same time, which also makes it the hardest to earn.

## Law

$$P \propto \eta \quad\text{at constant fuel} \qquad \dot m_{fuel} \propto \frac{1}{\eta} \quad\text{at constant power}$$

| Overall `η` | 2 hp chamber `D` | 2 hp straw | Mechanical cap at 30 kg / 20 min |
|---:|---:|---:|---:|
| 5 % (baseline) | 55.7 cm | 8.83 kg/h | 15 kW ≈ 20.4 hp |
| 10 % | 44.2 cm | 4.41 kg/h | 30 kW ≈ 40.8 hp |
| 15 % (target) | 38.6 cm | 2.94 kg/h | 45 kW ≈ 61.2 hp |
| 20 % (lab ceiling) | 35.1 cm | 2.21 kg/h | 60 kW ≈ 81.6 hp |

The customer promise uses **5–15 %**; 20 % is a laboratory ceiling, not a sales number. The intermediate 8–12 % tier is an advanced build with better materials and more wear.

## Where efficiency comes from

- **Combustion** — the [rocket stove](../energy/rocket-stove/README.md) must burn the straw completely, with low excess air and low unburned losses.
- **Heat exchange** — the hot gas must actually heat the working air; a large `ΔT` on paper is not a large `ΔT` in the chamber.
- **Port timing and filling** — see [optimisation](../engines/manson/optimisation.md). A chamber that does not fill loses power before thermodynamics matters.
- **Sealing and friction** — leakage and piston friction are direct losses. They get worse with pressure and speed.
- **Insulation** — every kelvin lost before the working air expands is efficiency lost.

## Pessimistic reading

Size and price at **5 %**. Use 15 % only after a measured test, and never multiply the two best cases together. Efficiency improvements are multiplicative in the model but not independent in hardware: higher temperature, pressure and frequency all stress the same seals and materials.

## Why it is a resilience lever

If straw is expensive or the feed limit is the bottleneck, efficiency buys fuel headroom. If the engine is too heavy, efficiency shrinks the chamber. If a build cannot reach 15 %, the 5 % baseline still delivers the 2 hp promise with a larger chamber. The pessimistic floor is the resilience.

## See also

- [Thermodynamics](../engines/manson/thermodynamics.md) — Carnot ceiling and tiers
- [Fuel](../engines/manson/fuel.md) — consumption table and feed limit
- [Sizing](../engines/manson/sizing.md) — volume for a given power
- [Optimisation](../engines/manson/optimisation.md) — practical loss paths
