```python
import numpy as np

powers = [2, 3, 6, 9]
volumes_L = [180, 270, 540, 810] # litres

results = []
for P, V_L in zip(powers, volumes_L):
    V_m3 = V_L / 1000.0
    # diametre = racine(2.5 * volume en m3 / (9 * 3.14))
    diametre = np.sqrt((2.5 * V_m3) / (9 * np.pi))
    longueur = diametre
    results.append({
        'P': P,
        'V_L': V_L,
        'D': diametre,
        'L': longueur
    })

for r in results:
    print(f"P: {r['P']} kW | Volume: {r['V_L']} L | D: {r['D']*1000:.1f} mm | L: {r['L']*1000:.1f} mm")


```

```text
P: 2 kW | Volume: 180 L | D: 126.2 mm | L: 126.2 mm
P: 3 kW | Volume: 270 L | D: 154.5 mm | L: 154.5 mm
P: 6 kW | Volume: 540 L | D: 218.5 mm | L: 218.5 mm
P: 9 kW | Volume: 810 L | D: 267.6 mm | L: 267.6 mm


```

Mes réponses doivent être brèves.

Voici le tableau des dimensions des cylindres (avec $D = L$) calculés selon votre formule :

| Puissance ($P_m$) | Volume ($V_{cycle}$) | Diamètre ($D$) | Longueur ($L$) |
| --- | --- | --- | --- |
| **2 kW** | $180\text{ L}$ ($0{,}180\text{ m}^3$) | **$126\text{ mm}$** ($0{,}126\text{ m}$) | **$126\text{ mm}$** ($0{,}126\text{ m}$) |
| **3 kW** | $270\text{ L}$ ($0{,}270\text{ m}^3$) | **$155\text{ mm}$** ($0{,}155\text{ m}$) | **$155\text{ mm}$** ($0{,}155\text{ m}$) |
| **6 kW** | $540\text{ L}$ ($0{,}540\text{ m}^3$) | **$219\text{ mm}$** ($0{,}219\text{ m}$) | **$219\text{ mm}$** ($0{,}219\text{ m}$) |
| **9 kW** | $810\text{ L}$ ($0{,}810\text{ m}^3$) | **$268\text{ mm}$** ($0{,}268\text{ m}$) | **$268\text{ mm}$** ($0{,}268\text{ m}$) |
