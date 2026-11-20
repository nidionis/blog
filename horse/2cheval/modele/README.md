# Modèle soft-coded

> **Status:** canonical · **Owns:** constantes de base et sensibilité aux leviers · **Up:** [2Cheval](../README.md) · **Lang:** FR · [EN](../../model/README.md)

Ce dossier est l'entrée unique des chiffres utilisés dans les [articles sur les leviers](../leviers/README.md). Il est volontairement petit : pas de simulation, pas de dépendance externe, seulement les relations du premier ordre utilisées pour le dimensionnement et la sensibilité.

## Fichiers

- [`params.json`](../../model/params.json) — constantes de base et plages des leviers. **Modifier ce fichier, pas les tableaux.**
- [`levers.py`](../../model/levers.py) — calcule les tableaux, vérifie la base et écrit les deux dessins SVG.
- `../../levers/sensitivity.svg` — diamètre de chambre à 2 ch pour chaque levier.
- `../../levers/fuel-limit.svg` — plafond de puissance mécanique selon le rendement.

## Lancer

```bash
python3 model/levers.py          # affiche les tableaux et régénère les SVG
python3 model/levers.py --check  # vérifie seulement les chiffres de base
```

Les contrôles vérifient la base du projet : 2 ch → `V_a` = 67,76 L, `V_c` = 135,53 L, `D` = 55,67 cm, 15 kW à 5 % et 8,83 kg/h. Si une constante change, le contrôle et les articles doivent changer ensemble.

## Relations

```
P        = η · ρ · f · V_a · Cp · ΔT          (puissance air, premier ordre)
V_a      = V_c / 2                           (règle du déplaceur)
D        = (4 · V_c / π)^(1/3)               (convention D = L)
P_fuel   = η · (30 kg / 20 min) · LHV        (plafond d'alimentation à 12 MJ/kg)
m_Al     = 0,66 · V_c · 2700 kg/m³           (masse de chambre coulée, matière seule)
```

Le modèle suppose une masse volumique d'air ambiante constante. La pression entre comme multiplicateur de densité, `ρ_eff = ρ · r_p`, avec un `pressure_derate` pessimiste ; c'est un levier de **variante fermée**, pas une modification du Manson atmosphérique. La température est un multiplicateur de `ΔT` à `η` constant ; la table de Carnot est un plafond, pas une prédiction.

## Ce que le modèle ne fait pas

- Il ne simule pas le cycle réel, la distribution, les fuites ou l'échange thermique.
- Il ne prédit pas le rendement ; `η` est un palier d'entrée.
- Il ne dimensionne ni le stove, ni l'alternateur, ni la structure.
- Il ne remplace pas un essai. Il garde les documents cohérents jusqu'à ce qu'une mesure remplace une hypothèse.

## Voir aussi

- [Leviers](../leviers/README.md) — les articles construits sur ce modèle
- [Glossaire](../GLOSSARY.md) — symboles et unités
- [Dimensionnement](../engines/manson/sizing.md) — tableau canonique des puissances
- [Version anglaise](../../model/README.md)
