# Modèle soft-coded

> **Status:** canonical · **Owns:** documentation du modèle et paramètres de compatibilité · **Up:** [2Cheval](../README.md) · **Lang:** FR · [EN](../../model/README.md)

La configuration est centralisée dans **[`env/`](../../env/README.md)** (valeurs, i18n/traductions, correspondances de concepts). [`params.json`](../../model/params.json) est un **fichier de compatibilité dérivé**, synchronisé depuis `env/` par `tools/calc.py`. Les calculs sont réunis dans [`tools/calc.py`](../../tools/calc.py).

## Source de vérité

- **Valeurs :** `env/values/*.json` (unités/constantes, base moteur, combustibles, cibles, leviers, contrôles, config SVG)
- **Noms/traductions :** `env/i18n/en.json`, `env/i18n/fr.json`
- **Correspondances de concepts :** `env/concepts/concepts.json`
- **Compatibilité dérivée :** `model/params.json` (synchronisé automatiquement)

## Lancer

```bash
python3 tools/calc.py                 # synchronise, affiche la base, écrit les SVG
python3 tools/calc.py --check         # vérifie la base (env/values/checks.json)
python3 tools/calc.py --tables all    # affiche les tableaux Markdown générés
python3 tools/calc.py --update        # synchronise + réécrit les blocs <!-- calc:... --> + {{env:...}}
python3 tools/calc.py --sync          # synchronise uniquement les fichiers de compatibilité

# compatibilité
python3 model/levers.py
python3 model/levers.py --check
```

## Sorties configurées/générées

- Blocs de tableaux : `sizing:en`, `sizing:fr`, `fuel:en`, `fuel:fr`, `fuel-cap:en`, `fuel-cap:fr`, `material:en`, `material:fr`
- Substitutions en ligne hors code : `{{env:values.engine.baseline.eta}}`, `{{i18n:fr:...}}` (résolues au `--update`)
- Les SVG et `model/params.json` sont régénérés depuis `env/`.

## Règle d'édition

- Modifier les hypothèses numériques dans `env/values/*.json`, pas dans les scripts ni en dur dans le texte.
- Modifier les libellés/traductions dans `env/i18n/en.json` et `env/i18n/fr.json`.
- Modifier les correspondances de concepts dans `env/concepts/concepts.json`.
- Après modification : lancer `--update`/`--check`, puis relire le texte concerné.

## Voir aussi

- [Configuration env/](../../env/README.md)
- [Leviers](../leviers/README.md)
- [Dimensionnement](../engines/manson/sizing.md) · [Carburant](../engines/manson/fuel.md) · [Matière recyclée](../business/recycled-material.md)
- [Glossaire](../GLOSSARY.md)
- [Version anglaise](../../model/README.md)
