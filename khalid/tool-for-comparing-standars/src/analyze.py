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
