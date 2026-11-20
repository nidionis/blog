# Consommation de carburant

> **Status:** canonical · **Owns:** consommation par puissance mécanique · **Up:** [M Manson](README.md) · **Lang:** FR · [EN](../../../engines/manson/fuel.md)

Cette page donne le débit de carburant à **5 % de rendement**. Le tableau complet, paille/charbon/pétrole et les autres rendements sont dans la [page anglaise](../../../engines/manson/fuel.md). Les propriétés de la paille sont dans [paille](../../energy/rocket-stove/straw.md) ; le tableau biomasse dans [capacité calorifique](../../energy/rocket-stove/biomass-calorific.md).

## Hypothèses

- **1 ch = 735,5 W**, rendement global **5 %**, fonctionnement continu à pleine charge.
- PCI : paille **12 MJ/kg** (valeur basse), charbon 30 MJ/kg, pétrole 43 MJ/kg.
- Densités : paille 100 kg/m³ (vrac) ou 250 kg/m³ (densifiée).

## Besoin en paille

<!-- calc:fuel:fr -->
| Puissance | Mécanique | Thermique | Paille kg/h | Paille L/h (vrac) | Paille L/h (densifiée) |
|---:|---:|---:|---:|---:|---:|
| 1 ch | 0,74 kW | 14,7 kW | 4,41 | 44,1 | 17,7 |
| 2 ch | 1,47 kW | 29,4 kW | 8,83 | 88,3 | 35,3 |
| 6 ch | 4,41 kW | 88,3 kW | 26,48 | 264,8 | 105,9 |
| 20 ch | 14,71 kW | 294,2 kW | 88,26 | 882,6 | 353,0 |
<!-- /calc:fuel:fr -->

Pour un essai de 10 min à 2 ch : 8,83 kg/h × 1/6 h ≈ **1,47 kg de paille**.

## Limite d'alimentation : 30 kg en 20 min

La limite annoncée est **30 kg pour 20 min**, soit **90 kg/h**. À 12 MJ/kg :

$$P_{th,max} = 90 \times \frac{12\,000}{3\,600} = 300\ \text{kW} \qquad P_{m,max} = 0,05 \times 300 = 15\ \text{kW} \approx 20,4\ \text{ch}$$

C'est un plafond **à 5 %**. La ligne 20 ch consomme 29,4 kg par 20 min ; la ligne 2 ch en consomme 2,94 kg. À 15 %, la même alimentation laisse 45 kW. La puissance du moteur est le minimum de la limite de volume d'air et de cette limite carburant ; voir [dimensionnement](sizing.md#limite-carburant) et [levier rendement](../../leviers/rendement.md).

## Voir aussi

- [Paille](../../energy/rocket-stove/straw.md) · [Biomasse](../../energy/rocket-stove/biomass-calorific.md)
- [Thermodynamique](thermodynamics.md) · [Dimensionnement](sizing.md)
- [Glossaire](../../GLOSSARY.md) · [Version anglaise](../../../engines/manson/fuel.md)
