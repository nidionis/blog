#!/usr/bin/env python3
"""Unified calculation source for the 2Cheval / Manson engine.

Configuration is loaded from env/ (values, i18n, svg). No hardcoded digital
values, names, or translations in logic: edit env/* files.

Usage:
    python3 tools/calc.py                 # print baseline and write SVGs
    python3 tools/calc.py --check         # verify baseline numbers
    python3 tools/calc.py --svg           # write SVGs only
    python3 tools/calc.py --tables all    # print all markdown tables
    python3 tools/calc.py --tables sizing:en
    python3 tools/calc.py --update        # rewrite marked blocks in docs
    python3 tools/calc.py --sync          # sync derived compat files (model/params.json)

No third-party dependency.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / "env"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_env() -> dict:
    values = {}
    vdir = ENV / "values"
    for p in sorted(vdir.glob("*.json")):
        values[p.stem] = _load_json(p)
    i18n = {}
    idir = ENV / "i18n"
    for p in sorted(idir.glob("*.json")):
        i18n[p.stem] = _load_json(p)
    concepts = {}
    cdir = ENV / "concepts"
    if cdir.exists():
        for p in sorted(cdir.glob("*.json")):
            concepts[p.stem] = _load_json(p)
    return {"values": values, "i18n": i18n, "concepts": concepts}


CFG = _load_env()
V = CFG["values"]
UNITS = V["units"]
ENGINE = V["engine"]
FUELS = V["fuels"]
TARGETS = V["targets"]
LEVERS = V["levers"]
CHECKS = V["checks"]
SVGCFG = V.get("svg", {})
I18N = CFG["i18n"]

B = ENGINE["baseline"]
HP_W = float(UNITS["hp_w"])
KELVIN = float(UNITS["kelvin_offset"])
W_PER_KW = float(UNITS["w_per_kw"])
SEC_PER_H = float(UNITS["seconds_per_hour"])
L_PER_M3 = float(UNITS["liters_per_m3"])
CM_PER_M = float(UNITS["cm_per_m"])
CHAMBER_RATIO = float(UNITS["chamber_to_working_air_ratio"])
FEED_PERIODS_PER_H = SEC_PER_H / (float(UNITS["feed_limit_period_min"]) * float(UNITS["minutes_per_hour"]))


def compat_params() -> dict:
    """Compatibility shape for model/params.json consumers."""
    return {
        "ambient_c": ENGINE["ambient_c"],
        "baseline": B,
        "targets_hp": TARGETS["targets_hp"],
        "fuels": FUELS,
        "material_rows_hp": TARGETS["material_rows_hp"],
        "stress_test": TARGETS["stress_test"],
        "levers": LEVERS,
    }


PARAMS = compat_params()


def sync_compat() -> list[Path]:
    out = ROOT / "model" / "params.json"
    out.write_text(json.dumps(compat_params(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return [out]


# ---------------------------------------------------------------------------
# Core calculations
# ---------------------------------------------------------------------------

def power_w(eta: float, rho: float, f: float, v_a_m3: float, cp: float,
            delta_t_k: float, pressure_factor: float = 1.0) -> float:
    return eta * rho * f * v_a_m3 * cp * delta_t_k * pressure_factor


def air_volume_m3(power: float, eta: float, rho: float, f: float, cp: float,
                  delta_t_k: float, pressure_factor: float = 1.0) -> float:
    return power / (eta * rho * f * cp * delta_t_k * pressure_factor)


def chamber_m3(v_a_m3: float) -> float:
    return CHAMBER_RATIO * v_a_m3


def diameter_m(v_c_m3: float) -> float:
    # D = L cylinder convention
    return (4.0 * v_c_m3 / math.pi) ** (1.0 / 3.0)


def mass_flow_kg_s(thermal_w: float, cp: float, delta_t_k: float) -> float:
    return thermal_w / (cp * delta_t_k)


def carnot(hot_c: float, cold_c: float | None = None) -> float:
    cold_c = ENGINE["ambient_c"] if cold_c is None else cold_c
    return 1.0 - (cold_c + KELVIN) / (hot_c + KELVIN)


def fuel_limit_kw(eta: float) -> float:
    kg_per_h = B["feed_limit_kg_per_20min"] * FEED_PERIODS_PER_H
    thermal_kw = kg_per_h * B["lhv_straw_mj_kg"] * W_PER_KW / SEC_PER_H
    return eta * thermal_kw


def fuel_flow_kg_h(power_kw: float, eta: float, lhv_mj_kg: float | None = None) -> float:
    lhv = B["lhv_straw_mj_kg"] if lhv_mj_kg is None else lhv_mj_kg
    return power_kw * SEC_PER_H / (eta * lhv * W_PER_KW)


def chamber_mass_kg(v_c_m3: float) -> float:
    return v_c_m3 * B["fill_ratio"] * B["aluminium_density_kg_m3"]


def target(hp: float) -> dict:
    p_w = hp * HP_W
    thermal_w = p_w / B["eta"]
    v_a = air_volume_m3(p_w, B["eta"], B["rho_air_kg_m3"], B["frequency_hz"],
                        B["cp_air_j_kg_k"], B["delta_t_k"])
    v_c = chamber_m3(v_a)
    return {
        "hp": hp,
        "power_kw": p_w / W_PER_KW,
        "thermal_kw": thermal_w / W_PER_KW,
        "mass_flow": mass_flow_kg_s(thermal_w, B["cp_air_j_kg_k"], B["delta_t_k"]),
        "v_a_l": v_a * L_PER_M3,
        "v_c_l": v_c * L_PER_M3,
        "diameter_cm": diameter_m(v_c) * CM_PER_M,
        "mass_kg": chamber_mass_kg(v_c),
    }


def baseline_target() -> dict:
    return target(float(CHECKS["baseline_hp"]))


# ---------------------------------------------------------------------------
# Formatting (driven by i18n locale)
# ---------------------------------------------------------------------------

def _i18n(lang: str) -> dict:
    return I18N.get(lang, I18N.get("en", {}))


def nf(value: float, digits: int = 2, lang: str = "en", group: bool = False) -> str:
    loc = _i18n(lang).get("locale", {})
    dec = loc.get("decimal_separator", ".")
    thou = loc.get("thousands_separator", ",")
    if group:
        s = f"{value:,.{digits}f}"  # 1,234.56
        if dec == "," and thou == " ":
            s = s.replace(",", " ").replace(".", ",")
        elif dec == "." and thou == ",":
            pass
        elif thou != ",":
            s = s.replace(",", thou)
            if dec != ".":
                s = s.replace(".", dec)
        return s
    s = f"{value:.{digits}f}"
    if dec != ".":
        s = s.replace(".", dec)
    return s


def nint(value: float, lang: str = "en") -> str:
    i = int(round(value))
    loc = _i18n(lang).get("locale", {})
    thou = loc.get("thousands_separator", ",")
    s = f"{i:,}"
    if thou != ",":
        s = s.replace(",", thou)
    return s


def money(value: float, lang: str = "en", decimals: int | None = None) -> str:
    loc = _i18n(lang).get("locale", {})
    sym = loc.get("currency_symbol", "€")
    fmt = loc.get("currency_format", "prefix")
    if decimals is None:
        decimals = 2
    if decimals == 0 or (decimals == 2 and abs(value - round(value)) < 0.005 and lang == "fr"):
        core = nf(round(value), 0, lang, group=abs(value) >= W_PER_KW)
    else:
        core = nf(value, decimals, lang, group=abs(value) >= W_PER_KW)
    if fmt == "suffix":
        return f"{core} {sym}"
    return f"{sym}{core}"


def u(lang: str, key: str) -> str:
    return _i18n(lang).get("units", {}).get(key, key)


# ---------------------------------------------------------------------------
# Markdown table generators
# ---------------------------------------------------------------------------

def table_sizing(lang: str = "en") -> str:
    rows = [target(float(hp)) for hp in TARGETS["targets_hp"]]
    t = _i18n(lang)["tables"]["sizing"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for r in rows:
        hp_i = int(r["hp"]) if r["hp"] == int(r["hp"]) else r["hp"]
        power = t["power_cell"].format(kw=nf(r["power_kw"], 2, lang), kw_unit=u(lang, "kw"), hp=hp_i, hp_unit=hp_unit)
        lines.append(
            f"| {power} | {nf(r['thermal_kw'], 1, lang)} {u(lang,'kw')} | "
            f"{nf(r['mass_flow'], 4, lang)} {u(lang,'kg_s')} | "
            f"{nf(r['v_a_l'], 2, lang, group=r['v_a_l']>=L_PER_M3)} {u(lang,'l')} | "
            f"{nf(r['v_c_l'], 2, lang, group=r['v_c_l']>=L_PER_M3)} {u(lang,'l')} | "
            f"**{nf(r['diameter_cm'], 2, lang)} {u(lang,'cm')}** |"
        )
    return "\n".join(lines)


def table_fuel(lang: str = "en") -> str:
    straw = FUELS.get("straw", {})
    charcoal = FUELS.get("charcoal", {})
    oil = FUELS.get("oil", {})
    eta = B["eta"]
    hp_list = TARGETS.get("fuel_hp", [1, 2, 3, 4, 6, 8, 12, 20])
    t = _i18n(lang)["tables"]["fuel"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for hp in hp_list:
        p_kw = hp * HP_W / W_PER_KW
        th_kw = p_kw / eta
        straw_kg = fuel_flow_kg_h(p_kw, eta, straw.get("lhv_mj_kg"))
        straw_l_loose = straw_kg / straw["density_loose_kg_m3"] * L_PER_M3
        straw_l_dense = straw_kg / straw["density_densified_kg_m3"] * L_PER_M3
        char_kg = fuel_flow_kg_h(p_kw, eta, charcoal.get("lhv_mj_kg"))
        oil_kg = fuel_flow_kg_h(p_kw, eta, oil.get("lhv_mj_kg"))
        lines.append(
            f"| {t['power_cell'].format(hp=hp, hp_unit=hp_unit)} | {nf(p_kw, 2, lang)} {u(lang,'kw')} | "
            f"{nf(th_kw, 1, lang)} {u(lang,'kw')} | {nf(straw_kg, 2, lang)} | "
            f"{nf(straw_l_loose, 1, lang)} | {nf(straw_l_dense, 1, lang)} | "
            f"{nf(char_kg, 2, lang)} | {nf(oil_kg, 2, lang)} |"
        )
    return "\n".join(lines)


def table_fuel_fr(lang: str = "fr") -> str:
    straw = FUELS.get("straw", {})
    eta = B["eta"]
    hp_list = TARGETS.get("fuel_hp_fr", [1, 2, 6, 20])
    t = _i18n(lang)["tables"]["fuel"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for hp in hp_list:
        p_kw = hp * HP_W / W_PER_KW
        th_kw = p_kw / eta
        straw_kg = fuel_flow_kg_h(p_kw, eta, straw.get("lhv_mj_kg"))
        straw_l_loose = straw_kg / straw["density_loose_kg_m3"] * L_PER_M3
        straw_l_dense = straw_kg / straw["density_densified_kg_m3"] * L_PER_M3
        lines.append(
            f"| {t['power_cell'].format(hp=hp, hp_unit=hp_unit)} | {nf(p_kw, 2, lang)} {u(lang,'kw')} | "
            f"{nf(th_kw, 1, lang)} {u(lang,'kw')} | {nf(straw_kg, 2, lang)} | "
            f"{nf(straw_l_loose, 1, lang)} | {nf(straw_l_dense, 1, lang)} |"
        )
    return "\n".join(lines)


def table_fuel_cap(lang: str = "en") -> str:
    base = baseline_target()
    t = _i18n(lang)["tables"]["fuel_cap"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for eta in LEVERS["eta"]:
        cap = fuel_limit_kw(eta)
        cap_hp = cap / HP_W * W_PER_KW
        s2 = fuel_flow_kg_h(base["power_kw"], eta)
        s20 = fuel_flow_kg_h(base["power_kw"] * (TARGETS["targets_hp"][-1] / CHECKS["baseline_hp"]), eta)
        pct = f"{int(eta*100)} {u(lang,'percent')}"
        cap_cell = t["cap_cell"].format(kw=nf(cap, 0, lang), kw_unit=u(lang, "kw"), hp=nf(cap_hp, 1, lang), hp_unit=hp_unit)
        lines.append(
            f"| {pct} | {cap_cell} | {nf(s2, 2, lang)} {u(lang,'kg_h')} | {nf(s20, 1, lang)} {u(lang,'kg_h')} |"
        )
    return "\n".join(lines)


def _material_display(hp: float | None = None, v_c_m3: float | None = None) -> dict:
    if v_c_m3 is None and hp is not None:
        t = target(float(hp))
        v_c_l = t["v_c_l"]
        mass = t["mass_kg"]
    else:
        v_c_l = (v_c_m3 or 0.0) * L_PER_M3
        mass = chamber_mass_kg(v_c_m3 or 0.0)
    cans_n = int(round(mass / B["can_mass_kg"]))
    can_cost = cans_n * B["can_price_eur"]
    remelt = mass * B["remelt_kwh_per_kg"] * B["remelt_eur_per_kwh"]
    total = can_cost + remelt
    return {"v_c_l": v_c_l, "mass_kg": mass, "cans_n": cans_n, "can_cost": can_cost, "remelt": remelt, "total": total}


def table_material(lang: str = "en") -> str:
    rows_hp = TARGETS.get("material_rows_hp", [2, 6, 20])
    t = _i18n(lang)["tables"]["material"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for hp in rows_hp:
        c = _material_display(hp=float(hp))
        engine = t["engine_cell"].format(hp=int(hp), hp_unit=hp_unit)
        lines.append(
            f"| {engine} | {nf(c['v_c_l'], 2, lang, group=c['v_c_l']>=L_PER_M3)} {u(lang,'l')} | "
            f"{nf(c['mass_kg'], 1, lang)} {u(lang,'kg')} | {nint(c['cans_n'], lang)} | "
            f"{money(c['can_cost'], lang)} | {money(c['remelt'], lang)} | **{money(c['total'], lang)}** |"
        )
    st = TARGETS.get("stress_test")
    if st:
        c = _material_display(v_c_m3=float(st["vc_m3"]))
        label = t.get("stress_label", st.get("label", "stress test")).format(label=st.get("label", ""))
        lines.append(
            f"| **{label}** | {t.get('stress_volume','2 × 3.534 m³')} | "
            f"{nf(c['mass_kg'], 1, lang, group=c['mass_kg']>=L_PER_M3)} {u(lang,'kg')} | "
            f"{nint(c['cans_n'], lang)} | {money(c['can_cost'], lang)} | {money(c['remelt'], lang)} | **{money(c['total'], lang)}** |"
        )
    return "\n".join(lines)


def table_material_fr(lang: str = "fr") -> str:
    rows_hp = TARGETS.get("material_rows_hp", [2, 6, 20])
    t = _i18n(lang)["tables"]["material"]
    lines = ["| " + " | ".join(t["headers"]) + " |", t["align"]]
    hp_unit = u(lang, "ch")
    for hp in rows_hp:
        c = _material_display(hp=float(hp))
        engine = t["engine_cell"].format(hp=int(hp), hp_unit=hp_unit)
        lines.append(
            f"| {engine} | {nf(c['v_c_l'], 2, lang, group=c['v_c_l']>=L_PER_M3)} {u(lang,'l')} | "
            f"{nf(c['mass_kg'], 1, lang)} {u(lang,'kg')} | {nint(c['cans_n'], lang)} | **{money(c['total'], lang)}** |"
        )
    st = TARGETS.get("stress_test")
    if st:
        c = _material_display(v_c_m3=float(st["vc_m3"]))
        label = t.get("stress_label", "2 cylindres pleins (test)")
        lines.append(
            f"| **{label}** | {t.get('stress_volume','2 × 3,534 m³')} | "
            f"{nf(c['mass_kg'], 1, lang, group=c['mass_kg']>=L_PER_M3)} {u(lang,'kg')} | "
            f"{nint(c['cans_n'], lang)} | **{money(c['total'], lang)}** |"
        )
    return "\n".join(lines)


TABLES = {
    "sizing:en": lambda: table_sizing("en"),
    "sizing:fr": lambda: table_sizing("fr"),
    "fuel:en": lambda: table_fuel("en"),
    "fuel:fr": lambda: table_fuel_fr("fr"),
    "fuel-cap:en": lambda: table_fuel_cap("en"),
    "fuel-cap:fr": lambda: table_fuel_cap("fr"),
    "material:en": lambda: table_material("en"),
    "material:fr": lambda: table_material_fr("fr"),
}


# ---------------------------------------------------------------------------
# SVG generation (config-driven)
# ---------------------------------------------------------------------------

def _svg_text(x, y, value, size=12, anchor="start", weight="normal", fill="#111111", rotate=None, family="sans-serif"):
    extra = f' transform="rotate({rotate} {x} {y})"' if rotate else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{value}</text>')


def _svg_line(x1, y1, x2, y2, color, width=2.0, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}"{extra}/>')


def sensitivity_svg(lang: str = "en") -> str:
    sc = SVGCFG["sensitivity"]
    colors = SVGCFG["colors"]
    i = _i18n(lang)["svg"]["sensitivity"]
    family = SVGCFG.get("fonts", {}).get("family", "sans-serif")
    width, height = sc["width"], sc["height"]
    left, right, top, bottom = sc["left"], sc["right"], sc["top"], sc["bottom"]
    plot_w = width - left - right
    plot_h = height - top - bottom
    x_max = sc["x_max"]
    base = baseline_target()
    base_d = base["diameter_cm"]
    derate = LEVERS["pressure_derate"]
    derate_pct = int(round(derate * 100))
    ctx = {
        "eta_pct": int(B["eta"] * 100), "pct": u(lang, "percent"),
        "delta_t": int(B["delta_t_k"]), "k": u(lang, "k"),
        "hz": int(B["frequency_hz"]) if B["frequency_hz"] == int(B["frequency_hz"]) else B["frequency_hz"],
        "hz_unit": u(lang, "hz"), "baseline_d": nf(base_d, 1, lang), "cm": u(lang, "cm"),
    }
    rows = [
        ("baseline", i["rows"]["baseline"].format(**ctx), base_d, colors["baseline"]),
        ("pressure", i["rows"]["pressure"].format(bar=LEVERS["pressure_ratio"][1], derate=derate_pct), base_d / (1.0 + derate * (LEVERS["pressure_ratio"][1] - 1.0)) ** (1 / 3), colors["pressure"]),
        ("pressure", i["rows"]["pressure"].format(bar=LEVERS["pressure_ratio"][2], derate=derate_pct), base_d / (1.0 + derate * (LEVERS["pressure_ratio"][2] - 1.0)) ** (1 / 3), colors["pressure"]),
        ("pressure", i["rows"]["pressure"].format(bar=LEVERS["pressure_ratio"][3], derate=derate_pct), base_d / (1.0 + derate * (LEVERS["pressure_ratio"][3] - 1.0)) ** (1 / 3), colors["pressure"]),
    ]
    for hot in LEVERS["hot_c"][1:]:
        delta = hot - ENGINE["ambient_c"]
        factor = delta / B["delta_t_k"]
        rows.append(("temperature", i["rows"]["temperature"].format(hot=hot, delta=delta), base_d / factor ** (1 / 3), colors["temperature"]))
    for hz in LEVERS["frequency_hz"][2:]:
        factor = hz / B["frequency_hz"]
        rows.append(("frequency", i["rows"]["frequency"].format(hz=int(hz) if hz == int(hz) else hz), base_d / factor ** (1 / 3), colors["frequency"]))
    for eta in LEVERS["eta"][1:]:
        factor = eta / B["eta"]
        rows.append(("efficiency", i["rows"]["efficiency"].format(pct=int(eta * 100)), base_d / factor ** (1 / 3), colors["efficiency"]))

    def x(value: float) -> float:
        return left + value / x_max * plot_w

    subtitle1 = i["subtitle1"].format(**ctx) if "{" in i["subtitle1"] else i["subtitle1"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{i["aria"]}">',
        f'<rect width="100%" height="100%" fill="{colors["background"]}"/>',
        _svg_text(left, 28, i["title"], sc["title_size"], weight="bold", fill=colors["text"], family=family),
        _svg_text(left, 47, subtitle1, sc["subtitle_size"], fill=colors["text_muted"], family=family),
        _svg_text(left, 64, i["subtitle2"], sc["subtitle_size"], fill=colors["text_muted"], family=family),
    ]
    for value in range(0, int(x_max) + 1, 10):
        out.append(_svg_line(x(value), top, x(value), height - bottom, colors["grid"], 1))
        out.append(_svg_text(x(value), height - bottom + 18, str(value), sc["tick_size"], anchor="middle", fill=colors["text_muted"], family=family))
    out.append(_svg_line(x(base_d), top, x(base_d), height - bottom, colors["baseline"], sc["baseline_width"], sc["baseline_dash"]))
    row_h = plot_h / len(rows)
    for index, (_, label, diameter, color) in enumerate(rows):
        cy = top + (index + 0.5) * row_h
        bar_h = row_h * sc["row_bar_ratio"]
        out.append(_svg_text(left - 10, cy + 4, label, sc["label_size"], anchor="end", fill=colors["text_dark"], family=family))
        out.append(f'<rect x="{left}" y="{cy - bar_h / 2:.1f}" width="{x(diameter) - left:.1f}" height="{bar_h:.1f}" fill="{color}" opacity="{sc["bar_opacity"]}"/>')
        if index:
            out.append(_svg_text(x(diameter) + 6, cy + 4, f"{nf(diameter, 1, lang)} {u(lang,'cm')}", sc["label_size"], fill=colors["text_dark"], family=family))
    legend_keys = ["pressure", "temperature", "frequency", "efficiency"]
    lx = left
    for k, label in zip(legend_keys, i["legend"]):
        out.append(f'<rect x="{lx}" y="{height - sc["legend_y_offset"]}" width="{sc["legend_rect_w"]}" height="{sc["legend_rect_h"]}" fill="{colors[k]}"/>')
        out.append(_svg_text(lx + 20, height - 19, label, sc["legend_size"], fill=colors["text_dark"], family=family))
        lx += sc["legend_item_width"]
    out.append(_svg_text(width - right, height - 19, i["x_label"], sc["axis_label_size"], anchor="end", fill=colors["text_muted"], family=family))
    out.append("</svg>")
    return "\n".join(out)


def fuel_svg(lang: str = "en") -> str:
    fc = SVGCFG["fuel"]
    colors = SVGCFG["colors"]
    i = _i18n(lang)["svg"]["fuel"]
    family = SVGCFG.get("fonts", {}).get("family", "sans-serif")
    width, height = fc["width"], fc["height"]
    left, right, top, bottom = fc["left"], fc["right"], fc["top"], fc["bottom"]
    plot_w = width - left - right
    plot_h = height - top - bottom
    y_max = fc["y_max"]
    etas = LEVERS["eta"]
    cap5 = fuel_limit_kw(B["eta"])
    thermal_kw_cap = cap5 / B["eta"]
    ctx = {
        "feed_kg": int(B["feed_limit_kg_per_20min"]), "feed_min": int(UNITS["feed_limit_period_min"]),
        "lhv": nf(B["lhv_straw_mj_kg"], 0, lang), "thermal_kw": nf(thermal_kw_cap, 0, lang),
        "eta_pct": int(B["eta"] * 100), "pct": u(lang, "percent"),
        "cap_kw": nf(cap5, 0, lang), "cap_hp": nf(cap5 / HP_W * W_PER_KW, 1, lang),
    }

    def y(value: float) -> float:
        return top + plot_h - value / y_max * plot_h

    title = i["title"].format(**ctx) if "{" in i["title"] else i["title"]
    subtitle = i["subtitle"].format(**ctx) if "{" in i["subtitle"] else i["subtitle"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{i["aria"]}">',
        f'<rect width="100%" height="100%" fill="{colors["background"]}"/>',
        _svg_text(left, 28, title, fc["title_size"], weight="bold", fill=colors["text"], family=family),
        _svg_text(left, 47, subtitle, fc["subtitle_size"], fill=colors["text_muted"], family=family),
    ]
    for value in range(0, int(y_max), 10):
        out.append(_svg_line(left, y(value), width - right, y(value), colors["grid"], fc["grid_width"]))
        out.append(_svg_text(left - 8, y(value) + 4, str(value), fc["tick_size"], anchor="end", fill=colors["text_muted"], family=family))
    out.append(_svg_line(left, height - bottom, width - right, height - bottom, colors["axis"], fc["axis_width"]))
    out.append(_svg_line(left, top, left, height - bottom, colors["axis"], fc["axis_width"]))
    out.append(_svg_text(18, top + plot_h / 2, i["y_label"], fc["label_size"], anchor="middle", rotate=-90, fill=colors["text"], family=family))
    bar_w = plot_w / len(etas) * fc["bar_width_ratio"]
    for index, eta in enumerate(etas):
        cx = left + (index + 0.5) * plot_w / len(etas)
        value = fuel_limit_kw(eta)
        out.append(f'<rect x="{cx - bar_w / 2:.1f}" y="{y(value):.1f}" width="{bar_w:.1f}" height="{y(0) - y(value):.1f}" fill="{colors["fuel_bar"]}" opacity="{fc["bar_opacity"]}"/>')
        out.append(_svg_text(cx, y(value) - 8, i["bar_label_kw"].format(v=nf(value, 0, lang)), fc["bar_label_size"], anchor="middle", weight="bold", family=family))
        out.append(_svg_text(cx, height - bottom + 20, f"{int(eta * 100)} {u(lang,'percent')}", fc["label_size"], anchor="middle", family=family))
        out.append(_svg_text(cx, height - bottom + 37, i["bar_label_hp"].format(v=nf(value / HP_W * W_PER_KW, 0, lang)), fc["bar_sub_size"], anchor="middle", fill=colors["text_muted"], family=family))
    baseline_20 = target(20.0)["power_kw"]
    out.append(_svg_line(left, y(baseline_20), width - right, y(baseline_20), colors["baseline"], fc["baseline_width"], fc["baseline_dash"]))
    out.append(_svg_text((left + width - right) / 2, height - 20, i["x_label"], fc["label_size"], anchor="middle", fill=colors["text"], family=family))
    out.append("</svg>")
    return "\n".join(out)


def write_svgs() -> list[Path]:
    out_dir = ROOT / "levers"
    out_dir.mkdir(exist_ok=True)
    paths = []
    for name, content in [("sensitivity.svg", sensitivity_svg("en")), ("fuel-limit.svg", fuel_svg("en"))]:
        p = out_dir / name
        p.write_text(content, encoding="utf-8")
        paths.append(p)
    return paths


# ---------------------------------------------------------------------------
# Markdown block updater
# ---------------------------------------------------------------------------

BLOCK_RE = re.compile(
    r"(?P<start><!--\s*calc:(?P<name>[a-z0-9_:-]+)\s*-->)\n?"
    r"(?P<body>.*?)(?P<end><!--\s*/calc:(?P=name)\s*-->)",
    re.DOTALL,
)

ENV_RE = re.compile(r"\{\{env:([a-zA-Z0-9_.-]+)\}\}")
I18N_RE = re.compile(r"\{\{i18n:([a-z]{2}):([a-zA-Z0-9_.-]+)\}\}")
FENCE_RE = re.compile(r"(```[\s\S]*?```|`[^`\n]+`)")


def _resolve_path(root: dict, dotted: str):
    cur = root
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def _format_env_value(val) -> str:
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, float) and val == int(val):
        return str(int(val))
    return str(val)


def _protect_fences(text: str):
    slots = []

    def repl(m: re.Match) -> str:
        slots.append(m.group(0))
        return f"\x00FENCE{len(slots)-1}\x00"

    return FENCE_RE.sub(repl, text), slots


def _restore_fences(text: str, slots: list[str]) -> str:
    for i, s in enumerate(slots):
        text = text.replace(f"\x00FENCE{i}\x00", s)
    return text


def substitute_env(text: str) -> str:
    text, slots = _protect_fences(text)

    def repl_env(m: re.Match) -> str:
        val = _resolve_path({"values": V, "i18n": I18N, "concepts": CFG.get("concepts", {})}, m.group(1))
        if val is None:
            val = _resolve_path(CFG, m.group(1))
        return _format_env_value(val) if val is not None else m.group(0)

    def repl_i18n(m: re.Match) -> str:
        lang, path = m.group(1), m.group(2)
        val = _resolve_path(I18N.get(lang, {}), path)
        return _format_env_value(val) if val is not None else m.group(0)

    text = ENV_RE.sub(repl_env, text)
    text = I18N_RE.sub(repl_i18n, text)
    return _restore_fences(text, slots)


def update_marked_blocks(paths: list[Path] | None = None) -> list[Path]:
    changed: list[Path] = []
    if paths is None:
        paths = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        protected, slots = _protect_fences(text)

        def repl(m: re.Match) -> str:
            name = m.group("name")
            if name not in TABLES:
                return m.group(0)
            body = TABLES[name]() + "\n"
            return m.group("start") + "\n" + body + m.group("end")

        protected = BLOCK_RE.sub(repl, protected)
        text = _restore_fences(protected, slots)
        text = substitute_env(text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path)
    return changed


# ---------------------------------------------------------------------------
# Checks and CLI
# ---------------------------------------------------------------------------

def check_baseline() -> None:
    base = baseline_target()
    assert abs(base["v_a_l"] - float(CHECKS["v_a_l"])) < float(CHECKS["v_a_tol_l"]), base
    assert abs(base["v_c_l"] - float(CHECKS["v_c_l"])) < float(CHECKS["v_c_tol_l"]), base
    assert abs(base["diameter_cm"] - float(CHECKS["diameter_cm"])) < float(CHECKS["diameter_tol_cm"]), base
    assert abs(fuel_limit_kw(float(CHECKS["fuel_limit_eta"])) - float(CHECKS["fuel_limit_kw"])) < float(CHECKS["fuel_limit_tol_kw"])
    assert abs(fuel_flow_kg_h(base["power_kw"], float(CHECKS["fuel_flow_eta"])) - float(CHECKS["fuel_flow_kg_h"])) < float(CHECKS["fuel_flow_tol_kg_h"])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--svg", action="store_true")
    ap.add_argument("--tables", nargs="?", const="all")
    ap.add_argument("--update", action="store_true")
    ap.add_argument("--sync", action="store_true", help="sync derived compat files (model/params.json)")
    args = ap.parse_args(argv)

    check_baseline()

    if args.sync:
        rpt = _i18n("en").get("report", {})
        for p in sync_compat():
            print(rpt.get("synced", "Synced {path}").format(path=p.relative_to(ROOT)))
        return 0

    if args.check:
        print(_i18n("en").get("report", {}).get("checks_passed", "Baseline checks passed."))
        return 0

    if args.tables:
        if args.tables == "all":
            for name in TABLES:
                print(f"<!-- calc:{name} -->")
                print(TABLES[name]())
                print()
        else:
            for name in args.tables.split(","):
                name = name.strip()
                if name not in TABLES:
                    print(f"Unknown table: {name}", file=sys.stderr)
                    return 2
                print(TABLES[name]())
        return 0

    if args.update:
        sync_compat()
        changed = update_marked_blocks()
        rpt = _i18n("en").get("report", {})
        for p in changed:
            print(rpt.get("updated", "Updated {path}").format(path=p.relative_to(ROOT)))
        if not changed:
            print(rpt.get("no_changes", "No marked blocks changed."))
        return 0

    sync_compat()
    paths = write_svgs()
    base = baseline_target()
    rpt = _i18n("en").get("report", {})
    ctx = {
        "hp": int(CHECKS["baseline_hp"]) if float(CHECKS["baseline_hp"]) == int(float(CHECKS["baseline_hp"])) else CHECKS["baseline_hp"],
        "hp_unit": u("en", "ch"),
        "kw": nf(base["power_kw"], 3), "kw_unit": u("en", "kw"),
        "thermal": nf(base["thermal_kw"], 1),
        "eta_pct": int(B["eta"] * 100), "pct": u("en", "percent"),
        "va": nf(base["v_a_l"], 2), "vc": nf(base["v_c_l"], 2), "d": nf(base["diameter_cm"], 2),
        "l": u("en", "l"), "cm": u("en", "cm"),
        "fill_pct": int(B["fill_ratio"] * 100), "mass": nf(base["mass_kg"], 1), "kg": u("en", "kg"),
    }
    print(rpt.get("baseline_title", "## Baseline"))
    print(rpt.get("power_line", "- 2 hp = {kw} kW mechanical; {thermal} kW thermal at {eta_pct} %.").format(**ctx))
    print(rpt.get("volume_line", "- V_a = {va} L; V_c = {vc} L; D = {d} cm (D = L).").format(**ctx))
    print(rpt.get("mass_line", "- Cast chamber mass at {fill_pct} % fill: {mass} kg (material only).").format(**ctx))
    for p in paths:
        print(rpt.get("wrote", "Wrote {path}").format(path=p.relative_to(ROOT)))
    if not args.svg:
        print()
        print(rpt.get("help", "Use --tables all, --update, --sync, or --check for other modes."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
