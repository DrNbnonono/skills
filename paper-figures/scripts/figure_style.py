#!/usr/bin/env python3
"""Publication figure style for security/systems papers (S&P, USENIX, CCS, NDSS).

One place for the choices every figure in the paper should share: size, fonts, palette,
line weights, spines, direct labels, vector export.

Usage
-----
    from figure_style import apply_style, new_fig, save, panel_label, PALETTE, SERIES

    apply_style()                        # global rcParams (call once)
    fig, ax = new_fig()                  # 3.5 x 2.3 in, one panel
    ax.plot(x, y, color=SERIES[0], label="Pre-AI")
    save(fig, "fig_cdf")                 # writes fig_cdf.pdf and fig_cdf.png (300 dpi)

Column widths (inches), for LaTeX figures:

    IEEEtran single column  3.5    double column 7.16
    ACM sigconf single      3.33   double       7.0
    USENIX single           3.4    double       7.0

Set the figure to the width it will be printed at, with fonts at print size. Scaling a
large figure down at LaTeX time shrinks the fonts below the 7 pt floor.
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pathlib import Path

# ---------------------------------------------------------------------------
# Palettes
# ---------------------------------------------------------------------------

# Okabe & Ito, "Color Universal Design (CUD)" — colour-blind safe, distinct in grayscale.
# https://jfly.uni-koeln.de/color/
OKABE_ITO = {
    "black": "#000000",
    "orange": "#E69F00",
    "sky": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
}

# Default series order: dark first, so a single-series plot is black (prints anywhere).
SERIES = [
    OKABE_ITO["black"],
    OKABE_ITO["blue"],
    OKABE_ITO["vermillion"],
    OKABE_ITO["green"],
    OKABE_ITO["orange"],
    OKABE_ITO["purple"],
    OKABE_ITO["sky"],
]

# Two-tone for "before / after", "claim / observed": readable in B&W by lightness.
PAIR = [OKABE_ITO["black"], OKABE_ITO["vermillion"]]

# Sequential: perceptually uniform, safe in grayscale (never jet/rainbow).
SEQ_CMAP = "cividis"
DIV_CMAP = "RdBu_r"   # only for signed deviations around a meaningful zero

# Line and marker styles for series that also survive greyscale printing.
LINESTYLES = ["-", "--", "-.", ":"]
MARKERS = ["o", "s", "^", "D", "v", "P"]


# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
def apply_style(base: float = 8.0) -> None:
    """Set global rcParams for print. Call once, before creating figures."""
    mpl.rcParams.update(
        {
            # fonts: 8 pt base at 3.5 in column width, 7 pt floor for ticks/captions
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
            "font.size": base,
            "axes.titlesize": base + 1,
            "axes.labelsize": base,
            "xtick.labelsize": base - 1,
            "ytick.labelsize": base - 1,
            "legend.fontsize": base - 1,
            "legend.title_fontsize": base - 1,
            # figure
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "figure.figsize": (3.5, 2.3),
            "figure.constrained_layout.use": False,
            # lines and markers
            "lines.linewidth": 1.2,
            "lines.markersize": 3.5,
            "lines.markeredgewidth": 0.8,
            "errorbar.capsize": 2.0,
            # axes: Tufte-lite — no top/right spines, light horizontal grid only
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.6,
            "axes.edgecolor": "#333333",
            "axes.labelcolor": "#111111",
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": "#DDDDDD",
            "grid.linewidth": 0.5,
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "xtick.major.size": 2.5,
            "ytick.major.size": 2.5,
            "xtick.color": "#333333",
            "ytick.color": "#333333",
            # legend: frameless by default; direct labels are better
            "legend.frameon": False,
            "legend.handlelength": 1.6,
            "legend.handletextpad": 0.5,
            "legend.labelspacing": 0.3,
            # output
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,   # embed TrueType, not Type 3 (venue requirement)
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def new_fig(width: float = 3.5, height: float = 2.3, nrows: int = 1, ncols: int = 1):
    """Figure at printed width, fixed cell size (avoids constrained-layout surprises)."""
    fig, axes = plt.subplots(
        nrows, ncols, figsize=(width, height), squeeze=False, sharex="none", sharey="none"
    )
    return fig, axes[0, 0] if nrows == 1 and ncols == 1 else axes


def save(fig: Figure, path: str | Path, formats: tuple[str, ...] = ("pdf", "png")) -> list[str]:
    """Write vector PDF (for LaTeX) + 300 dpi PNG (for preview). Returns written paths."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    written = []
    for fmt in formats:
        out = path.with_suffix("." + fmt)
        fig.savefig(out, format=fmt)
        written.append(str(out))
    plt.close(fig)
    return written


def panel_label(ax, label: str, x: float = -0.14, y: float = 1.06) -> None:
    """Bold panel label (A, B, C) at the top-left, outside the axes."""
    ax.text(
        x, y, label, transform=ax.transAxes,
        fontsize=8, fontweight="bold", va="top", ha="left",
    )


def annotate_end(ax, x, y, text: str, color: str = "#000000", dx: float = 4, **kw) -> None:
    """Direct label at the end of a line (replaces a legend box)."""
    ax.annotate(
        text, xy=(x, y), xytext=(dx, 0), textcoords="offset points",
        color=color, fontsize=7, va="center", ha="left", **kw
    )


def annotate_point(ax, x, y, text: str, color: str = "#000000",
                   dx: float = 6, dy: float = 6, **kw) -> None:
    """Label a point with a small offset and a leader if needed."""
    ax.annotate(
        text, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
        color=color, fontsize=7, va="bottom", ha="left",
        arrowprops=dict(arrowstyle="-", lw=0.5, color="#888888", shrinkA=0, shrinkB=2),
        **kw
    )


def despine_keep(ax, keep: tuple[str, ...] = ("left", "bottom")) -> None:
    for side in ("left", "right", "top", "bottom"):
        ax.spines[side].set_visible(side in keep)


def tight_limits(ax, xpad: float = 0.03, ypad: float = 0.06) -> None:
    """Add a little breathing room instead of touching the frame."""
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - (x1 - x0) * xpad, x1 + (x1 - x0) * xpad)
    ax.set_ylim(y0 - (y1 - y0) * ypad, y1 + (y1 - y0) * ypad)
