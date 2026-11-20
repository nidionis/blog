# Ensoleillement — le levier solaire

> **Status:** exploratory · **Owns:** chaleur solaire et sensibilité à l'ensoleillement · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/insolation.md)

Le moteur ne se soucie pas de l'origine de la chaleur. La paille est la référence parce qu'elle se stocke et qu'elle est dense, mais le soleil peut la remplacer quand il est disponible. Le levier n'est pas le moteur : c'est la surface du capteur et le stockage.

## Définitions

- **Irradiance `G`** — puissance instantanée par surface, W/m². Ciel clair à midi : environ **1 000 W/m²** ; moyenne pessimiste : **250–500 W/m²**.
- **Ensoleillement `H`** — énergie par surface et par jour, kWh/m²/jour. Site tempéré ensoleillé : **2–6 kWh/m²/jour**, l'hiver au bas de la plage.
- **Rendement du capteur `η_solaire`** — chaleur utile divisée par l'énergie solaire reçue. **50 %** en pessimiste pour un capteur thermique simple ; la concentration fait mieux mais demande du suivi.

$$P_{th} = G \cdot A \cdot \eta_{solaire} \qquad A = \frac{P_{th}}{G \cdot \eta_{solaire}}$$

## Surface instantanée pour 2 ch

| Rendement moteur | Besoin thermique | À 250 W/m² utile | À 400 W/m² | À 600 W/m² |
|---:|---:|---:|---:|---:|
| 5 % (base) | 29,4 kW | 118 m² | 74 m² | 49 m² |
| 15 % (cible) | 9,8 kW | 39 m² | 25 m² | 16 m² |

Ce sont des surfaces **à midi**. Un moteur de 2 ch à 5 % demande un capteur de la taille d'un petit toit de maison ; à 15 %, d'un grand toit de garage.

## Surface quotidienne et stockage

| Usage | Énergie thermique | À 2 kWh/m²/jour | À 4 kWh/m²/jour |
|---|---:|---:|---:|
| 10 min à 2 ch, 5 % | 4,9 kWh | 2,5 m² | 1,2 m² |
| 10 min à 2 ch, 15 % | 1,6 kWh | 0,8 m² | 0,4 m² |
| 24 h à 2 ch, 5 % | 706 kWh | 353 m² | 176 m² |
| 24 h à 2 ch, 15 % | 235 kWh | 118 m² | 59 m² |

Une courte démonstration quotidienne est facile : quelques mètres carrés suffisent. Le fonctionnement continu est un autre projet : il faut des centaines de mètres carrés ou un très grand stock thermique. À 5 %, stocker 706 kWh dans de l'eau sur 50 K demande environ **12 m³** ; à 15 %, environ **4 m³**. C'est pourquoi la conception de référence garde la paille en base et traite le solaire comme une entrée hybride.

## Ce que cela coûte

- **Surface** — le capteur est la partie chère, pas le moteur.
- **Intermittence** — nuit, nuages, hiver. Une batterie remplace mal la chaleur ; un stove à biomasse est un secours bon marché.
- **Température** — un capteur plan donne 60–100 °C, pas 200–800 °C. La concentration est nécessaire pour le levier [température](temperature.md).
- **Maintenance** — miroirs, suivi, poussière, grêle.

## Pourquoi c'est un levier de résilience

Soleil et paille sont complémentaires : soleil en été, paille stockée en hiver ; solaire pour une courte démonstration, paille pour la puissance continue. Le [four solaire](../production/prototype.md) figure déjà dans la route du prototype pour la coulée : le projet a donc une raison de développer la concentration solaire indépendamment du moteur.

## Voir aussi

- [Chaleur solaire](../energy/solaire/README.md) — la variante de source
- [Température](temperature.md) — pourquoi la concentration est nécessaire
- [Résilience](../business/resilience.md) — stratégie hybride
- [Version anglaise (dérivation)](../../levers/insolation.md)
