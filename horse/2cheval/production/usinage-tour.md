# Usinage tour — coût de série et prix de vente

> **Status:** marketing · **Owns:** coût de production de série · **Up:** [Production](README.md) · **Lang:** FR · [EN](../../engines/manson/costs/lathe-machining.md)

Le tour à métaux de 2 m sert à la **finition** et à la série, pas à la première fabrication. Le premier prototype est à **15 000 €** (prévoir **30 000 €** sur commande pour bielle et support) : voir [premier prototype](prototype.md). En série, le tour est amorti sur des **milliers de moteurs**. La dérivation complète est dans la [page anglaise](../../engines/manson/costs/lathe-machining.md).

## Hypothèses pessimistes

- **Tour 2 m** : achat ≈ **600 000 €**, durée de vie 3 ans → **200 000 €/an**.
- **Production** : `N` moteurs/an ; scénarios 1 000 / 3 000 / 5 000.
- **Usure** des 2 chambres : **3 000 €/moteur**.
- **Refonte/impression** des 2 cylindres : **12 000 €/moteur**.
- **Aluminium recyclé** (2 ch, 135,53 L) : 241,5 kg → **17 251 canettes** à 0,03 € (base 14 g, env) + 16,30 € de refonte = **~534 €/moteur**. Voir [matière recyclée](../business/recycled-material.md).
- **Piston + bielle + cylindre** : **1 200 €/moteur**.

Les lignes usure et refonte restent majorées de 2 gros cylindres : le total est conservateur.

## Résultat

| | 1 000 moteurs/an | 3 000 moteurs/an | 5 000 moteurs/an |
|---|---:|---:|---:|
| **Coût de production** | **16 934 €** | **16 801 €** | **16 774 €** |
| Prix de vente retenu | 19 999 € | 19 999 € | 19 999 € |
| **Marge brute** | **3 065 €** | **3 198 €** | **3 225 €** |

En comparaison, le prototype seul est à **15 000 €** (prévoir **30 000 €** sur commande pour bielle et support) ; le prix de série inclut l'amortissement outillage et la marge. Marge ≈ **2 000 €** de salaire (une vente/mois) et réserve commerciale.

## Scénario d'échec

Produire quelques unités par tour est la **pire option** : à 12 moteurs/an, la part du tour est ≈ 16 667 €/moteur et le coût monte à ≈ 33 420 €, au-dessus de 19 999 €. Action : **vendre ou louer la machine de production**. Voir [scénario d'échec](../archive/scenarios/lathe-low-volume.md).

## Voir aussi

- [Premier prototype](prototype.md) · [Matière recyclée](../business/recycled-material.md)
- [Coûts business](../business/costs.md) · [Équipement d'atelier](../business/atelier/equipement.md)
- [Stratégie de production](strategy.md)
- [Version anglaise](../../engines/manson/costs/lathe-machining.md)
