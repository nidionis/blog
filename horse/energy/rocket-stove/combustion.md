# Combustion and heat release

> **Status:** canonical · **Owns:** stove heat balance · **Up:** [Rocket stove](README.md)

The rocket stove is the heat source. Its thermal power is the fuel flow multiplied by the LHV.

$$P_{th} = \dot m_{fuel} \cdot \mathrm{LHV}$$

With straw at 15 MJ/kg, a **2 ch** engine at **5 % overall efficiency** needs:

- mechanical output: 2 × 735.5 W = **1.47 kW**
- thermal input: 1.47 / 0.05 = **29.4 kW**
- straw flow: 29.4 kW × 3600 / 15 MJ/kg = **7.1 kg/h**

The full table for straw, charcoal and oil is in [fuel consumption](../../engines/manson/fuel.md). The stove must be sized for the thermal power, not the mechanical output; the engine's volume and frequency only determine how that heat is converted into work (see [sizing](../../engines/manson/sizing.md)).

## See also

- [Straw properties](straw.md)
- [Injection](injection.md)
- [Fuel consumption](../../engines/manson/fuel.md)
- [Thermodynamics](../../engines/manson/thermodynamics.md)
