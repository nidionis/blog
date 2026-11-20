#!/usr/bin/env python3
"""Soft-coded sensitivity model for the 2Cheval / Manson engine.

The project baseline is deliberately pessimistic: 5 % overall efficiency,
12 MJ/kg straw, 2 Hz, 180 K temperature difference and a 30 kg / 20 min feed
limit.  This script turns those assumptions into the tables and SVG drawings
used by the `levers/` articles.

Usage:
    python3 model/levers.py          # write the SVG drawings and print tables
    python3 model/levers.py --check  # only check the baseline numbers

No third-party dependency.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARAMS = json.loads((ROOT / "model" / "params.json").read_text(encoding="utf-8"))
B = PARAMS["baseline"]
KELVIN = 273.15
HP_W = 735.5


def power_w(eta: float, rho: float, f: float, v_a_m3: float, cp: float,
            delta_t_k: float, pressure_factor: float = 1.0) -> float:
    """First-order air-power relation, with an optional density multiplier."""
    return eta * rho * f * v_a_m3 * cp * delta_t_k * pressure_factor


def air_volume_m3(power: float, eta: float, rho: float, f: float, cp: float,
                  delta_t_k: float, pressure_factor: float = 1.0) -> float:
    return power / (eta * rho * f * cp * delta_t_k * pressure_factor)


def chamber_m3(v_a_m3: float) -> float:
    """The displacer leaves half of the geometric chamber as working air."""
    return 2.0 * v_a_m3


def diameter_m(v_c_m3: float) -> float:
    """Diameter of a cylinder with D = L (a convention, not a requirement)."""
    return (4.0 * v_c_m3 / math.pi) ** (1.0 / 3.0)


def carnot(hot_c: float, cold_c: float = None) -> float:
    cold_c = PARAMS["ambient_c"] if cold_c is None else cold_c
    return 1.0 - (cold_c + KELVIN) / (hot_c + KELVIN)


def fuel_limit_kw(eta: float) -> float:
    """Mechanical cap from 30 kg / 20 min at the retained 12 MJ/kg."""
    kg_per_h = B["feed_limit_kg_per_20min"] * 3.0
    thermal_kw = kg_per_h * B["lhv_straw_mj_kg"] * 1000.0 / 3600.0
    return eta * thermal_kw


def fuel_flow_kg_h(power_kw: float, eta: float) -> float:
    return power_kw * 3600.0 / (eta * B["lhv_straw_mj_kg"] * 1000.0)


def chamber_mass_kg(v_c_m3: float) -> float:
    return v_c_m3 * B["fill_ratio"] * B["aluminium_density_kg_m3"]


def target(hp: float) -> dict:
    p_w = hp * HP_W
    v_a = air_volume_m3(p_w, B["eta"], B["rho_air_kg_m3"], B["frequency_hz"],
                        B["cp_air_j_kg_k"], B["delta_t_k"])
    v_c = chamber_m3(v_a)
    return {
        "hp": hp,
        "power_kw": p_w / 1000.0,
        "thermal_kw": p_w / 1000.0 / B["eta"],
        "v_a_l": v_a * 1000.0,
        "v_c_l": v_c * 1000.0,
        "diameter_cm": diameter_m(v_c) * 100.0,
        "mass_kg": chamber_mass_kg(v_c),
    }


def baseline_target() -> dict:
    return target(2.0)


def fmt(value: float, digits: int = 1) -> str:
    return f"{value:.{digits}f}"


# ---------------------------------------------------------------------------
# SVG helpers
# ---------------------------------------------------------------------------

COLORS = {
    "pressure": "#1f77b4",
    "temperature": "#d62728",
    "frequency": "#2ca02c",
    "efficiency": "#9467bd",
    "baseline": "#555555",
}


def svg_open(width: int, height: int, title: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
    ]


def svg_text(x: float, y: float, value: str, size: int = 12,
             anchor: str = "start", weight: str = "normal",
             fill: str = "#111111", rotate: int | None = None) -> str:
    extra = f' transform="rotate({rotate} {x} {y})"' if rotate else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{value}</text>')


def svg_line(x1: float, y1: float, x2: float, y2: float, color: str,
             width: float = 2.0, dash: str | None = None) -> str:
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}"{extra}/>')


def svg_polyline(points: list[tuple[float, float]], color: str,
                 width: float = 2.5) -> str:
    raw = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (f'<polyline points="{raw}" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linejoin="round"/>')


def svg_circle(x: float, y: float, r: float, color: str) -> str:
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'


def sensitivity_svg() -> str:
    """Practical 2 hp chamber diameters, one lever at a time."""
    width, height = 820, 560
    left, right, top, bottom = 190, 40, 82, 55
    plot_w = width - left - right
    plot_h = height - top - bottom
    x_max = 60.0

    base_d = baseline_target()["diameter_cm"]
    derate = PARAMS["levers"]["pressure_derate"]
    pressure_label = f"{derate * 100:.0f} % of ideal gain"
    rows = [
        ("baseline", "atmospheric, 5 %, 180 K, 2 Hz", base_d, COLORS["baseline"]),
        ("pressure", f"2 bar ({pressure_label})", base_d / (1.0 + derate * 1.0) ** (1 / 3), COLORS["pressure"]),
        ("pressure", f"4 bar ({pressure_label})", base_d / (1.0 + derate * 3.0) ** (1 / 3), COLORS["pressure"]),
        ("pressure", f"8 bar ({pressure_label})", base_d / (1.0 + derate * 7.0) ** (1 / 3), COLORS["pressure"]),
        ("temperature", "400 °C hot source (ΔT 380 K)", base_d / (380 / 180) ** (1 / 3), COLORS["temperature"]),
        ("temperature", "600 °C hot source (ΔT 580 K)", base_d / (580 / 180) ** (1 / 3), COLORS["temperature"]),
        ("temperature", "800 °C hot source (ΔT 780 K)", base_d / (780 / 180) ** (1 / 3), COLORS["temperature"]),
        ("frequency", "4 Hz", base_d / 2 ** (1 / 3), COLORS["frequency"]),
        ("frequency", "8 Hz", base_d / 4 ** (1 / 3), COLORS["frequency"]),
        ("efficiency", "10 %", base_d / 2 ** (1 / 3), COLORS["efficiency"]),
        ("efficiency", "15 %", base_d / 3 ** (1 / 3), COLORS["efficiency"]),
        ("efficiency", "20 %", base_d / 4 ** (1 / 3), COLORS["efficiency"]),
    ]

    def x(value: float) -> float:
        return left + value / x_max * plot_w

    out = svg_open(width, height, "Practical 2 hp chamber diameters for each lever")
    out.append(svg_text(left, 28, "2 hp chamber: what each lever buys", 17, weight="bold"))
    out.append(svg_text(left, 47, "One lever at a time; dashed line = 55.7 cm baseline. D = L convention.", 11, fill="#555555"))
    out.append(svg_text(left, 64, "Cube-root law: 4× more power only halves the diameter, but mass falls with the cube.", 11, fill="#555555"))

    for value in range(0, 61, 10):
        out.append(svg_line(x(value), top, x(value), height - bottom, "#e5e5e5", 1))
        out.append(svg_text(x(value), height - bottom + 18, f"{value}", 11, anchor="middle", fill="#555555"))
    out.append(svg_line(x(base_d), top, x(base_d), height - bottom, COLORS["baseline"], 1.3, "6 5"))

    row_h = plot_h / len(rows)
    for index, (_, label, diameter, color) in enumerate(rows):
        cy = top + (index + 0.5) * row_h
        bar_h = row_h * 0.62
        out.append(svg_text(left - 10, cy + 4, label, 10.8, anchor="end", fill="#333333"))
        out.append(f'<rect x="{left}" y="{cy - bar_h / 2:.1f}" width="{x(diameter) - left:.1f}" '
                   f'height="{bar_h:.1f}" fill="{color}" opacity="0.85"/>')
        if index:
            out.append(svg_text(x(diameter) + 6, cy + 4, f"{diameter:.1f} cm", 10.8, fill="#333333"))

    legend = [
        ("pressure", COLORS["pressure"]),
        ("temperature", COLORS["temperature"]),
        ("frequency", COLORS["frequency"]),
        ("efficiency", COLORS["efficiency"]),
    ]
    lx = left
    for label, color in legend:
        out.append(f'<rect x="{lx}" y="{height - 28}" width="14" height="10" fill="{color}"/>')
        out.append(svg_text(lx + 20, height - 19, label, 10.5, fill="#333333"))
        lx += 120

    out.append(svg_text(width - right, height - 19, "chamber diameter (cm)", 10.5, anchor="end", fill="#555555"))
    out.append("</svg>")
    return "\n".join(out)


def fuel_svg() -> str:
    """Mechanical power cap versus efficiency at the 30 kg / 20 min feed."""
    width, height = 820, 420
    left, right, top, bottom = 70, 30, 60, 70
    plot_w = width - left - right
    plot_h = height - top - bottom
    y_max = 65.0
    etas = PARAMS["levers"]["eta"]

    def y(value: float) -> float:
        return top + plot_h - value / y_max * plot_h

    out = svg_open(width, height, "Fuel-limited mechanical power versus efficiency")
    out.append(svg_text(left, 28, "Fuel cap: 30 kg / 20 min × 12 MJ/kg = 300 kW thermal", 17, weight="bold"))
    out.append(svg_text(left, 47, "Mechanical cap = efficiency × 300 kW. At the 5 % baseline it is 15 kW ≈ 20.4 hp.", 11, fill="#555555"))
    for value in range(0, 61, 10):
        out.append(svg_line(left, y(value), width - right, y(value), "#e5e5e5", 1))
        out.append(svg_text(left - 8, y(value) + 4, f"{value}", 11, anchor="end", fill="#555555"))
    out.append(svg_line(left, height - bottom, width - right, height - bottom, "#333333", 1.2))
    out.append(svg_line(left, top, left, height - bottom, "#333333", 1.2))
    out.append(svg_text(18, top + plot_h / 2, "mechanical cap (kW)", 12, anchor="middle", rotate=-90))

    bar_w = plot_w / len(etas) * 0.55
    for index, eta in enumerate(etas):
        cx = left + (index + 0.5) * plot_w / len(etas)
        value = fuel_limit_kw(eta)
        out.append(f'<rect x="{cx - bar_w / 2:.1f}" y="{y(value):.1f}" width="{bar_w:.1f}" '
                   f'height="{y(0) - y(value):.1f}" fill="#2ca02c" opacity="0.85"/>')
        out.append(svg_text(cx, y(value) - 8, f"{value:.0f} kW", 12, anchor="middle", weight="bold"))
        out.append(svg_text(cx, height - bottom + 20, f"{eta * 100:.0f} %", 12, anchor="middle"))
        out.append(svg_text(cx, height - bottom + 37, f"{value / HP_W * 1000:.0f} hp", 10.5, anchor="middle", fill="#555555"))

    out.append(svg_line(left, y(14.71), width - right, y(14.71), COLORS["baseline"], 1.4, "6 5"))
    out.append(svg_text((left + width - right) / 2, height - 20, "overall efficiency", 12, anchor="middle"))
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def markdown_report() -> str:
    base = baseline_target()
    lines: list[str] = []
    lines.append("## Baseline")
    lines.append("")
    lines.append(f"- 2 hp = {base['power_kw']:.3f} kW mechanical; {base['thermal_kw']:.1f} kW thermal at 5 %.")
    lines.append(f"- V_a = {base['v_a_l']:.2f} L; V_c = {base['v_c_l']:.2f} L; D = {base['diameter_cm']:.2f} cm (D = L).")
    lines.append(f"- Cast chamber mass at 66 % fill: {base['mass_kg']:.1f} kg (material only).")
    lines.append("")
    lines.append("## Targets")
    lines.append("")
    lines.append("| hp | kW | thermal kW | V_a L | V_c L | D cm | Al mass kg |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for hp in PARAMS["targets_hp"]:
        item = target(float(hp))
        lines.append(f"| {hp} | {item['power_kw']:.2f} | {item['thermal_kw']:.1f} | "
                     f"{item['v_a_l']:.1f} | {item['v_c_l']:.1f} | {item['diameter_cm']:.1f} | {item['mass_kg']:.0f} |")
    lines.append("")
    lines.append("## Levers")
    lines.append("")
    lines.append("| Lever | Range | 2 hp D (cm) | Note |")
    lines.append("|---|---:|---:|---|")
    for ratio in PARAMS["levers"]["pressure_ratio"]:
        derate = PARAMS["levers"]["pressure_derate"]
        factor = 1.0 + derate * (ratio - 1.0)
        lines.append(f"| pressure | {ratio} bar | {base['diameter_cm'] / factor ** (1/3):.1f} | {derate * 100:.0f} % of ideal gain |")
    for hot in PARAMS["levers"]["hot_c"]:
        factor = (hot - PARAMS["ambient_c"]) / B["delta_t_k"]
        lines.append(f"| hot source | {hot} °C | {base['diameter_cm'] / factor ** (1/3):.1f} | η held at 5 % |")
    for f in PARAMS["levers"]["frequency_hz"]:
        factor = f / B["frequency_hz"]
        lines.append(f"| frequency | {f} Hz | {base['diameter_cm'] / factor ** (1/3):.1f} | ideal filling |")
    for eta in PARAMS["levers"]["eta"]:
        factor = eta / B["eta"]
        lines.append(f"| efficiency | {eta * 100:.0f} % | {base['diameter_cm'] / factor ** (1/3):.1f} | same 2 hp |")
    lines.append("")
    lines.append("## Fuel cap")
    lines.append("")
    lines.append("| η | mechanical cap kW | hp | 2 hp fuel kg/h | 20 hp fuel kg/h |")
    lines.append("|---:|---:|---:|---:|---:|")
    for eta in PARAMS["levers"]["eta"]:
        cap = fuel_limit_kw(eta)
        lines.append(f"| {eta * 100:.0f} % | {cap:.1f} | {cap / HP_W * 1000:.1f} | "
                     f"{fuel_flow_kg_h(base['power_kw'], eta):.2f} | {fuel_flow_kg_h(base['power_kw'] * 10, eta):.2f} |")
    lines.append("")
    lines.append("## Solar aperture (2 hp)")
    lines.append("")
    lines.append("| η | 10 min thermal kWh | 24 h thermal kWh | 10 min area m² (2 kWh/m²/day) | 24 h area m² (2 kWh/m²/day) |")
    lines.append("|---:|---:|---:|---:|---:|")
    for eta in [0.05, 0.15]:
        ten_min = base["power_kw"] * (10 / 60) / eta
        day = base["power_kw"] * 24 / eta
        lines.append(f"| {eta * 100:.0f} % | {ten_min:.2f} | {day:.0f} | {ten_min / 2:.2f} | {day / 2:.0f} |")
    return "\n".join(lines)


def main() -> int:
    base = baseline_target()
    assert abs(base["v_a_l"] - 67.76) < 0.2, base
    assert abs(base["diameter_cm"] - 55.67) < 0.2, base
    assert abs(fuel_limit_kw(0.05) - 15.0) < 0.1
    assert abs(fuel_flow_kg_h(base["power_kw"], 0.05) - 8.83) < 0.05

    if "--check" in sys.argv:
        print("Baseline checks passed.")
        return 0

    out_dir = ROOT / "levers"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "sensitivity.svg").write_text(sensitivity_svg(), encoding="utf-8")
    (out_dir / "fuel-limit.svg").write_text(fuel_svg(), encoding="utf-8")
    print(markdown_report())
    print("")
    print(f"Wrote {out_dir / 'sensitivity.svg'}")
    print(f"Wrote {out_dir / 'fuel-limit.svg'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
