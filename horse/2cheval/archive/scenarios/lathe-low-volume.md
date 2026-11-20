# Scénario d'échec — faible volume tour et vente de machine

> **Status:** archived scenario · **Owns:** risque d'amortissement tour à faible volume · **Up:** [Archive](../README.md)

Cette page archive la **pire option** de production : utiliser un tour de 2 m comme unité de production pour seulement quelques moteurs par an. Elle est conservée comme **scénario d'échec** et déclencheur pour envisager la vente ou la location de la machine de production.

## Pourquoi c'est la pire option

- **Tour 2 m** : achat ≈ **600 000 €**, durée de vie 3 ans → amortissement **200 000 €/an**.
- Le modèle de coût de série ne tient que si le tour produit des **milliers de moteurs** sur sa durée de vie.
- À **12 moteurs/an** (une vente/mois), la part du tour est `200 000 € / 12 ≈ 16 667 €` par moteur.
- Avec la matière produit 2 ch et des charges coulée/outillage conservatrices, le coût de production monte à ≈ **33 420 €**.
- Au prix de vente retenu de **19 999 €**, l'amortissement n'est pas couvert.

## Test de charge 2 cylindres pleins (plafond matière)

Le test matière utilise 2 cylindres pleins `d = 1,5 m`, `L = 2 m`, remplis à 66 % → 12 596 kg, 933 053 canettes, **28 842 €** de matière (canettes 27 992 € + refonte 850 €). Cette valeur est prise comme **valeur maximale d'un premier réessai non optimisé** et arrondie à **30 000 €** comme assurance d'investissement pour le premier prototypage : **15 000–30 000 €**.

Si la même charge 2 cylindres pleins est forcée dans une production tour à faible volume, le total devient ≈ **45 242 €** à 1 000 moteurs/an et reste ≈ **45 082 €** à 5 000 moteurs/an — marge négative à 19 999 €. Confirmation : ne pas utiliser la billette 2 cylindres pleins comme trajectoire produit par moteur.

## Actions en scénario d'échec

Si la production reste à quelques unités par tour :

1. **Arrêter la trajectoire d'amortissement par unité** — elle n'est pas viable.
2. **Vendre la machine de production** (tour 2 m) pour récupérer du capital, ou
3. **Louer/partager le tour** avec d'autres productions pour répartir l'amortissement, ou
4. **Produire pour stock** seulement si la demande et la trésorerie le justifient, ou
5. **Augmenter le prix** pour couvrir l'amortissement réel.

## Hypothèses dépassées

- Ancienne comparaison « tout le tour sur un seul moteur » : ≈ 243 842 € hors piston (≈ 245 042 € avec piston) avec les hypothèses canettes/refonte durcies. Pas un scénario de première fabrication.
- Les anciennes fourchettes de premier prototype sous-traité 52 000–196 000 € et capex four 122 000–426 000 € sont dépassées par l'**assurance d'investissement de prototypage 15 000–30 000 €** ancrée au plafond matière non optimisé de 30 000 €.
- La route du premier prototype reste conceptuellement **impression PLA → moule sable → coulée → finition tour**, mais son investissement est borné par cette fourchette d'assurance plutôt que par l'ancien chiffrage sous-traité.

## Voir aussi

- [Premier prototype](../../production/prototype.md)
- [Matière recyclée](../../business/recycled-material.md)
- [Coûts](../../business/costs.md)
- [Modèle de coût de série](../../production/usinage-tour.md)
- [Archive anglaise](../../../archive/scenarios/lathe-low-volume.md)
- [Archive](../README.md)
- [Dictionnaire / Glossary](../../GLOSSARY.md)
