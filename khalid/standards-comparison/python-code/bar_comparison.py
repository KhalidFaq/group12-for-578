# bar_comparison.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ----- Paths (robust, relative to this file) -----
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_PATH = ROOT / "data" / "standards.csv"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ----- Load data -----
df = pd.read_csv(DATA_PATH)

frameworks = df.iloc[:, 0].tolist()                 # first column = framework names
metrics = df.columns[1:].tolist()                   # remaining columns = metrics
metrics_clean = [m.replace("_", " & ") for m in metrics]
scores = df.iloc[:, 1:].to_numpy()                  # shape: (n_frameworks, n_metrics)

# ===== BAR CHART =====
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.25
x = np.arange(len(metrics))
colors = ['#2563eb', '#dc2626', '#16a34a']  # extend if you add more frameworks

bars = []
for idx, framework in enumerate(frameworks):
    bar = ax.bar(x + idx * bar_width, scores[idx], bar_width,
                 label=framework, color=colors[idx % len(colors)], alpha=0.85)
    bars.append(bar)

ax.set_xlabel('Metrics', fontsize=12, weight='bold')
ax.set_ylabel('Score (1-5)', fontsize=12, weight='bold')
ax.set_title('AI Framework Metric-by-Metric Comparison\n(Scale: 1-5, where 5 is highest)',
             fontsize=14, weight='bold', pad=20)
ax.set_xticks(x + (bar_width * (len(frameworks)-1) / 2))
ax.set_xticklabels(metrics_clean, rotation=45, ha='right', fontsize=10)
ax.set_ylim(0, 5.5)
ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_axisbelow(True)
ax.legend(loc='upper right', fontsize=10)

# value labels
for bar_group in bars:
    for bar in bar_group:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h,
                f'{h:.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
bar_path = FIG_DIR / "bar_comparison.png"
plt.savefig(bar_path, dpi=300, bbox_inches='tight')
print(f"Bar chart saved to: {bar_path}")

# ===== RADAR CHART =====
# angles for each metric
N = len(metrics)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# close the loop by repeating first point at the end
def closed(vals):
    return np.concatenate([vals, vals[:1]])

angles_closed = closed(angles)

fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(111, polar=True)

# plot each framework
for idx, framework in enumerate(frameworks):
    vals = scores[idx].astype(float)
    ax2.plot(angles_closed, closed(vals), linewidth=2,
             color=colors[idx % len(colors)], label=framework)
    ax2.fill(angles_closed, closed(vals), alpha=0.15,
             color=colors[idx % len(colors)])

# radial and theta formatting
ax2.set_ylim(0, 5.5)
ax2.set_yticks([1, 2, 3, 4, 5])
ax2.set_yticklabels([1, 2, 3, 4, 5], fontsize=10)
ax2.set_title('AI Framework Radar Comparison (1–5)', va='bottom', fontsize=14, weight='bold', pad=20)

# Put metric labels slightly outside the outer ring to avoid overlap
for angle, label in zip(angles, metrics_clean):
    # radius a bit beyond the max to push labels out
    ax2.text(angle, 5.8, label, ha='center', va='center', fontsize=10)

ax2.grid(alpha=0.5)
ax2.legend(loc='upper right', bbox_to_anchor=(1.25, 1.05), frameon=False)

radar_path = FIG_DIR / "radar_overlay.png"
plt.tight_layout()
plt.savefig(radar_path, dpi=300, bbox_inches='tight')
print(f"Radar chart saved to: {radar_path}")

# ===== SUMMARY =====
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)
for idx, framework in enumerate(frameworks):
    total = scores[idx].sum()
    average = scores[idx].mean()
    print(f"\n{framework}:")
    print(f"  Total Score: {int(total)}/50")
    print(f"  Average: {average:.2f}/5")
print("="*60)

# Optional: show plots interactively (comment out on headless runs)
plt.show()
