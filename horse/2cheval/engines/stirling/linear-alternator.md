# Stirling Beta — Alternateur linéaire (Version française, sous-projet 2Cheval)

> **Status:** exploratory summary · **Owns:** linear-alternator ranges · **Up:** [Stirling](README.md)

Résumé des plages d'aimants, bobines et contrôle pour un alternateur linéaire de Stirling à piston libre. Le détail brut est dans [l'estimation de bobine](notes/coil-estimation.md).

Cela s'applique à un Stirling à piston libre avec alternateur linéaire, pas au Manson.

## Aimants et moueur

- NdFeB **N42–N52** ; utiliser les grades SH/UH/EH ou SmCo si les aimants dépassent ~80 °C.
- Diamètre extérieur des aimants **40–150 mm**, épaisseur **5–20 mm** pour la classe 1–2 kW.
- Entrefer (air gap) **0,5–1,5 mm** ; c'est la contrainte mécanique la plus serrée.
- Masse du moueur **5–20 kg** ; il participe à la masse résonante.
- Course **100–200 mm** pour la classe 1–2 kW.
- Une arrangement Halbach peut gagner ~20–30 % de flux mais complique l'assemblage.

## Bobines

- Alternateur : **500–5 000 tours par phase** ; **3 000–6 000+** pour >100 V à 2 Hz.
- Conducteur **0,5–4 mm²** (≈ AWG 20–12) ; du fil Litz n'est pas obligatoire à 2–10 Hz.
- Stator sans fer évite le détourage, au prix d'un couplage plus faible ; un noyau en fer laminé nécessite un soin particulier dans les encoches.
- Bobine du déplaceur : **200–600 tours**, force cible 10–50 N, piloté avec un avance de phase d'environ 90°.

## Contrôle

À 2 Hz et 1–2 kW, la tension induite est faible et le courant élevé, donc les pertes par effet Joule comptent. Bobiner plusieurs sections indépendantes le long de la course et les relier en série ; utiliser un contrôle de charge active comme une boîte de vitesses virtuelle pour stabiliser l'oscillation.

## Voir aussi
- [Dictionnaire / Glossary](../../GLOSSARY.md)

- [Dimensionnement Beta](beta-sizing.md)
- [Estimation brute de bobine](notes/coil-estimation.md)
- [Références de vibration](notes/vibrating.md)
- [Hub Stirling](README.md)
