# Résilience — Moteur résilient justifiant un prix de € 19 999 — Version française (sous-projet 2Cheval)

> **Status:** marketing · **Owns:** resilience argument (price € 19 999) · **Up:** [Business](README.md)

Un moteur à la paille, en cycle ouvert, est résilient : il fonctionne avec une vaste gamme de sources, est silencieux, fonctionne en extérieur/hiver, et est conçu pour des applications flexibles. Il justifie un prix d'entrée de **€ 19 999**.

## Résilience des sources d'énergie (électric / solar / thermic / fossil / biomass)

- **Biomasse (paille) :** [Rocket stove → straw](../energy/rocket-stove/straw.md) — carburant de référence, disponible localement, peu coûteux.
- **Thermique :** le moteur est une source de chaleur compacte (voir [thermodynamique](../engines/manson/thermodynamics.md)) ; pour un système thermique, un [alternateur électrique](../engines/stirling/linear-alternator.md) d'électricité ou un système de distribution peut récupérer l'énergie thermique.
- **Électricité :** [générateur électrique](../engines/stirling/linear-alternator.md) — électricité continue, silencieuse.
- **Solar :** peut servir de charge locale ou complément à la paille dans un système hybride.
- **Fossile :** rarement requis pour le projet ; relevant plutôt du [nuclear](../energy/nuclear/README.md).

## Applications : heat pump, electricity generator, tractor

- **Heat pump (pompe à chaleur) :** le moteur produit de la chaleur compacte et efficace, pertinent pour une heat pump à basse énergie.
- **Electricity generator (générateur électrique) :** le [Stirling Beta](../engines/stirling/README.md) est l'alternative étudiée avec alternateur linéaire ; on peut aussi générer de l'électricité via le moteur Manson.
- **Tracteur (tractor highly expected) :** le moteur de traction attendu : [transmission](../drivetrain/README.md) et [design du tracteur](../drivetrain/design.md).

## Silent system (perspective armée)

- Système silencieux : moteur sans bruit, pertinent pour les applications militaires ou silencieuses (tracteurs, générateurs, systèmes de secours).

## Justification du prix de € 19 999

- **Coût de production pessimiste : ≈ €16 650/moteur** (tour réparti sur des milliers d'unités, 2 chambres, 2 cylindres, piston et bielle). **Prix de vente retenu : €19 999.** Marge brute : ≈ **€3 350**, dont **€2 000** pour le salaire (une vente/mois) et ≈ **€1 350** de réserve commerciale (transport, garantie, administration).
- **Limite honnête :** à 12 moteurs/an, la part du tour monte à ≈ €16 667/moteur et le coût dépasse €33 000. Le prix de €19 999 suppose donc une production de milliers d'unités sur la vie du tour (ou un tour partagé/loué). Détail : [usinage tour — coûts / recettes](../production/usinage-tour.md).
- Le moteur 2Cheval s'appuie sur l'un de ces axes résilients pour justifier ce prix d'entrée de **€19 999** (voir aussi [coûts business](costs.md) et [modèle économique](business-model.md)).

## Voir aussi

- [Business model](business-model.md)
- [Cas client](customers.md)
- [Production et impression 3D](../production/README.md)
- [Dictionnaire technique](../GLOSSARY.md#dictionnaire-conceptuel)
- [État stationnaire](../../engines/manson/thermodynamic-steady.md)
