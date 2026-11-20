# Rocket stove — la source de chaleur

> **Status:** canonical hub · **Owns:** source de chaleur · **Up:** [Énergie](../README.md) · **Lang:** FR · [EN](../../../energy/rocket-stove/README.md)

Le rocket stove brûle de la paille et fournit le gaz chaud au [moteur Manson](../../engines/manson/README.md). C'est une **source de chaleur**, pas le moteur.

- [Propriétés de la paille](straw.md) — PCI, densités vrac et densifiée.
- [Capacité calorifique de la biomasse](biomass-calorific.md) — tableau PCI/PCS et base 12 MJ/kg.
- [Injection](injection.md) — comment la paille est introduite.
- [Combustion](combustion.md) — libération de chaleur et puissance thermique requise.

À 5 %, un moteur de 2 ch a besoin d'environ **29,4 kW thermiques**. Le débit de paille correspondant est dans [carburant](../../engines/manson/fuel.md). La limite d'alimentation de **30 kg en 20 min** plafonne la puissance mécanique à **15 kW ≈ 20,4 ch à 5 %** ; à 15 %, elle laisse 45 kW. Voir [dimensionnement](../../engines/manson/sizing.md#limite-carburant) et [levier rendement](../../leviers/rendement.md).

Le stove peut brûler bois, granulés, miscanthus ou charbon de bois : le moteur ne voit que la chaleur. C'est la base de la [résilience des sources](../../business/resilience.md).

## Voir aussi

- [Moteur Manson](../../engines/manson/README.md)
- [Thermodynamique](../../engines/manson/thermodynamics.md)
- [Chaleur solaire](../solaire/README.md) · [Variante nucléaire](../nuclear/README.md)
- [Glossaire](../../GLOSSARY.md) · [Version anglaise](../../../energy/rocket-stove/README.md)
