# Combustion et libération de chaleur — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** stove heat balance · **Up:** [Rocket stove](README.md)

Le rocket stove est la source de chaleur. Sa puissance thermique est le débit de carburant multiplié par le PCI.

$$P_{th} = \dot m_{fuel} \cdot \mathrm{LHV}$$

Avec de la paille à 15 MJ/kg, un moteur de **2 ch** à **5 % de rendement global** demande :

- puissance mécanique : 2 × 735.5 W = **1.47 kW**
- puissance thermique : 1.47 / 0.05 = **29.4 kW**
- débit de paille : 29.4 kW × 3600 / 15 MJ/kg = **7.1 kg/h**

Le tableau complet pour paille, charbon et pétrole est dans [consommation](../../engines/manson/fuel.md). Le stove se dimensionne sur la puissance thermique, pas la puissance mécanique.

## Voir aussi
- [Dictionnaire / Glossary](../../GLOSSARY.md)

- [Propriétés de la paille](straw.md)
- [Injection](injection.md)
- [Consommation](../../engines/manson/fuel.md)
- [Thermodynamique](../../engines/manson/thermodynamics.md)
