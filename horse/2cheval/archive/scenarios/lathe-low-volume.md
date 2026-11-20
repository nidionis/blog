# Scénario d'échec — faible volume tour et vente de machine

> **Status:** archived scenario · **Owns:** risque d'amortissement tour à faible volume · **Up:** [Archive](../README.md)

Cette page archive la **pire option** de production : utiliser un tour de 2 m comme unité de production pour seulement quelques moteurs par an. Elle est conservée comme **scénario d'échec** et déclencheur pour envisager la vente ou la location de la machine de production.

## Pourquoi c'est la pire option

- **Tour 2 m** : achat ≈ **600 000 €**, durée de vie 3 ans → amortissement **200 000 €/an**.
- Le modèle de coût de série ne tient que si le tour produit des **milliers de moteurs** sur sa durée de vie.
- À **12 moteurs/an** (une vente/mois), la part du tour est `200 000 € / 12 ≈ 16 667 €` par moteur.
- Avec la matière produit 2 ch et des charges coulée/outillage conservatrices, le coût de production monte à ≈ **33 420 €**.
- Au prix de vente retenu de **19 999 €**, l'amortissement n'est pas couvert.

## Référence plafond matière

Le test 2 cylindres pleins (2 cylindres `d = 1,5 m`, `L = 2 m`, remplis à 66 % → 12 596 kg Al) est un **plafond matière/référence**, pas une trajectoire produit. Aux hypothèses canette de base configurées dans l'env (14 g, 0,03 €/canette), il représente ~**27 842 €** de matière ; voir [matière recyclée](../../business/recycled-material.md) et [scénarios de coût canette](../../business/recycled-material.md#scénarios-de-coût-canette). Le projet expose désormais le prototype à **15 000 €** (prévoir **30 000 €** sur commande pour bielle et support), distinct du prix de série.

Forcer une charge matière 2 cylindres pleins dans une production à faible volume reste non viable à 19 999 €.

## Actions en scénario d'échec

Si la production reste à quelques unités par tour :

1. **Arrêter la trajectoire d'amortissement par unité** — elle n'est pas viable.
2. **Vendre la machine de production** (tour 2 m) pour récupérer du capital, ou
3. **Louer/partager le tour** avec d'autres productions pour répartir l'amortissement, ou
4. **Produire pour stock** seulement si la demande et la trésorerie le justifient, ou
5. **Augmenter le prix** pour couvrir l'amortissement réel.

## Hypothèses dépassées

- Les anciennes comparaisons « tout le tour sur un seul moteur » et chiffrages sous-traités sont dépassés par le modèle de coûts actuel piloté par l'env et le prix prototype exposé.
- La route du premier prototype reste **impression PLA → moule sable → coulée → finition tour**.

## Voir aussi

- [Premier prototype](../../production/prototype.md)
- [Matière recyclée](../../business/recycled-material.md)
- [Coûts](../../business/costs.md)
- [Équipement d'atelier](../../business/atelier/equipement.md)
- [Modèle de coût de série](../../production/usinage-tour.md)
- [Archive anglaise](../../../archive/scenarios/lathe-low-volume.md)
- [Archive](../README.md)
- [Glossaire](../../GLOSSARY.md)
