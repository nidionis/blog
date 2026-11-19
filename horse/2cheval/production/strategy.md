# 2Cheval — Stratégie de production — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** production route · **Up:** [Production](README.md)

L'entreprise valide d'abord le premier prototype par **impression PLA → moule sable → coulée → finition tour**, puis prépare la découpe cylindrique et l'impression de sable avant la métallurgie de série. L'objectif est de valider les formes et le procédé à coût maîtrisé.

## Premier prototype

Le premier moteur n'est pas usiné dans la masse : impression PLA (1,5 m³) → moule sable (10 m³) → coulée (creuset ~3 m³, four solaire ou fonderie) → finition tour (~1,40 m). Coût pessimiste : ≈ **€52 000–196 000** en sous-traitance, ou ≈ **€122 000–426 000** avec four solaire et creuset. Détail : [Premier prototype — PLA, sable, coulée, tour](prototype.md).

## Du concept à la production

L'entreprise prépare la [technologie de découpe cylindrique](polar-slicer/polar-grid.md) ([prototype](https://github.com/nidionis/polar-slicer)). Cette technique est chère à implémenter directement en métallurgie.

L'impression de sable par [binder jetting](https://jlc3dp.com/fr/blog/binder-jetting-basics) est [une étape intermédiaire pertinente](binder-jetting/cost.md) vers l'aluminium.

## Notre vision

1. **Passer à l'échelle** — passer des petits prototypes à la fabrication de meubles à grande échelle.
2. **Conversion métallurgique** — adapter la technologie aux composants de moteur.
3. **Un écosystème de fabrication** — combiner impression 3D avancée, systèmes rotatifs polaires et métallurgie.

## Coûts de production (pessimistes)

Le **premier prototype** coûte ≈ **€52 000–196 000** en sous-traitance, ou ≈ **€122 000–426 000** avec four solaire et creuset de 3 m³ : voir [prototype](prototype.md). En série, le tour est réparti sur des milliers de moteurs : le coût tombe à ≈ **€16 650/moteur** et le prix de vente retenu est **€19 999**. Détail et marge : [Usinage tour — coût de production et prix de revente](usinage-tour.md) et [coûts business](../business/costs.md).

## Voir aussi
- [Dictionnaire / Glossary](../GLOSSARY.md)
- [Premier prototype — PLA, sable, coulée, tour](prototype.md)
- [Coût de production : usine tour et cylindres](machining-cost.md)
- [Usinage tour — coût de production et prix de revente](usinage-tour.md)

- [Polar slicer](polar-slicer/README.md)
- [Binder jetting](binder-jetting/README.md)
- [Coûts business](../business/costs.md)
