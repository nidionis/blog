<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<style>
    body { font-family: serif; font-size: 11pt; line-height: 1.4; margin: 20mm; color: #111; }
    h1 { font-size: 16pt; text-align: center; }
    .author { text-align: center; font-style: italic; margin-bottom: 20px; }
    h2 { font-size: 13pt; border-bottom: 1px solid #ccc; margin-top: 15px; }
    .abstract { background: #f9f9f9; padding: 10px; border-left: 3px solid #666; font-size: 10pt; }
    table { width: 100%; border-collapse: collapse; margin: 15px 0; }
    th, td { border: 1px solid #bbb; padding: 6px 10px; text-align: center; }
    th { background-color: #f0f0f0; }
</style>
</head>
<body>

<h1>Estimation du volume d'air pour un moteur de Manson à cycle ouvert (2 à 9 kW)</h1>
<div class="author">Note technique synthétique</div>

<div class="abstract">
<strong>Résumé :</strong> Estimation du débit d'air et du volume balayé pour un moteur de Manson à cycle ouvert (2, 3, 6 et 9 kW). Hypothèses : rendement &eta; = 0{,}05, &Delta;T = 300 K, fréquence f = 2 Hz.
</div>

<h2>1. Formules et Hypothèses</h2>
<p>
P<sub>th</sub> = P<sub>m</sub> / &eta;<br>
q<sub>m</sub> = P<sub>th</sub> / (C<sub>p</sub> &middot; &Delta;T) (avec C<sub>p</sub> = 1005 J/(kg&middot;K))<br>
V<sub>cycle</sub> = (q<sub>m</sub> / &rho;) / f (avec &rho; = 1{,}2 kg/m<sup>3</sup>)
</p>

<h2>2. Résultats Numériques</h2>
<table>
    <tr>
        <th>Puissance (P<sub>m</sub>)</th>
        <th>Puissance Thermique (P<sub>th</sub>)</th>
        <th>Débit Massique (q<sub>m</sub>)</th>
        <th>Volume par Cycle (V<sub>cycle</sub>)</th>
    </tr>
    <tr><td>2 kW</td><td>40 kW</td><td>0,43 kg/s</td><td><strong>180 litres</strong></td></tr>
    <tr><td>3 kW</td><td>60 kW</td><td>0,65 kg/s</td><td><strong>270 litres</strong></td></tr>
    <tr><td>6 kW</td><td>120 kW</td><td>1,30 kg/s</td><td><strong>540 litres</strong></td></tr>
    <tr><td>9 kW</td><td>180 kW</td><td>1,95 kg/s</td><td><strong>810 litres</strong></td></tr>
</table>

<h2>3. Conclusion</h2>
<p>
Les volumes obtenus (180 à 810 litres par cycle) confirment les fortes contraintes dimensionnelles des moteurs à air à cycle ouvert pour des puissances de l'ordre du kilowatt.
</p>

</body>
</html>
