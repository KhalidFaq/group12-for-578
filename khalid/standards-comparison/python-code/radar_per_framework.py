# radar_per_framework.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import re

# ---------- Paths (robust, relative to this file) ----------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_PATH = ROOT / "data" / "standards.csv"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ---------- Load data ----------
df = pd.read_csv(DATA_PATH)

frameworks = df.iloc[:, 0].tolist()                      # first column: framework names
metrics = df.columns[1:].tolist()                        # other columns: metrics
metrics_clean = [m.replace("_", " & ") for m in metrics] # nicer labels

# ensure numeric (avoids issues if CSV has stray text)
scores = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce").to_numpy()

# ---------- Radar helpers ----------
def closed(arr):
    """Repeat first element at end to close the loop."""
    return np.concatenate([arr, arr[:1]])

def slugify(text: str) -> str:
    """Filesystem-friendly filename."""
    text = text.strip().lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")

# angles (same for all charts so they’re comparable)
N = len(metrics)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
angles_closed = closed(angles)

# ---------- Per-framework radar ----------
colors = ["#2563eb", "#dc2626", "#16a34a"]  # cycle if more frameworks

for i, fw in enumerate(frameworks):
    vals = scores[i].astype(float)
    vals_closed = closed(vals)

    fig, ax = plt.subplots(figsize=(9.5, 9.5), subplot_kw=dict(polar=True))

    # outline + fill
    ax.plot(angles_closed, vals_closed, linewidth=2.5, color=colors[i % len(colors)], label=fw)
    ax.fill(angles_closed, vals_closed, alpha=0.20, color=colors[i % len(colors)])

    # style
    ax.set_ylim(0, 5.5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels([1, 2, 3, 4, 5], fontsize=10)
    ax.grid(alpha=0.5)

    # title
    ax.set_title(
        f"{fw} — Radar of AI Metrics (1–5)",
        fontsize=14, weight="bold", pad=20
    )

    # put metric labels slightly outside the ring to avoid overlap
    ax.set_xticks([])  # hide default theta ticks
    for ang, lab in zip(angles, metrics_clean):
        ax.text(ang, 5.8, lab, ha="center", va="center", fontsize=10)

    # optional: annotate values at each vertex
    for ang, v in zip(angles, vals):
        ax.text(ang, v + 0.15, f"{v:.0f}", ha="center", va="bottom", fontsize=9)

    # legend (small, inside)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 1.02), frameon=False, fontsize=10)

    # save
    out_name = f"radar_{slugify(fw)}.png"
    out_path = FIG_DIR / out_name
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print(f"Saved: {out_path}")

    plt.close(fig)  # free memory