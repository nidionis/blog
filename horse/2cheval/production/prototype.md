# Premier prototype — prix et route

> **Status:** canonical prototype route · **Owns:** prix et route du premier prototype · **Up:** [Production](README.md) · **Lang:** FR · [EN](../../engines/manson/costs/prototype.md)

Le premier prototype est un **premier réessai non optimisé**. Le prix exposé du prototype est **15 000 €** ; **prévoir 30 000 € sur commande pour bielle et support**. La matière et les itérations restent des facteurs majeurs (voir [matière recyclée](../business/recycled-material.md) et [scénarios de coût canette](../business/recycled-material.md#scénarios-de-coût-canette)).

## Prix

| Poste | Valeur | Note |
|---|---:|---|
| **Prototype** | **15 000 €** | prévoir **30 000 €** sur commande pour bielle et support |
| Engrenage prototype (si nécessaire) | 10 000 € | poste séparé ; voir [équipement d'atelier](../business/atelier/equipement.md) |
| Matière produit 2 ch (référence) | ~534 € | 241,5 kg, 17 251 canettes + refonte (base 14 g, 0,03 €) |
| Plafond matière test (2 cylindres pleins, 66 %) | ~27 842 € | référence plafond, pas matière produit |

## Route de fabrication

1. **Impression PLA** — motif pour une enveloppe de 1,5 m³, perdu ou réutilisable.
2. **Moule sable** — moule en sable fin (ordre de grandeur 10 m³) autour du motif.
3. **Coulée** — aluminium fondu dans un creuset de ~3 m³ (fonderie sous-traitée ou four solaire). Les hypothèses de remplissage/canettes sont configurées dans `env/`.
4. **Finition tour** — tour 2 m pour les pièces d'environ 1,40 m de diamètre.
5. **Assemblage** — piston, bielle, support/paliers, cylindre, raccords.
6. **Ingénierie et itération** — géométrie, ajustement, étanchéité, intégration combustion.

Le tour sert à la **finition et à la validation**, pas à amortir une machine sur un seul moteur. Voir [usinage tour](usinage-tour.md).

## Positionnement

Le moteur remplace une **PAC air-eau 15–30 kW** (15 000–35 000 €, chaleur seule) ou un **tracteur compact 20–40 ch** (25 000–60 000 €, travail mécanique). À **19 999 €** en série, il fournit ~1,5 kW mécanique + ~29 kW thermique à 5 %. Le rendement de 5 % n'est pas un COP de PAC : c'est un positionnement de prix, pas une équivalence. Voir [coûts](../business/costs.md#4-remplacement-positionnement-de-prix).

## Voir aussi

- [Matière recyclée](../business/recycled-material.md)
- [Équipement d'atelier](../business/atelier/equipement.md)
- [Usinage tour — coût de série](usinage-tour.md)
- [Coûts business](../business/costs.md)
- [Dimensionnement](../engines/manson/sizing.md) · [Carburant](../engines/manson/fuel.md)
- [Version anglaise](../../engines/manson/costs/prototype.md)
