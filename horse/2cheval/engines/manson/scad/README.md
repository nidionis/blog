# CAO paramétrique du piston

> **Status:** illustrative · **Owns:** esquisse paramétrique · **Up:** [M Manson](../README.md) · **Lang:** FR · [EN](../../../../engines/manson/scad/README.md)

`piston.scad` est une **esquisse paramétrique**, pas un plan de production. Le modèle utilise `inner_r = 70` (millimètres) et une unité géométrique appelée `chink` ; il n'est pas à l'échelle du moteur complet. Le fichier est soft-coded : `chamber_l`, `eta`, `delta_t_k`, `frequency_hz` et `pressure_ratio` pilotent la puissance et la masse affichées.

- [`piston.scad`](../../../../engines/manson/scad/piston.scad) — esquisse paramétrique d'un piston et d'une chambre possible.
- [`manson.stl`](../../../../engines/manson/scad/manson.stl) — maillage exporté.

Les volumes et diamètres réels sont dans [dimensionnement](../sizing.md). Les paramètres de calcul sont dans [`model/params.json`](../../../../model/params.json).

## Voir aussi

- [Dimensionnement](../sizing.md) · [Optimisation](../optimisation.md)
- [Moteur Manson](../README.md) · [Version anglaise](../../../../engines/manson/scad/README.md)
