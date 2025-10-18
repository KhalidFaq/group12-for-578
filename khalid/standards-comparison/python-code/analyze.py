#!/usr/bin/env python3
import argparse
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from radar import radar_plot

METRIC_COLUMNS = [
    "Human_Oversight","Transparency","Accountability","Privacy_Protection",
    "Security_Robustness","Risk_Management","Enforcement_Strength",
    "Fairness_And_Bias","Data_Quality","Monitoring_Audit"
]

def bar_overall_scores(df, outdir):
    # Mean score per framework
    scores = df.set_index("Framework")[METRIC_COLUMNS].mean(axis=1).sort_values(ascending=False)
    fig = plt.figure()
    ax = plt.subplot(111)
    scores.plot(kind="bar", ax=ax)
    ax.set_ylabel("Average Score (1–5)")
    ax.set_title("Overall Scores by Framework")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "bar_overall_scores.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

def correlation_heatmap(df, outdir):
    # Correlation across metrics (using all frameworks as rows)
    corr = df[METRIC_COLUMNS].corr()
    fig = plt.figure()
    ax = plt.subplot(111)
    cax = ax.imshow(corr.values, interpolation="nearest")
    ax.set_xticks(range(len(METRIC_COLUMNS)))
    ax.set_yticks(range(len(METRIC_COLUMNS)))
    ax.set_xticklabels(METRIC_COLUMNS, rotation=90)
    ax.set_yticklabels(METRIC_COLUMNS)
    ax.set_title("Metric Correlation Heatmap")
    fig.colorbar(cax)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "heatmap_metric_correlations.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

def per_framework_radar(df, outdir):
    for _, row in df.iterrows():
        framework = row["Framework"]
        values = [float(row[m]) for m in METRIC_COLUMNS]
        outfile = os.path.join(
            outdir,
            f"radar_{framework.replace(' ', '_').replace('(', '').replace(')', '').replace('–','-').replace('/','-')}.png"
        )
        radar_plot(METRIC_COLUMNS, values, framework, outfile)

def table_summary(df, outdir):
    # Save summary CSVs for the paper appendix
    means = df.set_index("Framework")[METRIC_COLUMNS].mean(axis=1)
    stds = df.set_index("Framework")[METRIC_COLUMNS].std(axis=1)
    summary = pd.DataFrame({"Mean": means, "StdDev": stds}).sort_values("Mean", ascending=False)
    summary.to_csv(os.path.join(outdir, "summary_overall_scores.csv"))
    # Per-metric leaderboard
    per_metric = []
    for m in METRIC_COLUMNS:
        top = df[["Framework", m]].sort_values(m, ascending=False).reset_index(drop=True)
        top["Metric"] = m
        per_metric.append(top)
    pm = pd.concat(per_metric, axis=0, ignore_index=True)
    pm.to_csv(os.path.join(outdir, "leaderboard_per_metric.csv"), index=False)

def main():
    parser = argparse.ArgumentParser(description="Analyze AI policy benchmarks and plot figures.")
    parser.add_argument("--input", required=True, help="Path to data CSV (frameworks × metrics).")
    parser.add_argument("--outdir", default="figures", help="Directory to save outputs.")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    df = pd.read_csv(args.input)

    # Basic validation
    missing = [c for c in METRIC_COLUMNS if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing columns in data: {missing}")

    bar_overall_scores(df, args.outdir)
    correlation_heatmap(df, args.outdir)
    per_framework_radar(df, args.outdir)
    table_summary(df, args.outdir)

    print(f"Done. Figures saved to: {os.path.abspath(args.outdir)}")

if __name__ == "__main__":
    main()


# --- DRAFT: bar chart of overall scores (sample values) ---
import os, matplotlib.pyplot as plt, numpy as np

os.makedirs("figures", exist_ok=True)

standards = ["EU_AI_Act", "US_EO_14110", "Saudi_SDAIA"]
overall = [3.8, 3.2, 3.5]   # sample placeholders (scale 1–5)

plt.figure(figsize=(7,4))
x = np.arange(len(standards))
plt.bar(x, overall)
plt.xticks(x, standards, rotation=15)
plt.ylabel("Overall score (1–5)")
plt.title("Draft Bar Chart — sample only")
plt.tight_layout()
plt.savefig("figures/bar_overall_scores_draft.png")
plt.close()


# --- DRAFT: heatmap of metric correlations (sample matrix) ---
import os, matplotlib.pyplot as plt, numpy as np

os.makedirs("figures", exist_ok=True)

metrics = ["Transparency", "Accountability", "Privacy", "Oversight", "Fairness"]
# symmetric 5x5 sample correlation matrix (-1..1). Diagonal = 1.
corr = np.array([
    [1.00, 0.55, 0.40, 0.35, 0.50],
    [0.55, 1.00, 0.45, 0.30, 0.60],
    [0.40, 0.45, 1.00, 0.25, 0.42],
    [0.35, 0.30, 0.25, 1.00, 0.33],
    [0.50, 0.60, 0.42, 0.33, 1.00],
])

plt.figure(figsize=(6,5))
plt.imshow(corr, vmin=-1, vmax=1)
plt.colorbar(label="Correlation")
plt.xticks(range(len(metrics)), metrics, rotation=30, ha="right")
plt.yticks(range(len(metrics)), metrics)
plt.title("Draft Heatmap — sample only")
plt.tight_layout()
plt.savefig("figures/heatmap_metric_correlations_draft.png")
plt.close()
