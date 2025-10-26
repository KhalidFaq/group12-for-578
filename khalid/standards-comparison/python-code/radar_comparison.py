import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ---------- Paths (robust, relative to this file) ----------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_PATH = ROOT / "data" / "standards.csv"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = FIG_DIR / "radar_comparison.png"

# ---------- Load data ----------
df = pd.read_csv(DATA_PATH)

frameworks = df.iloc[:, 0].tolist()                      # first column: framework names
metrics = df.columns[1:].tolist()                        # other columns: metrics
metrics_clean = [m.replace("_", " & ") for m in metrics]

# ensure numeric (avoids issues if CSV has stray text)
scores = df.iloc[:, 1:].apply(pd.to_numeric, errors="coerce").to_numpy()

# ---------- Radar setup ----------
N = len(metrics)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

def closed(arr):
    return np.concatenate([arr, arr[:1]])

angles_closed = closed(angles)

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ["#2563eb", "#dc2626", "#16a34a"]

# plot each framework
for i, fw in enumerate(frameworks):
    vals = scores[i].astype(float)
    ax.plot(angles_closed, closed(vals), linewidth=2,
            color=colors[i % len(colors)], label=fw)
    ax.fill(angles_closed, closed(vals), alpha=0.20,
            color=colors[i % len(colors)])

# styling
ax.set_ylim(0, 5.5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels([1, 2, 3, 4, 5], fontsize=10)
ax.grid(alpha=0.5)
ax.set_title("AI Framework Overall Comparison - Radar View\n(Scale: 1-5, where 5 is highest)",
             fontsize=14, weight="bold", pad=20)

# place metric labels slightly outside the ring to avoid overlap
# (hide default theta tick labels)
ax.set_xticks([])
for ang, lab in zip(angles, metrics_clean):
    ax.text(ang, 5.8, lab, ha="center", va="center", fontsize=10)

ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.05), fontsize=10, frameon=False)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=300, bbox_inches="tight")
print(f"Radar chart saved to: {OUT_PATH}")

plt.show()
