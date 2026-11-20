# Variante solaire — chaleur solaire

> **Status:** exploratory · **Owns:** source de chaleur solaire · **Up:** [Énergie](../README.md) · **Lang:** FR · [EN](../../../energy/solar/README.md)

La chaleur solaire peut remplacer la paille quand le soleil est disponible. Elle ne change pas le moteur : elle change la source de chaleur et ajoute un capteur et un stock. La conception de référence garde la paille en base, car elle se stocke et elle est dense.

## Deux routes de température

| Route | Température typique | Usage |
|---|---:|---|
| Capteur plan ou à tubes sous vide | 60–100 °C | préchauffage, chaleur sanitaire, `ΔT` très faible |
| Capteur à concentration (miroirs, Fresnel) | 200–800 °C | côté chaud du moteur, `ΔT` élevé |
| [Four solaire](../../production/prototype.md) | > 1 000 °C | coulée, matériaux, pas la chaleur continue du moteur |

Le côté chaud du moteur est limité par ses matériaux, pas par le soleil. Un capteur plan n'atteint pas un `ΔT` utile pour un moteur compact ; la concentration est nécessaire pour le [levier température](../../leviers/temperature.md).

## Dimensionnement

$$P_{th} = G \cdot A \cdot \eta_{solaire}$$

À **250 W/m² utile** en pessimiste (500 W/m² d'irradiance × 50 % de capteur), un moteur de 2 ch à 5 % demande **118 m²** à midi. À 15 %, il demande **39 m²**. Une démonstration de 10 min par jour ne demande que quelques mètres carrés ; 24 h en continu demandent des centaines de mètres carrés. Le tableau complet est dans [ensoleillement](../../leviers/ensoleillement.md).

## Stockage et fonctionnement hybride

- **Courte durée** — quelques mètres carrés de capteur et un petit stock d'eau chaude suffisent à une démonstration.
- **Continu** — des centaines de mètres carrés, ou un grand stock thermique, ou un secours biomasse. À 5 %, 24 h à 2 ch font environ 706 kWh thermiques, soit à peu près 12 m³ d'eau sur 50 K.
- **Hybride** — le solaire préchauffe l'air du stove ou l'air de travail ; la paille complète la nuit. Le moteur n'a pas à choisir.

## Limites

Le solaire est intermittent, diffus en hiver et gourmand en surface. C'est une entrée de résilience, pas un remplacement de carburant pour tous les sites. Le [four solaire](../../production/prototype.md) déjà présent dans la route du prototype est un outil séparé, à haute température.

## Voir aussi

- [Ensoleillement](../../leviers/ensoleillement.md) — surfaces et stockage
- [Température](../../leviers/temperature.md) — pourquoi la concentration compte
- [Résilience](../../business/resilience.md) — stratégie de sources hybrides
- [Hub énergie](../README.md)
- [Version anglaise (dérivation)](../../../energy/solar/README.md)
