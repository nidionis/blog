# Combustion and heat release / Combustion et libération de chaleur

> **Status:** canonical · **Owns:** stove heat balance · **Up:** [Rocket stove](README.md)

**FR** — Le rocket stove est la source de chaleur. Sa puissance thermique est le débit de carburant multiplié par le PCI.  
**EN** — The rocket stove is the heat source. Its thermal power is the fuel flow multiplied by the LHV.

$$P_{th} = \dot m_{fuel} \cdot \mathrm{LHV}$$

With straw at 15 MJ/kg, a **2 ch** engine at **5 % overall efficiency** needs / Avec de la paille à 15 MJ/kg, un moteur de **2 ch** à **5 % de rendement global** demande :

- mechanical output / puissance mécanique : 2 × 735.5 W = **1.47 kW**
- thermal input / puissance thermique : 1.47 / 0.05 = **29.4 kW**
- straw flow / débit de paille : 29.4 kW × 3600 / 15 MJ/kg = **7.1 kg/h**

The full table for straw, charcoal and oil is in [fuel consumption](../../engines/manson/fuel.md). The stove must be sized for the thermal power, not the mechanical output; the engine's volume and frequency only determine how that heat is converted into work (see [sizing](../../engines/manson/sizing.md)).  
Le tableau complet pour paille, charbon et pétrole est dans [consommation](../../engines/manson/fuel.md). Le stove se dimensionne sur la puissance thermique, pas la puissance mécanique.

## See also / Voir aussi

- [Straw properties / Propriétés](straw.md)
- [Injection / Injection](injection.md)
- [Fuel consumption / Consommation](../../engines/manson/fuel.md)
- [Thermodynamics / Thermodynamique](../../engines/manson/thermodynamics.md)
