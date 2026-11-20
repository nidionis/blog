# Stratégie de production

> **Status:** canonical · **Owns:** route de production · **Up:** [Production](README.md) · **Lang:** FR · [EN](../../production/strategy.md)

L'entreprise valide d'abord le premier prototype par **impression PLA → moule sable → coulée → finition tour**, puis prépare la découpe cylindrique et l'impression de sable avant la métallurgie de série. L'objectif est de valider les formes et le procédé à coût maîtrisé. La version complète est dans la [page anglaise](../../production/strategy.md).

## Premier prototype

Le premier moteur est un **réessai non optimisé**. Le prototype est exposé à **15 000 €** (prévoir **30 000 €** sur commande pour bielle et support). Route : impression PLA (1,5 m³) → moule sable (10 m³) → coulée (creuset ~3 m³) → finition tour (~1,40 m). Détail : [premier prototype](prototype.md), [matière recyclée](../business/recycled-material.md), [équipement d'atelier](../business/atelier/equipement.md).

## Du concept à la production

1. **Passer à l'échelle** — des petits prototypes à la fabrication de meubles à grande échelle.
2. **Conversion métallurgique** — adapter la technologie aux composants de moteur.
3. **Écosystème de fabrication** — impression 3D avancée, systèmes rotatifs polaires et métallurgie.

La [découpe cylindrique](polar-slicer/polar-grid.md) ([prototype](https://github.com/nidionis/polar-slicer)) est chère à implémenter directement en métallurgie. L'impression de sable par [binder jetting](https://jlc3dp.com/fr/blog/binder-jetting-basics) est une [étape intermédiaire pertinente](binder-jetting/cost.md) vers l'aluminium.

## Coûts

En série, le tour est réparti sur des milliers de moteurs : coût ≈ **16 934 €/moteur** à 1 000/an, prix retenu **19 999 €**. Produire quelques unités par tour est la [pire option](../archive/scenarios/lathe-low-volume.md). Détail : [usinage tour](usinage-tour.md), [coûts business](../business/costs.md).

## Voir aussi

- [Premier prototype](prototype.md) · [Matière recyclée](../business/recycled-material.md)
- [Équipement d'atelier](../business/atelier/equipement.md)
- [Binder jetting](binder-jetting/README.md) · [Polar slicer](polar-slicer/README.md)
- [Version anglaise](../../production/strategy.md)
