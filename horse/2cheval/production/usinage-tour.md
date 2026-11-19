# Usinage tour — Coût de production et prix de revente — Version française (sous-projet 2Cheval)

> **Status:** marketing · **Owns:** per-engine production cost and sale price · **Up:** [Production](README.md)

Le tour à métaux de 2 m est l'investissement principal. Chargé sur un seul moteur, il donne un coût de prototype ≈ **€215 250**. En série, amorti sur des milliers de moteurs, il ne pèse que quelques centaines d'euros par unité. Le coût pessimiste d'un moteur est ≈ **€16 650** ; le prix de vente retenu est **€19 999**, avec ≈ **€3 350** de marge brute, dont **€2 000** pour le salaire (une vente par mois) et ≈ **€1 350** de réserve commerciale.

## 1. Hypothèses (pessimistes, majorant)

- **Tour 2 m** : achat ≈ **€600 000**, durée de vie 3 ans → amortissement **€200 000/an**.
- **Production** : `N` moteurs/an ; scénarios **1 000 / 3 000 / 5 000**.
- **Usure pièce/outillage** pour les 2 chambres : **€3 000/moteur**.
- **Refonte/impression** des 2 cylindres `d = 1,5 m`, `L = 2 m` : **€12 000/moteur**.
- **Brut aluminium** : 2 × 6 300 kg × **€0,02/kg** ≈ **€252/moteur**.
- **Piston + bielle + cylindre** : **€1 200/moteur** (piston ≈ €200, bielle 3 roulements haut de gamme ≈ €900–1 000, cylindre ≈ €50–60).

Majorant : on impute 2 chambres et 2 cylindres à **chaque** moteur. Si les cylindres sont des billets partagés entre plusieurs moteurs, le coût réel par moteur est plus bas. Le moteur 2 ch à petites chambres est lui aussi moins cher ; ce majorant couvre le cas des gros cylindres.

## 2. Coût par moteur

| Poste | 1 000 moteurs/an | 3 000 moteurs/an | 5 000 moteurs/an |
|---|---:|---:|---:|
| Part du tour (`€200 000 / N`) | 200 | 67 | 40 |
| Usure 2 chambres | 3 000 | 3 000 | 3 000 |
| Refonte/impression 2 cylindres | 12 000 | 12 000 | 12 000 |
| Brut aluminium (2 cylindres, 66 %) | 252 | 252 | 252 |
| Piston + bielle + cylindre | 1 200 | 1 200 | 1 200 |
| **Coût de production** | **16 652** | **16 519** | **16 492** |

## 3. Coût max du piston

Pas d'engrenages : une bielle à **3 roulements à billes haut de gamme** et un cylindre de plus.

| Composant | Estimation pessimiste |
|---|---:|
| Piston métallisé | ≈ €200 |
| Bielle (3 roulements haut de gamme + tige + axes) | ≈ €900–1 000 |
| Cylindre de la chambre (aluminium + usinage) | ≈ €50–60 |
| **Total piston** | **≈ €1 200** |

## 4. Prix de vente et marge

| | 1 000 moteurs/an | 3 000 moteurs/an | 5 000 moteurs/an |
|---|---:|---:|---:|
| Coût de production | 16 652 | 16 519 | 16 492 |
| Prix de vente retenu | 19 999 | 19 999 | 19 999 |
| **Marge brute** | **3 347** | **3 480** | **3 507** |
| Dont salaire (1 vente/mois) | 2 000 | 2 000 | 2 000 |
| Réserve commerciale | 1 347 | 1 480 | 1 507 |

Le prix plancher « coût + €2 000 » serait ≈ **€18 650** (à 1 000 moteurs/an). Le prix retenu de **€19 999** laisse ≈ **€1 350** de plus pour le transport, la garantie et l'administration.

## 5. Premier moteur (prototype)

Si on charge tout le tour sur un seul moteur, hors piston : `€200 000 + €3 000 + €12 000 + €252 ≈ €215 250`. Avec le piston : ≈ **€216 450**. C'est le coût du prototype, pas le coût de série. Détail : [machining-cost.md](machining-cost.md).

## 6. Limite honnête

Le prix de **€19 999** tient si le tour produit des **milliers** de moteurs sur sa durée de vie (ou s'il est partagé avec d'autres productions). À 12 moteurs/an (une vente/mois), la part du tour est `€200 000 / 12 ≈ €16 667` par moteur : le coût monte à ≈ **€33 100** et le prix de €19 999 ne couvre pas l'amortissement. Dans ce cas : produire pour stock, louer/partager le tour, ou augmenter le prix.

## Voir aussi

- [Coût de production : usine tour et cylindres](machining-cost.md) — détail du prototype et de la matière.
- [Résilience — moteur résilient à € 19 999](../business/resilience.md) — justification commerciale.
- [Stratégie de production](strategy.md)
- [Coûts business](../business/costs.md)
- [Dictionnaire technique](../GLOSSARY.md#dictionnaire-conceptuel)

Mots-clés : [tour a metaux](../GLOSSARY.md#dictionnaire-conceptuel), [estimations cout / recettes](../business/costs.md).
