# Moteur Manson — M Reloaded

> **Status:** canonical hub · **Owns:** choix du moteur · **Up:** [Moteurs](../README.md) · **Lang:** FR · [EN](../../../engines/manson/README.md)

Le [Moteur Manson](https://moteurstirling.com/mace/manson/principes.php) est choisi pour sa simplicité de construction et sa robustesse : **cycle ouvert, pression atmosphérique, basse fréquence**.

## Principe

Le [rendement](thermodynamics.md) dépend de l'écart de température entre la source chaude et l'ambiance. Le volume du foyer influence la [puissance](fuel.md) disponible, mais pas directement l'efficacité thermodynamique. Le projet vise **5 % en base**, **15 % avec optimisation**, et garde **20 %** comme plafond de laboratoire. Aucun de ces gains n'est requis pour la promesse de 2 ch.

## En bref

- **Produit** : 2 ch ≈ 1,47 kW · **laboratoire** : 6 ch ≈ 4,41 kW · **extrême** : 20 ch ≈ 14,71 kW.
- Volumes et dimensions : [dimensionnement](sizing.md) — 2 ch = 135,5 L / 55,7 cm ; 6 ch = 406,6 L / 80,3 cm.
- Rendement, Carnot et `ΔT` : [thermodynamique](thermodynamics.md).
- Consommation et limite 30 kg / 20 min : [carburant](fuel.md).
- Puissance à partir du volume d'air : [puissance air](power-from-air.md).
- Distribution et porosité : [optimisation](optimisation.md).
- Coûts matière : [coûts](costs/README.md).
- Modèle CAO paramétrique : [CAO](scad/README.md).

La **limite de 30 kg / 20 min** plafonne le moteur à 15 kW ≈ 20,4 ch **à 5 %**. À 15 %, la même alimentation laisse 45 kW ; c'est un levier, pas une promesse. Voir [leviers](../../leviers/README.md) et [résilience](../../business/resilience.md).

## Alternative étudiée

Le [Stirling Beta](../stirling/README.md) est documenté séparément comme alternative non choisie : cycle fermé, gaz sous pression. Ne pas mélanger ses hypothèses avec celles du Manson.

## Voir aussi

- [Rocket stove](../../energy/rocket-stove/README.md)
- [État stationnaire](../../thermodynamic-steady.md)
- [Glossaire](../../GLOSSARY.md)
- [Carte du projet](../../README.md)
- [Version anglaise](../../../engines/manson/README.md)
