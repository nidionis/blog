# Résilience — un moteur pessimiste, plusieurs issues

> **Status:** marketing · **Owns:** argument de résilience et de prix · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/resilience.md)

Le 2Cheval n'est pas résilient parce qu'il serait optimal. Il l'est parce qu'il est dimensionné au **plancher pessimiste** et qu'il possède plusieurs façons indépendantes de s'améliorer, de substituer une source ou de dégrader proprement. Cette page est l'argument derrière le prix de **19 999 €** ; les chiffres sont dans [leviers](../leviers/README.md) et [coûts](costs.md).

## 1. Quatre résiliences

| Type | Question | Réponse |
|---|---|---|
| **Source** | Et si la paille manque ? | Bois, granulés, charbon de bois, pétrole, chaleur solaire, chaleur nucléaire ; le moteur ne demande que de la chaleur. |
| **Charge** | Et si la charge change ? | Arbre, chaleur, électricité, tracteur, pompe à chaleur ; un arbre lent se redirige facilement. |
| **Conception** | Et si une pièce ou une compétence manque ? | Cycle ouvert, pression atmosphérique, basse fréquence, coulées simples, transmission hackable. |
| **Économie** | Et si l'optimiste échoue ? | La base à 5 % délivre encore 2 ch ; le prix est ancré à ce que le moteur remplace. |

## 2. Résilience des sources

Le [Manson](../engines/manson/README.md) est un moteur à **combustion externe** : l'air de travail ne se mélange jamais au carburant. Le [rocket stove](../energy/rocket-stove/README.md) peut brûler tout ce qui brûle ; le moteur ne voit ni cendre, ni humidité, ni couleur de flamme — seulement la chaleur qui atteint son côté chaud.

| Source | État | Porteur | Contrainte | Article |
|---|---|---|---|---|
| Paille | référence | 12 MJ/kg, 100–250 kg/m³ | alimentation, humidité | [paille](../energy/rocket-stove/straw.md) |
| Bois, granulés, miscanthus | substitut | 13,5–18 MJ/kg | cendre, taille du stove | [biomasse](../energy/rocket-stove/biomass-calorific.md) |
| Charbon de bois, pétrole | substitut dense | 30–43 MJ/kg | coût, stockage, sécurité | [carburant](../engines/manson/fuel.md) |
| Chaleur solaire | hybride | 2–6 kWh/m²/jour | surface, nuit, hiver | [solaire](../energy/solaire/README.md) |
| Chaleur nucléaire | exploratoire | échelle 1–12 ch | blindage, réglementation | [nucléaire](../energy/nuclear/README.md) |
| Électricité / PAC | remplacement | réseau ou batterie | capex, dépendance réseau | [coûts](costs.md#4-coût-de-ce-que-le-moteur-remplace) |

Une paille mouillée ou de mauvaise qualité ne casse pas le moteur : elle baisse la puissance disponible et augmente la consommation. La base pessimiste à 12 MJ/kg tient déjà compte d'un mauvais lot. La limite de **30 kg / 20 min** est une hypothèse de **stove et d'alimentation**, pas une loi thermodynamique : paille densifiée, meilleure vis ou plusieurs stoves peuvent l'augmenter. Voir [carburant](../engines/manson/fuel.md).

## 3. Résilience des charges

- **Arbre** — sortie principale ; un arbre lent et coupleux entraîne un [tracteur](../drivetrain/design.md), une pompe, un moulin ou un treuil.
- **Chaleur** — l'essentiel de l'énergie de la paille sort en chaleur. Un échangeur peut la récupérer pour l'espace, l'eau ou un procédé.
- **Électricité** — un [alternateur linéaire](../engines/stirling/linear-alternator.md) est étudié pour la variante Stirling ; le Manson peut aussi entraîner une génératrice.
- **Stockage** — une [batterie](../electric/README.md) est pratique mais chère au kWh ; un stock d'eau chaude ou de biomasse est moins cher pour la chaleur. Le stockage cinétique est documenté dans la [transmission](../drivetrain/design.md).

Le point n'est pas qu'une charge serait meilleure. Le point est que la même source de chaleur peut servir plusieurs charges : un marché qui échoue ou une génératrice en panne ne bloque pas le moteur.

## 4. Résilience de conception

- **Cycle ouvert, pression atmosphérique** — pas de carter étanche, pas de chambre haute pression, pas de suralimentation.
- **Basse fréquence** — 2 Hz tolère des roulements simples et une combustion imparfaite ; la vitesse est un levier optionnel.
- **Matériaux simples** — aluminium coulé à partir de canettes, chambre finie au tour, [transmission hackable](../drivetrain/README.md).
- **Production locale** — [impression PLA → moule sable → coulée → tour](../production/prototype.md) peut se faire près du client.
- **Modèle soft-coded** — le [modèle des leviers](../modele/README.md) rend les compromis explicites et modifiables.

## 5. Modes de défaillance et réponses

| Défaillance | Réponse | Levier |
|---|---|---|
| Le rendement reste à 5 % | Construire la chambre 2 ch plus grande ; tenir la promesse | [volume et poids](../leviers/volume-poids.md) |
| Chambre trop lourde ou trop grande | Monter pression, fréquence ou température | [pression](../leviers/pression.md), [fréquence](../leviers/frequence.md), [température](../leviers/temperature.md) |
| Paille trop humide ou trop chère | Sécher, densifier, mélanger bois/granulés, ou monter le rendement | [rendement](../leviers/rendement.md), [paille](../energy/rocket-stove/straw.md) |
| Pas de soleil | Brûler de la paille ; le solaire est un hybride, pas une dépendance | [ensoleillement](../leviers/ensoleillement.md) |
| Pas de biomasse | Chaleur solaire ou étude nucléaire ; sinon le moteur remplace une PAC | [solaire](../energy/solaire/README.md), [nucléaire](../energy/nuclear/README.md) |
| Pas de réseau | Arbre et chaleur directs ; l'électricité est optionnelle | [transmission](../drivetrain/README.md) |
| Faible volume de production | Ne pas amortir un tour sur quelques unités ; vendre ou louer la machine | [scénario d'échec](../archive/scenarios/lathe-low-volume.md) |
| Le prix de la canette monte | Utiliser de la ferraille, du minerai ou une autre route de coulée | [matière recyclée](recycled-material.md) |

## 6. Le plancher pessimiste est la garantie

Tous les chiffres commerciaux utilisent le plancher : **5 % de rendement, 12 MJ/kg de paille, 66 % de remplissage, 30 kg / 20 min, 0,03 €/canette**. La cible de 15 % et le plafond de 20 % sont du bonus, pas la promesse. S'ils arrivent, le moteur devient plus petit, plus léger et moins cher au kW ; sinon, le produit 2 ch fonctionne quand même.

## 7. Positionnement de prix

| Objet | Coût typique | Note |
|---|---:|---|
| PAC air-eau, 15–30 kW | 15 000–35 000 € | chaleur seule, COP 2–4 |
| Tracteur compact, 20–40 ch | 25 000–60 000 € | travail mécanique |
| **Moteur 2Cheval** | **19 999 €** | ~1,5 kW d'arbre + ~29 kW de chaleur à 5 % |

Le rendement mécanique de 5 % n'est **pas** un COP de PAC. La comparaison est un positionnement de prix pour la chaleur plus le travail d'arbre, pas une équivalence thermodynamique. Voir [coûts](costs.md#4-coût-de-ce-que-le-moteur-remplace) et [clients](customers.md).

## 8. Limites

Ce n'est ni un mouvement perpétuel ni un remplacement universel. Le moteur est lourd, son rendement électrique est faible, son alimentation est limitée, le solaire est intermittent et la variante nucléaire est une étude, pas un dossier de sécurité. Résilience signifie **dégradation gracieuse**, pas capacité infinie.

## Voir aussi

- [Leviers](../leviers/README.md) — les six chemins d'amélioration
- [Clients](customers.md) — le cas d'usage de référence
- [Coûts](costs.md) — atelier, prototype, série et remplacement
- [Énergie](../energy/README.md) — sources de chaleur
- [Stockage électrique](../electric/README.md) — pourquoi les batteries sont le maillon faible
- [Version anglaise](../../business/resilience.md)
