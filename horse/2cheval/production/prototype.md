# Premier prototype — PLA, sable, coulée et finition tour — Version française (sous-projet 2Cheval)

> **Status:** canonical prototype route · **Owns:** first prototype cost · **Up:** [Production](README.md)

Le premier moteur n'est pas usiné dans la masse. On imprime la géométrie en **PLA** (1,5 m³), on la moule dans **10 m³ de sable fin**, on coule l'aluminium dans un **creuset de ~3 m³** (four solaire à miroirs ou fonderie sous-traitée), puis on finit la pièce au **tour** (~1,40 m de diamètre). Coût pessimiste : **€52 000–196 000** en sous-traitance, ou **€122 000–426 000** avec achat du four solaire et du creuset.

## 1. Pourquoi pas le tour d'abord ?

Usiner un moteur de 1,5 m³ dans la masse demande un tour de 2 m, beaucoup de matière et des heures d'usinage. Le premier prototype doit valider la géométrie et la coulée, pas la production de série. Le tour vient **après** la coulée, pour la finition fine.

## 2. Route de fabrication

1. **Impression PLA** — motif perdu ou motif réutilisable, 1,5 m³ d'enveloppe, 10–20 % de matière effective (≈ 190–370 kg de PLA). Prix XXL grossier : €100–200/kg, soit €20 000–75 000.
2. **Moule sable** — 10 m³ de sable fin (≈ 16 t), liant, malaxage, mise en place : €3 000–8 000.
3. **Coulée** — aluminium fondu dans un creuset de ~3 m³. Deux options :
   - fonderie sous-traitée : €10 000–30 000 par coulée ;
   - four solaire + creuset + miroirs (plaques d'acier inoxydable polies) : €70 000–230 000 de capex, réutilisable.
4. **Finition tour** — tour 2 m, pièce ~1,40 m, 30–80 h : €3 000–20 000.
5. **Assemblage** — piston, bielle (3 roulements haut de gamme), cylindre, raccords : €1 200–3 000.
6. **Ingénierie** — 300–600 h : €15 000–60 000.

## 3. Coût du premier prototype

| Poste | Bas | Central | Haut |
|---|---:|---:|---:|
| Impression PLA 1,5 m³ | 20 000 | 45 000 | 75 000 |
| Sable fin 10 m³ | 3 000 | 5 000 | 8 000 |
| Coulée sous-traitée | 10 000 | 20 000 | 30 000 |
| Finition tour 1,40 m | 3 000 | 10 000 | 20 000 |
| Piston + bielle + cylindre | 1 200 | 2 000 | 3 000 |
| Ingénierie + assemblage | 15 000 | 30 000 | 60 000 |
| **Total sous-traité** | **52 200** | **112 000** | **196 000** |
| Four solaire + creuset 3 m³ + miroirs | 70 000 | 150 000 | 230 000 |
| **Total avec four** | **122 200** | **262 000** | **426 000** |

Le four et le creuset sont réutilisables : partagés sur 10 prototypes, leur part tombe à €7 000–23 000 par prototype. Le premier prototype seul reste donc à ≈ **€52 000–196 000** ; le four est un investissement d'atelier.

## 4. Ce que cela remplace

Le moteur remplace une **PAC air-eau 15–30 kW** (€15 000–35 000, chaleur seule) ou un **tracteur compact 20–40 ch** (€25 000–60 000, travail mécanique). À **€19 999**, il est dans la fourchette d'une PAC et moins cher qu'un tracteur, tout en fournissant ~1,5 kW mécanique + ~29 kW thermique. Voir [coûts business](../business/costs.md#4-coût-de-ce-que-le-moteur-remplace).

Attention : le rendement mécanique de 5 % n'est pas un COP de PAC. Une PAC déplace 2–4 kWh de chaleur par kWh d'électricité ; le moteur convertit 5 % de la chaleur de la paille en travail mécanique et restitue le reste en chaleur. Le tracteur de 20–40 ch fournit beaucoup plus de puissance : la comparaison est un positionnement de prix, pas une équivalence de puissance ou de thermodynamique.

## 5. Voir aussi

- [Coût de production : usine tour et cylindres](machining-cost.md) — ancien scénario de comparaison.
- [Usinage tour — coût de série et prix de revente](usinage-tour.md)
- [Stratégie de production](strategy.md)
- [Coûts business](../business/costs.md#4-coût-de-ce-que-le-moteur-remplace)
- [Dictionnaire technique](../GLOSSARY.md#dictionnaire-conceptuel)

Mots-clés : [prototype](../GLOSSARY.md#dictionnaire-conceptuel), [moulage sable](../GLOSSARY.md#dictionnaire-conceptuel), [creuset](../GLOSSARY.md#dictionnaire-conceptuel), [four solaire](../GLOSSARY.md#dictionnaire-conceptuel).
