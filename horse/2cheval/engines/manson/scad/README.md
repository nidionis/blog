# CAO paramétrique du piston

> **Status:** illustrative · **Owns:** esquisse paramétrique · **Up:** [Manson](../README.md) · **Lang:** FR · [EN](../../../../engines/manson/scad/README.md)

`piston.scad` est une **esquisse paramétrique**, pas un plan de production. Le modèle utilise `inner_r = 70` mm et une unité géométrique appelée `chink` ; il n'est pas à l'échelle du moteur complet.

## Configuration liée à l'env

Les paramètres moteur/matière sont **pilotés par l'env** :

- [`../../../../env/values/engine.json`](../../../../env/values/engine.json) est la source de vérité (rendement, ΔT, fréquence, propriétés de l'air, remplissage, densité, plage de coût canette, refonte).
- [`env.scad`](../../../../engines/manson/scad/env.scad) est **généré** depuis l'env par `tools/calc.py` (`--sync`, `--update` ou exécution par défaut).
- [`piston.scad`](../../../../engines/manson/scad/piston.scad) inclut `env.scad` et utilise ces valeurs pour le rapport puissance/masse ; la géométrie propre à l'esquisse (`inner_r`, `chamber_l`, `pressure_ratio`) reste locale.

## Fichiers

- [`piston.scad`](../../../../engines/manson/scad/piston.scad) — esquisse paramétrique (configurée par env).
- [`env.scad`](../../../../engines/manson/scad/env.scad) — configuration env générée pour OpenSCAD.
- [`manson.stl`](../../../../engines/manson/scad/manson.stl) — maillage exporté.

## Lancer

```bash
python3 tools/calc.py --sync   # régénère env.scad (et params de compatibilité)
openscad engines/manson/scad/piston.scad
```

## Voir aussi

- [Dimensionnement](../sizing.md) · [Optimisation](../optimisation.md)
- [Matière recyclée / scénarios canette](../../../business/recycled-material.md)
- [Modèle soft-coded](../../../modele/README.md)
- [Moteur Manson](../README.md) · [Version anglaise](../../../../engines/manson/scad/README.md)
