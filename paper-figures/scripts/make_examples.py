#!/usr/bin/env python3
"""Generate the example figures shipped in ../examples/.

Every figure uses synthetic data: these are style demonstrations, not results from any paper,
and they contain nothing copied from published work. Run from anywhere:

    python scripts/make_examples.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from figure_style import (  # noqa: E402
    apply_style, new_fig, save, panel_label, OKABE_ITO, SERIES, PAIR, SEQ_CMAP,
)

OUT = HERE.parent / "examples"
rng = np.random.default_rng(7)


def deuteranopia(hex_color: str, severity: float = 1.0) -> str:
    """Deuteranopia simulation (Machado et al. 2009, severity 1.0)."""
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    m = [
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501, 0.047413],
        [-0.011820, 0.042940, 0.968881],
    ]
    out = [sum(m[i][j] * (r, g, b)[j] for j in range(3)) for i in range(3)]
    out = [max(0, min(255, int(round(v)))) for v in out]
    return "#{:02x}{:02x}{:02x}".format(*out)


def cdf_eras():
    """fig01: four era CDFs, direct-labelled at the y=0.9 crossing."""
    apply_style()
    fig, ax = new_fig(3.5, 2.35)
    eras = [
        ("Pre-AI", 19, OKABE_ITO["black"]),
        ("Early", 11, OKABE_ITO["blue"]),
        ("Pre-LLM", 6, OKABE_ITO["vermillion"]),
        ("AI", 3, OKABE_ITO["green"]),
    ]
    for name, med, color in eras:
        data = np.clip(rng.lognormal(mean=np.log(med), sigma=0.9, size=60), 0.5, 365)
        x = np.sort(np.concatenate([[0], data]))
        y = np.arange(len(x)) / (len(x) - 1)
        ax.step(x, y, where="post", color=color, lw=1.2, label=name)
    # Curves are ordered and tightly packed near the top, so a horizontal legend above the
    # axes is cleaner than four colliding end-labels. Direct labels win only when they fit.
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.01), ncol=4, fontsize=6.5,
              handlelength=1.4, columnspacing=1.0, handletextpad=0.4, borderaxespad=0.0)
    ax.set_xscale("log")
    ax.set_xlim(1, 365)
    ax.set_ylim(0, 1.02)
    ax.set_xticks([1, 7, 30, 90, 365])
    ax.set_xticklabels(["1", "7", "30", "90", "365"])
    ax.set_xlabel("Days since disclosure (log scale)")
    ax.set_ylabel("Fraction with a public PoC")
    fig.subplots_adjust(left=0.17, right=0.97, bottom=0.20, top=0.84)
    return save(fig, OUT / "fig01_cdf")


def dumbbell():
    """fig02: paired comparison on a shared axis; no floating bars, no legend box."""
    apply_style()
    fig, ax = new_fig(3.5, 1.95)
    rows = [
        ("PHP Group", 3, 76),
        ("GitHub (GHSA)", 0, 69),
        ("CERT-EU", 0, 66),
        ("Distro trackers", 0, 63),
        ("Aggregators", 0, 61),
    ]
    ypos = np.arange(len(rows))[::-1]
    for y, (name, lit, fam) in zip(ypos, rows):
        ax.plot([lit, fam], [y, y], color="#BBBBBB", lw=1.6, zorder=1, solid_capstyle="round")
        ax.plot([lit], [y], "o", color=PAIR[0], ms=4.5, zorder=3)
        ax.plot([fam], [y], "o", color=PAIR[1], ms=4.5, zorder=3)
        ax.text(fam + 1.8, y, f"{fam}%", va="center", fontsize=7, color=PAIR[1])
        if lit > 0:
            ax.text(lit - 1.8, y, f"{lit}%", va="center", ha="right", fontsize=7, color=PAIR[0])
    ax.set_yticks(ypos)
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlim(-9, 92)
    ax.set_ylim(-0.65, len(rows) - 0.35)
    ax.set_xlabel("Advisory recall against validated units (%)")
    ax.grid(axis="x", color="#EEEEEE", lw=0.5)
    ax.grid(axis="y", visible=False)
    ax.legend(
        handles=[
            Line2D([], [], marker="o", ls="", color=PAIR[0], ms=4, label="literal lens"),
            Line2D([], [], marker="o", ls="", color=PAIR[1], ms=4, label="family lens"),
        ],
        loc="lower right", bbox_to_anchor=(1.0, 1.01), ncol=2, fontsize=6.5,
        handletextpad=0.3, columnspacing=1.0, borderaxespad=0.0,
    )
    fig.subplots_adjust(left=0.29, right=0.97, bottom=0.25, top=0.86)
    return save(fig, OUT / "fig02_dumbbell")


def swimlane():
    """fig03: disclosure timeline as swimlanes; the story is the ordering, not the axes."""
    apply_style()
    fig, ax = new_fig(3.5, 2.2)
    lanes = {"Finders": 2.4, "Vendor": 1.4, "Public": 0.4}
    events = [
        # x, lane, label, dx, dy, ha
        (0.3, "Finders", "3 teams report, independently", 8, 10, "left"),
        (3.0, "Vendor", "acknowledged", 0, -12, "center"),
        (5.2, "Public", "CVE id leaks on a tracker", 0, 10, "center"),
        (7.0, "Vendor", "advisory + fix", -8, 10, "right"),
        (9.0, "Vendor", "co-rooted CVE added", 8, -14, "left"),
        (11.5, "Public", "patch 7.4.x", 0, 10, "center"),
    ]
    for x, lane, label, dx, dy, ha in events:
        y = lanes[lane]
        ax.plot([x], [y], "o", ms=4.6, color=SERIES[0], zorder=4)
        ax.annotate(
            label, xy=(x, y), xytext=(dx, dy),
            textcoords="offset points", fontsize=6.3, ha=ha,
            va="bottom" if dy > 0 else "top", color="#222222",
        )
    ax.axvline(7.0, color="#999999", lw=0.7, ls=(0, (3, 2)), zorder=1)
    ax.text(7.55, 3.0, "coordinated release", fontsize=5.8, color="#666666",
            va="top", ha="left")
    ax.set_yticks(list(lanes.values()))
    ax.set_yticklabels(list(lanes.keys()))
    ax.set_ylim(0.0, 3.05)
    ax.set_xlim(-0.6, 13.4)
    ax.set_xlabel("Days from the first report")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color="#F0F0F0", lw=0.5)
    fig.subplots_adjust(left=0.20, right=0.98, bottom=0.20, top=0.92)
    return save(fig, OUT / "fig03_swimlane")


def taxonomy():
    """fig04: a 3x3 typology with only the populated cells drawn."""
    apply_style()
    fig, ax = new_fig(3.5, 2.05)
    cells = {(1, 3): 8, (2, 1): 5, (2, 2): 4, (3, 2): 3, (3, 3): 11}
    for (stage, driver), count in cells.items():
        strong = count >= 8
        color = SERIES[0] if strong else "#666666"
        box = FancyBboxPatch(
            (stage - 0.40, driver - 0.26), 0.80, 0.52,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            linewidth=1.0 if strong else 0.7, edgecolor=color,
            facecolor="white", zorder=3,
        )
        ax.add_patch(box)
        ax.text(stage, driver + 0.05, str(count), ha="center", va="center",
                fontsize=10, fontweight="bold", color=color, zorder=4)
        ax.text(stage, driver - 0.14, f"S{stage}×D{driver}", ha="center", va="center",
                fontsize=5.8, color="#666666", zorder=4)
    ax.set_xlim(0.45, 3.55)
    ax.set_ylim(0.45, 3.55)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["S1 discovery", "S2 disclosure", "S3 remediation"], fontsize=6.8)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["D1 technical", "D2 process", "D3 tooling"], fontsize=6.8)
    ax.set_xlabel("Stage where the gap originates", fontsize=7)
    ax.set_ylabel("Driver", fontsize=7)
    ax.grid(visible=False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    fig.subplots_adjust(left=0.20, right=0.97, bottom=0.22, top=0.96)
    return save(fig, OUT / "fig04_taxonomy")


def heatmap():
    """fig05: matrix with a perceptually uniform map and in-cell values."""
    apply_style()
    fig, ax = new_fig(3.5, 2.15)
    versions = ["5.6", "7.0", "7.4", "8.1", "8.3"]
    chains = ["A", "B", "C", "D", "E"]
    data = np.array([
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [100, 100, 80, 40, 0],
        [np.nan, 60, 60, 20, 0],
        [np.nan, 40, 40, 0, 0],
    ], dtype=float)
    cmap = plt.get_cmap(SEQ_CMAP).copy()
    cmap.set_bad("#F2F2F2")
    im = ax.imshow(np.ma.masked_invalid(data), cmap=cmap, vmin=0, vmax=100, aspect="auto")
    for i in range(len(chains)):
        for j in range(len(versions)):
            v = data[i, j]
            if np.isnan(v):
                ax.text(j, i, "—", ha="center", va="center", fontsize=7, color="#999999")
            else:
                ax.text(j, i, f"{int(v)}", ha="center", va="center", fontsize=7,
                        color="white" if v < 55 else "#111111")
    ax.set_xticks(range(len(versions)))
    ax.set_xticklabels([f"PHP {v}" for v in versions], fontsize=6.5)
    ax.set_yticks(range(len(chains)))
    ax.set_yticklabels([f"Chain {c}" for c in chains], fontsize=6.5)
    ax.grid(visible=False)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.05, pad=0.02)
    cbar.set_label("% of runs exploitable", fontsize=6.5)
    cbar.ax.tick_params(labelsize=6, length=2)
    cbar.outline.set_visible(False)
    fig.subplots_adjust(left=0.17, right=0.86, bottom=0.14, top=0.96)
    return save(fig, OUT / "fig05_heatmap")


def pareto():
    """fig06: trade-off scatter with a Pareto frontier (nothing dominates it)."""
    apply_style()
    fig, ax = new_fig(3.5, 2.3)
    eras = [("Pre-AI", OKABE_ITO["black"], 19, 2.5), ("Early", OKABE_ITO["blue"], 11, 4.0),
            ("Pre-LLM", OKABE_ITO["vermillion"], 6, 6.5), ("AI", OKABE_ITO["green"], 3, 11.0)]
    pts = []
    for name, color, med, art in eras:
        x = np.clip(rng.lognormal(np.log(med), 0.5, 10), 1, 120)
        y = np.clip(rng.normal(art, art * 0.25, 10), 0.5, 30)
        ax.scatter(x, y, s=13, color=color, alpha=0.9, linewidths=0, zorder=3)
        pts.append(np.column_stack([x, y]))
    pts = np.vstack(pts)
    order = np.argsort(pts[:, 0])
    best, fx, fy = -np.inf, [], []
    for x, y in pts[order]:
        if y > best:
            best = y
            fx.append(x)
            fy.append(y)
    # extend the last step to the right edge, so a single dominant point still draws a line
    if fx:
        fx.append(150.0)
        fy.append(fy[-1])
    ax.step(fx, fy, where="post", color="#111111", lw=0.9, ls=(0, (4, 2)), zorder=2)
    ax.annotate("Pareto frontier", xy=(fx[0], fy[0]), xytext=(4, 4),
                textcoords="offset points", fontsize=6.3, color="#333333", va="bottom")
    ax.set_xscale("log")
    ax.set_xlim(0.8, 150)
    ax.set_ylim(0, 26)
    ax.set_xlabel("Days to first public PoC (log scale)")
    ax.set_ylabel("Public artifacts at 30 days")
    handles = [Line2D([], [], marker="o", ls="", ms=4, color=c, label=n) for n, c, *_ in eras]
    ax.legend(handles=handles, loc="lower right", fontsize=6.5, handletextpad=0.3,
              borderaxespad=0.3, labelspacing=0.2)
    fig.subplots_adjust(left=0.16, right=0.97, bottom=0.20, top=0.96)
    return save(fig, OUT / "fig06_pareto")


def small_multiples():
    """fig07: 2x2 panels, shared axes, one shared y label, panel labels."""
    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(3.5, 2.55), sharex=True, sharey=True)
    eras = [("Pre-AI", 2.5, 4.0), ("Early", 4.0, 5.0), ("Pre-LLM", 6.5, 5.5), ("AI", 11.0, 6.0)]
    for ax, (era, art, adv), letter in zip(axes.flat, eras, ["A", "B", "C", "D"]):
        ax.bar([0, 1], [art, adv], width=0.62, color=[SERIES[0], SERIES[3]], edgecolor="none")
        ax.set_title(era, fontsize=7.5, pad=2)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["artifacts", "advisories"], fontsize=6.2)
        ax.set_ylim(0, 13)
        ax.grid(axis="y", color="#EEEEEE", lw=0.5)
        ax.grid(axis="x", visible=False)
        panel_label(ax, letter, x=-0.16, y=1.16)
        for xi, v in zip([0, 1], [art, adv]):
            ax.text(xi, v + 0.35, f"{v:g}", ha="center", fontsize=6.2)
    fig.text(0.015, 0.55, "Median count at 30 days", rotation=90,
             va="center", fontsize=7)
    fig.subplots_adjust(left=0.17, right=0.98, bottom=0.13, top=0.85, hspace=0.62, wspace=0.20)
    return save(fig, OUT / "fig07_smallmultiples")


def palette():
    """fig08: the palette, plus its grayscale and deuteranopia behaviour."""
    apply_style()
    names = ["black", "orange", "sky", "green", "yellow", "blue", "vermillion", "purple"]
    colors = [OKABE_ITO[n] for n in names]
    fig, ax = plt.subplots(figsize=(3.5, 2.6))
    ax.set_xlim(-0.95, 4.02)
    ax.set_ylim(-0.62, 3.85)
    ax.axis("off")
    ax.text(-0.95, 3.72, "Color Universal Design palette", fontsize=7, fontweight="bold")
    ax.text(-0.95, 3.45, "distinct in colour, in grayscale, and for deuteranopia",
            fontsize=6, color="#555555")

    def swatch(x, y, h, color):
        ax.add_patch(Rectangle((x + 0.02, y), 0.92, h, color=color, ec="#222222", lw=0.4))

    # colour grid: 4 x 2
    for i, (name, hexv) in enumerate(zip(names, colors)):
        x = i % 4
        y = 2.85 - (i // 4) * 1.05
        swatch(x, y, 0.5, hexv)
        ax.text(x + 0.48, y - 0.14, name, ha="center", fontsize=5.6, color="#222222")
        ax.text(x + 0.48, y - 0.31, hexv, ha="center", fontsize=5.0, color="#777777")

    # grayscale: 4 x 2
    ax.text(-0.92, 0.62, "grayscale", fontsize=5.6, color="#555555", va="center")
    for i, hexv in enumerate(colors):
        g = int(0.299 * int(hexv[1:3], 16) + 0.587 * int(hexv[3:5], 16)
                + 0.114 * int(hexv[5:7], 16))
        x = i % 4
        y = 0.75 - (i // 4) * 0.38
        swatch(x, y, 0.26, f"#{g:02x}{g:02x}{g:02x}")

    # deuteranopia: 4 x 2
    ax.text(-0.92, -0.30, "deuteranopia", fontsize=5.6, color="#555555", va="center")
    for i, hexv in enumerate(colors):
        x = i % 4
        y = -0.18 - (i // 4) * 0.38
        swatch(x, y, 0.26, deuteranopia(hexv))

    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.99)
    return save(fig, OUT / "fig08_palette")


def good_vs_bad():
    """fig09: the same data, drawn wrong and right, side by side."""
    apply_style()
    labels = ["A", "B", "C", "D", "E"]
    values = np.array([6, 11, 3, 4, 8])
    fig, (bad, good) = plt.subplots(1, 2, figsize=(3.5, 1.85))
    bad.pie(values, explode=[0.07] * 5, shadow=True,
            colors=plt.get_cmap("jet")(np.linspace(0.05, 0.95, 5)),
            textprops={"fontsize": 4.5}, startangle=140, wedgeprops={"lw": 0.3})
    bad.set_title("AVOID: rainbow pie, shadow, 4.5 pt text", fontsize=5.6, pad=3,
                  color="#B00020")
    order = np.argsort(values)[::-1]
    y = np.arange(len(values))[::-1]
    good.barh(y, values[order], height=0.60, color=SERIES[0])
    good.set_yticks(y)
    good.set_yticklabels([labels[i] for i in order], fontsize=6.5)
    good.set_xlim(0, 13)
    good.set_xlabel("count", fontsize=6.5)
    good.grid(axis="x", color="#EEEEEE", lw=0.5)
    good.grid(axis="y", visible=False)
    for yi, v in zip(y, values[order]):
        good.text(v + 0.3, yi, str(v), va="center", fontsize=6.5)
    good.set_title("PREFER: sorted bars, direct labels, 7 pt text", fontsize=5.6, pad=3,
                   color="#006400")
    fig.subplots_adjust(left=0.06, right=0.97, bottom=0.20, top=0.86, wspace=0.45)
    written = save(fig, OUT / "fig09_good_vs_bad")
    Image.open(str(OUT / "fig09_good_vs_bad.png")).convert("L").save(
        str(OUT / "fig09_good_vs_bad_grayscale.png")
    )
    written.append(str(OUT / "fig09_good_vs_bad_grayscale.png"))
    return written


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for fn in (cdf_eras, dumbbell, swimlane, taxonomy, heatmap, pareto,
               small_multiples, palette, good_vs_bad):
        print(fn.__name__, "->", [Path(p).name for p in fn()])


if __name__ == "__main__":
    main()
