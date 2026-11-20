# Matière recyclée — aluminium de canettes

> **Status:** canonical · **Owns:** estimation de matière première recyclée · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/recycled-material.md)

Estimation de matière pour de l'aluminium coulé à partir de canettes. Le prix est durci à **0,03 €/canette** (attendu : 0,02 €) et la refonte est comptée **séparément**. C'est uniquement la matière : usinage, liant, main-d'œuvre et reste de la chaîne sont exclus. La dérivation complète est dans la [page anglaise](../../business/recycled-material.md).

## Hypothèses

| Paramètre | Valeur |
|---|---:|
| Densité de l'aluminium compacté | **2 700 kg/m³** |
| Masse d'une canette | **13,5 g** (74 canettes/kg) |
| Remplissage de la chambre | **66 %** |
| Prix de la canette | **0,03 €/canette** |
| Énergie de refonte | **0,3375 kWh/kg** (four à 80 %) |
| Électricité solaire autoconsommée | **0,20 €/kWh** |
| Coût de refonte | **0,0675 €/kg** |

## Matière par moteur

| Moteur | `V_c` total | Aluminium | Canettes | **Total matière** |
|---|---:|---:|---:|---:|
| **2 ch** | 135,53 L | 241,5 kg | 17 890 | **553 €** |
| **6 ch** | 406,6 L | 724,6 kg | 53 671 | **1 659 €** |
| **20 ch** | 1 355,26 L | 2 415,1 kg | 178 894 | **5 530 €** |
| **2 cylindres pleins** (test) | 2 × 3,534 m³ | 12 596,2 kg | 933 053 | **28 842 €** |

La dernière ligne est la borne haute de l'**assurance premier prototypage**, pas un coût produit par moteur. Le remplissage à 66 % maintient la refonte sous ce maximum.

## Lecture

- Le moteur **2 ch** coûte ≈ **553 €** de matière : 537 € de canettes et 16 € de refonte.
- À 0,03 €/canette, les canettes dominent : ≈ 97 % du total, la refonte ≈ 3 %.
- Le test **2 cylindres pleins** coûte ≈ **28 842 €**, arrondi à **30 000 €** comme plafond d'assurance. Voir [premier prototype](../production/prototype.md).
- Amortir cette charge sur quelques unités est le [scénario d'échec](../archive/scenarios/lathe-low-volume.md) : vendre ou louer la machine.

## Voir aussi

- [Coûts](costs.md) · [Usinage tour](../production/usinage-tour.md)
- [Dimensionnement Manson](../engines/manson/sizing.md)
- [Glossaire](../GLOSSARY.md)
- [Version anglaise](../../business/recycled-material.md)
