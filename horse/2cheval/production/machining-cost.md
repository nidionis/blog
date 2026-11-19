# Coût de production : usine tour et cylindres — Version française (sous-projet 2Cheval)

> **Status:** marketing · **Owns:** prototype and material production cost · **Up:** [Production](README.md)

Cette page calcule le **coût du premier moteur** (tour chargé à 100 %) et la base matière. Pour le **coût de série** et le prix de revente, voir [usinage-tour.md](usinage-tour.md).

**Hypothèses (pessimistes, honnête approximation) :**
- Tour métaux 2 m : achat ≈ **€600 000**, durée de vie 3 ans → amortissement ≈ **€200 000/an**.
- Usure pièce/outillage pour les 2 chambres : **€3 000**.
- Refonte (sand casting ou binder jetting) des 2 cylindres `d = 1,5 m`, `L = 2 m` : ≈ **€12 000**.
- Brut aluminium : 2 cylindres remplis à 66 %, **2 cents/kg**.

## 1. Tour + usure (premier moteur)

| Poste | Estimation pessimiste |
|---|---:|
| Tour 2 m (1 an d'amortissement) | €200 000 |
| Usure pièce/outillage (2 chambres) | €3 000 |
| **Total tour + usure** | **€203 000** |

## 2. Cylindres d = 1,5 m, L = 2 m (2 cylindres)

`V_cylindre = π · (0,75)² · 2 ≈ 3,53 m³` → 2 cylindres : **7,07 m³** au total.

## 3. Brut matière (un cylindre, rempli à 66 % d'aluminium)

- Masse : 2,33 m³ × 2 700 kg/m³ ≈ **6 300 kg**
- Coût : 6 300 kg × **2 cents/kg** ≈ **€126**
- Brut 2 cylindres : ≈ **€252**

## 4. Refonte / impression (2 cylindres)

- Estimation pessimiste : **€12 000** (moules, stockage, foin, ambiance, manutention).

## 5. Coût du premier moteur (tour chargé à 100 %)

| Poste | Estimation pessimiste |
|---|---:|
| Tour 2 m (1 an) + usure 2 chambres | €203 000 |
| Refonte/impression 2 cylindres | €12 000 |
| Brut aluminium (2 cylindres, 66 %) | €252 |
| **Total hors piston** | **≈ €215 250** |
| Piston + bielle + cylindre | €1 200 |
| **Total avec piston** | **≈ €216 450** |

C'est le coût du **prototype**, pas le coût de série.

## 6. Coût de série par moteur

En série, le tour est réparti sur `N` moteurs/an. À **1 000 moteurs/an** :

| Poste | Coût par moteur |
|---|---:|
| Part du tour (€200 000 / 1 000) | €200 |
| Usure 2 chambres | €3 000 |
| Refonte/impression 2 cylindres | €12 000 |
| Brut aluminium | €252 |
| Piston + bielle + cylindre | €1 200 |
| **Total** | **≈ €16 650** |

Le prix de vente retenu est **€19 999** (marge ≈ €3 350). Scénarios 1 000 / 3 000 / 5 000 et limite honnête : [usinage-tour.md](usinage-tour.md).

## Voir aussi

- [Usinage tour — coût de production et prix de revente](usinage-tour.md)
- [Stratégie de production](strategy.md)
- [Résilience — moteur résilient à € 19 999](../business/resilience.md)
- [Dictionnaire technique](../GLOSSARY.md#dictionnaire-conceptuel)
- [Coûts business](../business/costs.md)
- [Coûts matière cylinders (2ch)](../business/recycled-material.md)
