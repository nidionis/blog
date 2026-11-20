# Combustion and heat release

> **Status:** canonical · **Owns:** stove heat balance · **Up:** [Rocket stove](README.md) · **Lang:** EN · [FR](../../2cheval/energy/rocket-stove/combustion.md)

The rocket stove is the heat source. Its thermal power is the fuel flow multiplied by the LHV.

$$P_{th} = \dot m_{fuel} \cdot \mathrm{LHV}$$

With straw at **12 MJ/kg** ([biomass](biomass-calorific.md)), a **2 hp** engine at **5 % overall efficiency** needs:

- mechanical output: 2 × 735.5 W = **1.47 kW**
- thermal input: 1.47 / 0.05 = **29.4 kW**
- straw flow: 29.4 kW × 3600 / 12 MJ/kg = **8.8 kg/h**

At 15 % the same 2 hp needs only **9.8 kW thermal** and **2.9 kg/h**. The full table for straw, charcoal and oil is in [fuel](../../engines/manson/fuel.md).

The stove is sized for the **thermal power**, not the mechanical output. The engine volume and frequency determine how that heat is converted into work; see [sizing](../../engines/manson/sizing.md) and [efficiency](../../levers/efficiency.md).

## See also

- [Straw properties](straw.md)
- [Injection](injection.md)
- [Fuel consumption](../../engines/manson/fuel.md)
- [Thermodynamics](../../engines/manson/thermodynamics.md)
- [Resilience](../../business/resilience.md)
