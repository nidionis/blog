# Glossaire — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** vocabulary, units, baseline assumptions · **Up:** [2Cheval](README.md)

Cette page est la source unique des termes, unités et hypothèses de référence. Les autres pages renvoient ici au lieu de redéfinir.

## Unités / Units

| Terme | Signification |
|---|---|
| `ch`, `cv`, `hp` | cheval-vapeur / horsepower : **1 ch = 735.5 W** |
| `kW` | 1 000 W |
| `L` | litre ; 1 000 L = 1 m³ |
| `ΔT` | écart de température entre la source chaude et l'ambiance, en K ou °C |
| `η` | rendement global : puissance mécanique / puissance thermique |
| `LHV` / `PCI` | pouvoir calorifique inférieur, en MJ/kg |
| `bar` | 100 000 Pa ; 10 bar ≈ 1 MPa |

## Termes / Terms

- **M Reloaded** — moteur à air chaud cycle ouvert, choisi pour sa simplicité et sa robustesse. Hub : [engines/manson](engines/manson/README.md).
- **Rocket stove** — le brûleur de paille qui fournit la chaleur. Hub : [energy/rocket-stove](energy/rocket-stove/README.md).
- **Stirling Beta** — alternative cycle fermé étudiée séparément ; non choisi. Hub : [engines/stirling](engines/stirling/README.md).
- **Paille densifiée** — paille compressée, environ 250 kg/m³ ; la paille en vrac environ 100 kg/m³.
- **Polar slicer** — prototype de slicage polaire. Hub : [production/polar-slicer](production/polar-slicer/README.md).
- **Binder jetting** — route d'impression en sable vers l'aluminium. Hub : [production/binder-jetting](production/binder-jetting/README.md).
- **Canonique** — page normative ; les autres pages y renvoient.
- **Note de source** — dérivation brute, sortie d'IA ou transcription conservée pour preuve ; non normative.
- **Exploratoire** — concept en étude, pas de décision de projet.
- **Déprécié** — conservé uniquement pour l'historique ; remplacé par une page canonique.

## Hypothèses de référence / Baseline assumptions

| Paramètre | Valeur de référence | Utilisé par |
|---|---:|---|
| Référence mécanique | 1 ch = 735.5 W | [fuel](engines/manson/fuel.md), [sizing](engines/manson/sizing.md) |
| Rendement global `η` | 5 % (15 % optimisé, 20 % en laboratoire) | [thermodynamics](engines/manson/thermodynamics.md) |
| Température ambiante | 20 °C | [thermodynamics](engines/manson/thermodynamics.md) |
| Fréquence de cycle `f` | 2 Hz | [sizing](engines/manson/sizing.md) |
| Écart de température `ΔT` | **180 K** — cycle de Carnot à 200°C (`T_hot = 200°C`, `T_cold = 20°C`) | [sizing](engines/manson/sizing.md) |
| Capacité thermique de l'air `Cp` | 1 005 J/(kg·K) | [sizing](engines/manson/sizing.md) |
| Masse volumique de l'air `ρ` | 1.2 kg/m³ | [sizing](engines/manson/sizing.md) |
| LHV de la paille | 15 MJ/kg | [straw](energy/rocket-stove/straw.md) |
| Densité de la paille, en vrac | ~100 kg/m³ | [straw](energy/rocket-stove/straw.md) |
| Densité de la paille, densifiée | ~250 kg/m³ | [straw](energy/rocket-stove/straw.md) |

## Structure linguistique / Language structure

- Le projet principal (`engines/`, `energy/`, `business/`, ...) est en anglais.
- La sous-arborescence `2cheval/` est l'arborescence française parallèle : marketing, stratégie et investisors, avec redirections vers les articles techniques anglais.
- Voir [état stationnaire](engines/manson/thermodynamic-steady.md) pour la duplication courte.

## Dictionnaire conceptuel / Conceptual dictionary

Le dictionnaire technique/conceptuel (dictionnaire de vocabulaire) : chaque concept a son article français (sous-projet 2Cheval) et son article technique anglais (projet principal).

| Concept | Article français (2Cheval) | Article anglais technique |
|---|---|---|
| M Reloaded (moteur choisi) | [engines/manson/README.md](engines/manson/README.md) | [engines/manson/README.md](../engines/manson/README.md) |
| Dimensionnement du moteur | [engines/manson/sizing.md](engines/manson/sizing.md) | [engines/manson/sizing.md](../engines/manson/sizing.md) |
| Thermodynamique du moteur | [engines/manson/thermodynamics.md](engines/manson/thermodynamics.md) | [engines/manson/thermodynamics.md](../engines/manson/thermodynamics.md) |
| État stationnaire thermodynamique | [engines/manson/thermodynamic-steady.md](engines/manson/thermodynamic-steady.md) | [engines/manson/thermodynamic-steady.md](../engines/manson/thermodynamic-steady.md) |
| Consommation de carburant | [engines/manson/fuel.md](engines/manson/fuel.md) | [engines/manson/fuel.md](../engines/manson/fuel.md) |
| Optimisation du moteur | [engines/manson/optimisation.md](engines/manson/optimisation.md) | [engines/manson/optimisation.md](../engines/manson/optimisation.md) |
| Modèle CAO du piston | [engines/manson/scad/README.md](engines/manson/scad/README.md) | [engines/manson/scad/README.md](../engines/manson/scad/README.md) |
| Coûts matière du Manson | [engines/manson/costs/README.md](engines/manson/costs/README.md) | [engines/manson/costs/README.md](../engines/manson/costs/README.md) |
| Alternative étudiée (Stirling Beta) | [engines/stirling/README.md](engines/stirling/README.md) | [engines/stirling/README.md](../engines/stirling/README.md) |
| Rocket stove | [energy/rocket-stove/README.md](energy/rocket-stove/README.md) | [energy/rocket-stove/README.md](../energy/rocket-stove/README.md) |
| Propriétés de la paille | [energy/rocket-stove/straw.md](energy/rocket-stove/straw.md) | [energy/rocket-stove/straw.md](../energy/rocket-stove/straw.md) |
| Variante nucléaire | [energy/nuclear/README.md](energy/nuclear/README.md) | [energy/nuclear/README.md](../energy/nuclear/README.md) |
| Business model | [business/business-model.md](business/business-model.md) | [business/business-model.md](../business/business-model.md) |
| Cas client de référence | [business/customers.md](business/customers.md) | [business/customers.md](../business/customers.md) |
| Transmission | [drivetrain/README.md](drivetrain/README.md) | [drivetrain/README.md](../drivetrain/README.md) |
| Production et impression 3D | [production/README.md](production/README.md) | [production/README.md](../production/README.md) |
| Coûts business | [business/costs.md](business/costs.md) | [business/costs.md](../business/costs.md) |
| Matière recyclée | [business/recycled-material.md](business/recycled-material.md) | [business/recycled-material.md](../business/recycled-material.md) |

## Conventions

- Utiliser des liens Markdown relatifs, pas de `[[liens wiki]]`.
- Relier la première mention d'un concept ; ne pas copier sa table.

## Voir aussi / See also

- [Carte du projet](README.md)
- [M Reloaded](engines/manson/README.md)
- [Coûts](business/costs.md)
