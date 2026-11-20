# Valorisation de l'investissement

> **Status:** concept · **Owns:** capex, itérations et apprentissage comme valeur · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/investment-valorisation.md)

La **valorisation de l'investissement** transforme les dépenses (outillage, moules, itérations, mesures) en valeur de projet : coût unitaire plus bas, risque plus faible, géométrie reproductible et savoir-faire. Sur un premier prototype pessimiste, l'argent achète de l'incertitude ; sur les suivants, le même investissement achète de la marge.

## Ce qui est valorisé

| Investissement | Actif créé | Effet sur le coût unitaire |
|---|---|---|
| Atelier / outillage (tour, imprimante, four, rails CNC) | capacité de production | amorti sur `N` unités ; le faible volume est le [scénario d'échec](../archive/scenarios/lathe-low-volume.md) |
| Moules, motifs, impressions PLA | géométrie réutilisable | moins de réessais, itérations plus rapides |
| Itérations de coulée et d'usinage | tolérances mesurées, rebut réduit | le facteur de gaspillage baisse (ex. ×4 → ×2) |
| Essais et instrumentation | `η`, `f`, `ΔT`, étanchéité validés | moteur plus petit à puissance égale via les [leviers](../leviers/README.md) |
| Documentation et modèle | [paramètres soft-coded](../modele/README.md) | décisions cohérentes, construction transmissible |

## Trajectoire pessimiste

| Étape | Gaspillage / risque typique | Action de valorisation |
|---|---|---|
| Premier réessai | rebut élevé, géométrie inconnue, équivalent matière ×3–4 | borner le risque : assurance **15 000–30 000 €** pour le premier moteur |
| Prototype validé | géométrie connue, procédé répétable | figer le motif, mesurer le rendement, réduire les reprises |
| Petite série | outillage amorti, rendement stable | répartir les coûts fixes, garder les charges pessimistes |
| Série | courbe d'apprentissage, moins de rebut | viser un coût unitaire plus bas sans changer la promesse de 2 ch |

L'[estimation gros piston](../engines/manson/costs/estimation-gros-piston.md) illustre la même logique sur une grande pièce : la matière parfaite est bon marché, mais le premier exemplaire isolé paie le gaspillage, le procédé et la marge.

## Lien avec la résilience

La valorisation est une résilience économique : si le premier prototype coûte cher, le projet possède déjà l'outillage, les moules et les données. Si un levier technique échoue, un autre compense ; si une unité coûte cher, la suivante peut coûter moins parce que l'investissement est déjà fait. Voir [résilience](resilience.md) et [coûts](costs.md).

## Voir aussi

- [Coûts](costs.md) — synthèse
- [Premier prototype](../production/prototype.md)
- [Estimation gros piston](../engines/manson/costs/estimation-gros-piston.md)
- [Usinage tour](../production/usinage-tour.md)
- [Stratégie de production](../production/strategy.md)
- [Version anglaise](../../business/investment-valorisation.md)
