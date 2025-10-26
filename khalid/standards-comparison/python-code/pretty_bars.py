import argparse, re
from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt

PALETTE = {"EU":"#1f77b4","US":"#d62728","SA":"#2ca02c"}
TITLE_MAP = {"EU":"EU AI Act (2024)","US":"US EO 14110 (2023)","SA":"SDAIA (2023–2025)"}

def normalize_columns(df):
    m={}
    for c in df.columns:
        s=c.strip().lower()
        if s in ("metric","metrics"): m[c]="Metric"
        elif "eu" in s: m[c]="EU"
        elif "us" in s or "eo" in s: m[c]="US"
        elif "sa" in s or "sdaia" in s or "saudi" in s: m[c]="SA"
        else: m[c]=c
    return df.rename(columns=m)

def load_data(csv_path: Path):
    df=pd.read_csv(csv_path)
    if "Metric" in df.columns[0]:
        df=df.set_index("Metric").T.reset_index().rename(columns={"index":"Metric"})
    df=normalize_columns(df)
    if "Metric" not in df.columns:
        df=df.rename(columns={df.columns[0]:"Metric"})
    metrics=df["Metric"].tolist()
    series={fw:df[fw].astype(float).tolist() for fw in ["EU","US","SA"] if fw in df.columns}
    return metrics,series

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input","-i",required=True)
    p.add_argument("--out","-o",default=None)
    p.add_argument("--name","-n",default="bars_comparison")
    args=p.parse_args()

    csv=Path(args.input).resolve()
    outdir=Path(args.out).resolve() if args.out else csv.parent.parent/"figures"
    outdir.mkdir(parents=True,exist_ok=True)

    metrics,series=load_data(csv)
    frameworks=list(series.keys())
    x=np.arange(len(metrics))
    width=0.25

    plt.rcParams.update({"font.size":12})
    fig,ax=plt.subplots(figsize=(10,6))
    for i,fw in enumerate(frameworks):
        ax.bar(x+i*width, series[fw], width, label=TITLE_MAP[fw], color=PALETTE[fw])

    ax.set_xticks(x+width)
    ax.set_xticklabels(metrics, rotation=30, ha="right")
    ax.set_ylim(0,5)
    ax.set_yticks([1,2,3,4,5])
    ax.set_ylabel("Score")
    ax.set_title("Metric-by-Metric Comparison", fontsize=15, fontweight="bold")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5,-0.3), ncol=3, frameon=False)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    for ext in ("png","pdf"):
        fig.savefig(outdir/f"{args.name}.{ext}", dpi=400, bbox_inches="tight")
    print(f"Saved bars: {outdir/(args.name+'.png')}")

if __name__=="__main__":
    main()
