# AI Ethics in Cybersecurity — Policy Comparison (Group 12)

This repository contains the **implementation** for our ITMS-578 research project.  
We operationalize a set of **benchmarks (metrics)** derived from widely used AI governance sources (NIST AI RMF, OECD AI Principles, ISO/IEC 42001 themes) and **compare** three policy frameworks:

- EU AI Act (2024)
- U.S. Executive Order 14110 (2023)
- Saudi SDAIA AI Guidelines (2023–2025)

The code transforms qualitative policy analysis into **structured, reproducible metrics**, computes **statistics**, and outputs **visualizations** (bar charts, radar-style spokes, and a correlation heatmap).

---

## Repository Structure

```
ai-ethics-cybersecurity-group12/
├─ data/
│  ├─ standards.csv                # Our dataset of frameworks × metrics (editable)
│  └─ scoring_rubric.md            # How we mapped text → numeric scores (1–5)
├─ src/
│  ├─ analyze.py                   # CLI: loads data, computes stats, saves plots
│  └─ radar.py                     # Helper for making radar/spider plots (matplotlib)
├─ figures/                        # Output charts saved here
├─ requirements.txt                # Python deps (minimal)
└─ README.md                       # You are here
```

> **Note**: Scores (1–5) are **just an initial draft** to demonstrate the pipeline. Replace with your finalized ratings after your group finishes the document analysis.

---

## Metrics (Benchmarks)

We compare each framework on the following **metrics (1–5)**. These are derived from common governance themes across NIST/OECD/ISO. Adjust as needed:

1. **Human_Oversight** – explicit human-in-the-loop, override, and oversight mechanisms.
2. **Transparency** – documentation, disclosure, model cards, risk reporting.
3. **Accountability** – clear assignment of responsibilities, auditability, liability hooks.
4. **Privacy_Protection** – data governance, privacy-by-design, minimization, DPIA-like steps.
5. **Security_Robustness** – security controls, red-teaming, incident response.
6. **Risk_Management** – risk classification, impact assessment, mitigation cycles.
7. **Enforcement_Strength** – regulatory powers, penalties, conformity assessments.
8. **Fairness_And_Bias** – non-discrimination measures, bias testing and mitigation.
9. **Data_Quality** – dataset governance, provenance, quality thresholds.
10. **Monitoring_Audit** – monitoring in deployment, logging, auditing.

Scoring uses **1 (weak) → 5 (strong)**. See `data/scoring_rubric.md` for the mapping template.

---

## Quickstart

### 1) Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the analysis

```bash
python src/analyze.py --input data/standards.csv --outdir figures
```

Outputs (saved in `figures/`):
- `bar_overall_scores.png`
- `heatmap_metric_correlations.png`
- `radar_EU_AI_Act_2024.png`, `radar_US_EO_14110_2023.png`, `radar_Saudi_SDAIA_2023_2025.png`

### 3) Update the dataset

Open `data/standards.csv` and update the **scores** once your policy coding is finalized.

### 4) Reproducibility

- Keep all raw policy excerpts and your scoring justifications in the rubric file.
- Commit changes regularly and push to GitHub.

---

## How We Scored (Workflow Draft)

1. Read policy text and **extract evidence** per metric (quotes/sections).
2. Map evidence to a **score 1–5** using the rubric.
3. Double-review scores (two group members) to reduce subjectivity.
4. Record traceability: **framework → metric → evidence → score**.
5. Re-run `analyze.py` to regenerate figures for the paper.

---

## Citation Note

In the final paper, cite the original frameworks and any secondary guidance documents (NIST, OECD, ISO) in APA style. This repo focuses on the **implementation** (data + code).

---

## License

Educational use only. Replace with a group-selected license if needed.
