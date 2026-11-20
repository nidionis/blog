# Équipement d'atelier — fourchettes de prix indicatives

> **Status:** indicative · **Owns:** fourchettes équipement atelier · **Up:** [Atelier](README.md) · **Lang:** FR · [EN](../../../business/workshop/equipment.md)

Fourchettes indicatives en euros (capex / prototypage). **DIY** = auto-construit ou fortement adapté ; **acheté** = commercial/neuf ou clé en main selon le cas. Les prix varient selon région, état (occasion/neuf), capacité et intégration — à vérifier avant chiffrage.

## Liste d'équipement

| Poste | DIY / auto-construit | Acheté / commercial | Notes / référence |
|---|---:|---:|---|
| Petite imprimante binder jetting | — | ~30 000 € | [iro3d](https://www.iro3d.com/) (référence exemple) |
| Binder jetting XXL (classe 8 m³) | — | 46 000–78 000 € (BOM) · ~100 000 € tout compris | [Détail BOM](../../production/binder-jetting/cost.md) ; les imprimantes sable commerciales sont généralement bien plus chères (ex. [ExOne](https://www.exone.com/), [voxeljet](https://www.voxeljet.com/)) |
| Imprimante PLA XLarge | ~20 000 € | ~30 000 € (cible vente/clé en main) | FDM grand format ; le DIY dépend du bâti, du mouvement, de la tête et du volume |
| Supplément tour / outillage | — | ~5 000 € | outillage, montages, accessoires de finition |
| Extrudeuse à granulés complète (type Titan) | — | ~15 000 € | tête/pellet extruder + intégration |
| Générateur d'azote | — | ~30 000 € | inertage/protection selon procédé |
| Poste à souder | ~500–1 500 € | ~2 000 €+ | MIG/TIG/arc selon épaisseur et facteur de marche |
| Rouleuse de tôle | — | ~50 000 € | équipement industriel, dépend de la capacité |
| Broyeur aluminium (recyclage) | — | ~30 000 € | préparation du flux aluminium recyclé |
| Tour 2 m (finition série) | DIY atypique | ~300 000–800 000 €+ classe neuf / occasion très variable ; hypothèse projet **600 000 €** sur 3 ans | machine-outil lourde ; l'achat en faible volume est un [scénario d'échec](../../archive/scenarios/lathe-low-volume.md). Voir [modèle tour](../../production/usinage-tour.md) |

## Lecture

- **BOM vs tout compris :** la BOM exclut R&D, logiciel, intégration, locaux et mise en service sauf mention.
- **DIY vs acheté :** le DIY peut réduire le cash mais ajoute temps d'ingénierie, risque d'itération et mise au point ; l'achat peut réduire le risque planning mais augmente le capex.
- **Tour de série :** traité comme capex série amorti sur le volume, pas comme équipement d'atelier d'entrée pour un premier prototype.

## Voir aussi

- [Coûts](../costs.md)
- [BOM binder jetting](../../production/binder-jetting/cost.md)
- [Premier prototype](../../production/prototype.md)
- [Modèle usinage tour](../../production/usinage-tour.md)
