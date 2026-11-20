# Glossaire et index des concepts

> **Status:** canonical · **Owns:** symboles, unités, constantes de base, correspondance FR/EN · **Up:** [2Cheval](README.md) · **Lang:** FR · [EN](../GLOSSARY.md)

Cette page possède les **symboles, unités et constantes de base**. Chaque terme technique renvoie à son article court ; l'article possède l'explication et les chiffres. Ne pas redéfinir un terme ici.

## Unités et symboles

| Terme | Signification |
|---|---|
| `ch`, `cv`, `hp` | cheval-vapeur / horsepower : **1 ch = 735,5 W** |
| `kW` | 1 000 W |
| `L` | litre ; 1 000 L = 1 m³ |
| `ΔT` | température de source chaude moins température ambiante, en K ou °C |
| `η` | rendement global : puissance mécanique / puissance thermique, combusteur inclus |
| `LHV` / `PCI` | pouvoir calorifique inférieur, en MJ/kg |
| `bar` | 100 000 Pa ; 10 bar ≈ 1 MPa |
| `V_c` | volume géométrique total de la chambre (les deux chambres) |
| `V_a` | volume d'air de travail ; `V_a = V_c / 2` (règle du déplaceur) |
| `D = L` | convention cylindrique des tableaux, pas une règle de fabrication |
| `f` | fréquence de cycle, en Hz |
| `r_p` | rapport de pression `p / p_atm` ; 1 = atmosphérique |
| `G` | irradiance solaire, W/m² (instantané) |
| `H` | ensoleillement, kWh/m²/jour (énergie quotidienne) |

## Constantes de base

| Paramètre | Base | Utilisé par |
|---|---:|---|
| Référence mécanique | 1 ch = 735,5 W | [carburant](engines/manson/fuel.md), [dimensionnement](engines/manson/sizing.md) |
| Rendement global `η` | **5 %** (cible 15 %, plafond labo 20 %, palier 8–12 %) | [thermodynamique](engines/manson/thermodynamics.md) |
| Température ambiante | 20 °C | [thermodynamique](engines/manson/thermodynamics.md) |
| Fréquence `f` | 2 Hz | [dimensionnement](engines/manson/sizing.md) |
| Écart de température `ΔT` | 180 K (200 °C chaud, 20 °C ambiant) | [dimensionnement](engines/manson/sizing.md) |
| Capacité thermique de l'air `Cp` | 1 005 J/(kg·K) | [dimensionnement](engines/manson/sizing.md) |
| Masse volumique de l'air `ρ` | 1,2 kg/m³ | [dimensionnement](engines/manson/sizing.md) |
| PCI de la paille | **12 MJ/kg** (sous la plage 12,5–14,5) | [paille](energy/rocket-stove/straw.md) |
| Densité de la paille, vrac / densifiée | ~100 / ~250 kg/m³ | [paille](energy/rocket-stove/straw.md) |
| Limite d'alimentation | 30 kg / 20 min = 90 kg/h | [carburant](engines/manson/fuel.md) |
| Remplissage de coulée | 66 % | [matière recyclée](business/recycled-material.md) |
| Prix / masse canette (base) | 0,03 €/canette, 14 g (configuré dans env ; jusqu'à 0,01 € et 8 g) | [matière recyclée](business/recycled-material.md) |
| Dérate de pression | 60 % du gain idéal | [levier pression](leviers/pression.md) |

## Termes

- **M Reloaded (Manson)** — nom de projet du moteur à air chaud choisi, cycle ouvert et pression atmosphérique. Hub : [engines/manson](engines/manson/README.md).
- **Rocket stove** — le combusteur de paille qui fournit la chaleur. Hub : [energy/rocket-stove](energy/rocket-stove/README.md).
- **Limite carburant** — 30 kg / 20 min à 12 MJ/kg → 300 kW thermiques → **15 kW ≈ 20,4 ch à 5 %**. À 15 %, la même alimentation laisse 45 kW. Voir [carburant](engines/manson/fuel.md).
- **Paliers de rendement** — 5 % base, 8–12 % avancé, 15 % cible, 20 % laboratoire. La promesse client est 5–15 %. Voir [levier rendement](leviers/rendement.md).
- **Paille densifiée** — paille compressée, environ 250 kg/m³ ; la paille en vrac environ 100 kg/m³. Voir [paille](energy/rocket-stove/straw.md).
- **Stirling Beta** — alternative à cycle fermé et sous pression, étudiée séparément ; non choisie. Hub : [engines/stirling](engines/stirling/README.md).
- **Alternateur linéaire** — générateur aimants/bobines de l'étude Stirling à piston libre, pas le Manson. Voir [alternateur linéaire](engines/stirling/linear-alternator.md).
- **Polar slicer** — prototype de découpe polaire/cylindrique. Hub : [production/polar-slicer](production/polar-slicer/README.md).
- **Binder jetting** — route d'impression en sable vers l'aluminium. Hub : [production/binder-jetting](production/binder-jetting/README.md).
- **Premier prototype** — premier moteur physique ; impression PLA → moule sable → coulée → finition tour. Voir [prototype](production/prototype.md).
- **Cheval cinétique** — 500 kg à 10 m/s = **25 kJ** ; référence d'énergie basse technologie. Voir [transmission](drivetrain/design.md).
- **PAC / tracteur** — références de remplacement pour la chaleur et le travail mécanique ; 15 000–35 000 € et 25 000–60 000 €. Voir [coûts](business/costs.md#4-coût-de-ce-que-le-moteur-remplace).
- **Valorisation de l'investissement** — capex et itérations transformés en valeur (outillage, moules, mesures, baisse du gaspillage). Voir [valorisation](business/valorisation-investissement.md).
- **Facteur de gaspillage / itération** — multiplicateur sur la matière parfaite (surcoulée, rebut, réessais) ; diminue avec l'apprentissage. Voir [estimation gros piston](engines/manson/costs/estimation-gros-piston.md).
- **Ensoleillement** — énergie solaire quotidienne par surface ; ne pas confondre avec l'irradiance instantanée. Voir [levier ensoleillement](leviers/ensoleillement.md).
- **Canonique** — page normative ; les autres pages y renvoient.
- **Note de source** — dérivation brute, sortie d'IA ou transcription conservée pour preuve ; non normative.
- **Exploratoire** — concept en étude, pas une décision de projet.
- **Archive / déprécié** — conservé pour l'historique ; remplacé par une page canonique.

## Index des concepts (FR ↔ EN)

L'arborescence anglaise est la source technique. L'arborescence française contient le marketing, la stratégie et des fiches courtes qui renvoient à l'article anglais pour les dérivations.

| Concept | Français | English |
|---|---|---|
| Moteur choisi | [Moteur Manson](engines/manson/README.md) | [M Reloaded](../engines/manson/README.md) |
| Dimensionnement | [Dimensionnement](engines/manson/sizing.md) | [Sizing](../engines/manson/sizing.md) |
| Thermodynamique | [Thermodynamique](engines/manson/thermodynamics.md) | [Thermodynamics](../engines/manson/thermodynamics.md) |
| État stationnaire | [État stationnaire](thermodynamic-steady.md) | [Steady state](../engines/manson/thermodynamic-steady.md) |
| Carburant | [Carburant](engines/manson/fuel.md) | [Fuel](../engines/manson/fuel.md) |
| Puissance air | [Puissance air](engines/manson/power-from-air.md) | [Power from air](../engines/manson/power-from-air.md) |
| Optimisation | [Optimisation](engines/manson/optimisation.md) | [Optimisation](../engines/manson/optimisation.md) |
| CAO | [CAO](engines/manson/scad/README.md) | [SCAD](../engines/manson/scad/README.md) |
| Premier prototype | [Premier prototype](production/prototype.md) | [Prototype](../engines/manson/costs/prototype.md) |
| Coût tour | [Usinage tour](production/usinage-tour.md) | [Lathe](../engines/manson/costs/lathe-machining.md) |
| Matière recyclée | [Matière recyclée](business/recycled-material.md) | [Recycled material](../business/recycled-material.md) |
| Rocket stove | [Rocket stove](energy/rocket-stove/README.md) | [Rocket stove](../energy/rocket-stove/README.md) |
| Paille | [Paille](energy/rocket-stove/straw.md) | [Straw](../energy/rocket-stove/straw.md) |
| Biomasse | [Biomasse](energy/rocket-stove/biomass-calorific.md) | [Biomass](../energy/rocket-stove/biomass-calorific.md) |
| Solaire | [Solaire](energy/solaire/README.md) | [Solar](../energy/solar/README.md) |
| Nucléaire | [Nucléaire](energy/nuclear/README.md) | [Nuclear](../energy/nuclear/README.md) |
| Stirling | [Stirling](engines/stirling/README.md) | [Stirling](../engines/stirling/README.md) |
| Transmission | [Transmission](drivetrain/README.md) | [Drivetrain](../drivetrain/README.md) |
| Polar slicer | [Polar slicer](production/polar-slicer/README.md) | [Polar slicer](../production/polar-slicer/README.md) |
| Binder jetting | [Binder jetting](production/binder-jetting/README.md) | [Binder jetting](../production/binder-jetting/README.md) |
| Résilience | [Résilience](business/resilience.md) | [Resilience](../business/resilience.md) |
| Leviers | [Leviers](leviers/README.md) | [Levers](../levers/README.md) |
| Pression | [Pression](leviers/pression.md) | [Pressure](../levers/pressure.md) |
| Température | [Température](leviers/temperature.md) | [Temperature](../levers/temperature.md) |
| Fréquence | [Fréquence](leviers/frequence.md) | [Frequency](../levers/frequency.md) |
| Volume et poids | [Volume et poids](leviers/volume-poids.md) | [Volume and weight](../levers/volume-weight.md) |
| Rendement | [Rendement](leviers/rendement.md) | [Efficiency](../levers/efficiency.md) |
| Ensoleillement | [Ensoleillement](leviers/ensoleillement.md) | [Insolation](../levers/insolation.md) |
| Modèle soft-coded | [Modèle](modele/README.md) | [Model](../model/README.md) |
| Stockage électrique | [Stockage électrique](electric/README.md) | [Electric storage](../electric/README.md) |
| Valorisation de l'investissement | [Valorisation](business/valorisation-investissement.md) | [Investment valorisation](../business/investment-valorisation.md) |
| Estimation gros piston | [Estimation gros piston](engines/manson/costs/estimation-gros-piston.md) | [Large-piston estimate](../engines/manson/costs/large-piston-estimate.md) |

## Langues

- L'arborescence principale est **anglaise** et possède les dérivations, les tableaux et le code.
- L'arborescence `2cheval/` est **française** : marketing, stratégie, investisseurs, plus des fiches courtes.
- Une fiche française traduit l'explication et renvoie à l'article anglais pour le tableau complet. Ne pas maintenir deux copies d'un même tableau.
- Chaque nouveau concept reçoit un article anglais et une fiche française courte ; les deux figurent dans l'index ci-dessus.

## Voir aussi

- [Carte du projet](README.md)
- [Glossaire anglais](../GLOSSARY.md)
- [Leviers](leviers/README.md)
- [Résilience](business/resilience.md)
