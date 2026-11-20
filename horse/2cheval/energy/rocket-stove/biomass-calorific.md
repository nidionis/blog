# Capacité calorifique de la biomasse

> **Status:** reference · **Owns:** valeurs PCI/PCS de la biomasse · **Up:** [Rocket stove](README.md) · **Lang:** FR · [EN](../../../energy/rocket-stove/biomass-calorific.md)

Les valeurs calorifiques varient selon le combustible et l'humidité. Le tableau complet et les sources sont dans la [page anglaise](../../../energy/rocket-stove/biomass-calorific.md). Cette fiche fixe les valeurs utilisées pour le dimensionnement.

## Valeurs de référence

| Biomasse | PCI (MJ/kg) |
|---|---:|
| Bois (feuillu) | 14,5–16 |
| Bois (résineux) | 15–16,5 |
| Céréales (paille) | **12,5–14,5** |
| Miscanthus | 13,5–15 |
| Granulés de bois (pellets) | 16,5–18 |
| Charbon de bois | ~30 |
| Pétrole | ~43 |

## Humidité

L'humidité est le facteur le plus critique :

- **Bois sec** (< 20 % d'humidité) : PCI ≈ 4,0–4,4 kWh/kg.
- **Bois frais** (~50 % d'humidité) : PCI ≈ 1,5–2,0 kWh/kg.
- Chaque 10 % d'humidité supplémentaire réduit le PCI d'environ 0,4–0,5 kWh/kg, car une partie de la chaleur évapore l'eau.

## Hypothèse du projet

Le dimensionnement utilise **12 MJ/kg**, volontairement sous la plage de la paille (12,5–14,5 MJ/kg). L'ancienne valeur de 15 MJ/kg était optimiste ; tous les débits sont recalculés à 12 MJ/kg.

À 5 % de rendement, 12 MJ/kg et 30 kg / 20 min, la puissance thermique est de 300 kW et la limite mécanique de **15 kW ≈ 20,4 ch**. À 15 %, la même alimentation laisse 45 kW. Voir [carburant](../../engines/manson/fuel.md), [dimensionnement](../../engines/manson/sizing.md#limite-carburant) et [levier rendement](../../leviers/rendement.md).

## Voir aussi

- [Paille](straw.md) · [Combustion](combustion.md)
- [Carburant](../../engines/manson/fuel.md) · [Rocket stove](README.md)
- [Version anglaise](../../../energy/rocket-stove/biomass-calorific.md)
