import argparse, re
from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt

PALETTE = {"EU":"#1f77b4","US":"#d62728","SA":"#2ca02c"}
TITLE_MAP = {"EU":"EU AI Act (2024)","US":"US EO 14110 (2023)","SA":"SDAIA (2023–2025)"}

def normalize_columns(df):
    m = {}
    for c in df.columns:
        s = c.strip().lower()
        if s in ("metric","metrics"): m[c]="Metric"
        elif "eu" in s: m[c]="EU"
        elif "us" in s or "eo" in s: m[c]="US"
        elif "sa" in s or "sdaia" in s or "saudi" in s: m[c]="SA"
        else: m[c]=c
    return df.rename(columns=m)

def load_data(csv_path: Path):
    df = pd.read_csv(csv_path)
    if "Metric" in df.columns[0]:  # frameworks as rows
        df = df.set_index("Metric").T.reset_index().rename(columns={"index":"Metric"})
    df = normalize_columns(df)
    if "Metric" not in df.columns:
        df = df.rename(columns={df.columns[0]:"Metric"})
    metrics = df["Metric"].tolist()
    series = {fw: df[fw].astype(float).tolist() for fw in ["EU","US","SA"] if fw in df.columns}
    return metrics, series

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input","-i",required=True)
    p.add_argument("--out","-o",default=None)
    p.add_argument("--name","-n",default="radar_overlay")
    args = p.parse_args()

    csv = Path(args.input).resolve()
    outdir = Path(args.out).resolve() if args.out else csv.parent.parent/"figures"
    outdir.mkdir(parents=True,exist_ok=True)

    metrics, series = load_data(csv)
    N = len(metrics)
    angles = np.linspace(0,2*np.pi,N,endpoint=False)

    plt.rcParams.update({"font.size":13})
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_offset(np.pi/2); ax.set_theta_direction(-1)
    ax.set_thetagrids(angles*180/np.pi, labels=metrics)
    ax.set_ylim(0,5); ax.set_yticks([1,2,3,4,5]); ax.set_yticklabels([1,2,3,4,5])
    ax.grid(True, linestyle="--", alpha=0.5)

    for fw,vals in series.items():
        color=PALETTE[fw]
        lab=TITLE_MAP[fw]
        v=np.r_[vals,vals[0]]; ang=np.r_[angles,angles[0]]
        ax.plot(ang,v,color=color,linewidth=2.4,label=lab)
        ax.fill(ang,v,color=color,alpha=0.18)

    ax.legend(loc="lower center", bbox_to_anchor=(0.5,-0.15), ncol=3, frameon=False)
    ax.set_title("AI Regulatory Framework Radar Comparison", pad=20, fontsize=15, fontweight="bold")

    for ext in ("png","pdf"):
        fig.savefig(outdir/f"{args.name}.{ext}", dpi=400, bbox_inches="tight")
    print(f"Saved radar: {outdir/(args.name+'.png')}")

if __name__=="__main__":
    main()

