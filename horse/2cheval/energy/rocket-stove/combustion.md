# Combustion et libération de chaleur

> **Status:** canonical · **Owns:** bilan thermique du stove · **Up:** [Rocket stove](README.md) · **Lang:** FR · [EN](../../../energy/rocket-stove/combustion.md)

Le rocket stove est la source de chaleur. Sa puissance thermique est le débit de carburant multiplié par le PCI :

$$P_{th} = \dot m_{fuel} \cdot \mathrm{LHV}$$

Avec de la paille à **12 MJ/kg** (voir [biomasse](biomass-calorific.md)), un moteur de **2 ch** à **5 % de rendement global** demande :

- puissance mécanique : 2 × 735,5 W = **1,47 kW** ;
- puissance thermique : 1,47 / 0,05 = **29,4 kW** ;
- débit de paille : 29,4 kW × 3 600 / 12 MJ/kg = **8,8 kg/h**.

Le stove se dimensionne sur la puissance thermique, pas sur la puissance mécanique. Le tableau complet paille/charbon/pétrole est dans [carburant](../../engines/manson/fuel.md).

## Voir aussi

- [Paille](straw.md) · [Injection](injection.md)
- [Carburant](../../engines/manson/fuel.md) · [Thermodynamique](../../engines/manson/thermodynamics.md)
- [Glossaire](../../GLOSSARY.md) · [Version anglaise](../../../energy/rocket-stove/combustion.md)
