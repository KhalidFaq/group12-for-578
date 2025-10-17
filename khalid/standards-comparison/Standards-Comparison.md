# Standards Comparison (Group 12)

This repository contains the **implementation** for our ITMS-578 research project.  
I operationalize a set of **benchmarks (metrics)** derived from widely used AI governance sources (NIST AI RMF, OECD AI Principles, ISO/IEC 42001 themes) and **compare** three policy frameworks:

- EU AI Act (2024)
- U.S. Executive Order 14110 (2023)
- Saudi SDAIA AI Guidelines (2023–2025)

The code transforms qualitative policy analysis into **structured, reproducible metrics**, computes **statistics**, and outputs **visualizations** (bar charts, radar-style spokes, and a correlation heatmap).

---

## Structure

```
standards-comparison/
├─ data/
│  ├─ standards.csv                # Our dataset of frameworks × metrics (editable)
│  └─ scoring_rubric.md            # How we mapped text → numeric scores (1–5)
├─ src/
│  ├─ analyze.py                   # CLI: loads data, computes stats, saves plots
│  └─ radar.py                     # Helper for making radar/spider plots (matplotlib)
├─ figures/                        # Output charts saved here
├─ requirements.txt                # Python deps (minimal)
└─ Standards.md                       # You are here
```

> **Note**: Scores (1–5) are **just an initial draft** to demonstrate the pipeline. Replace with your finalized ratings after your group finishes the document analysis.

---

## Metrics (Benchmarks)

I compare each framework on the following **metrics (1–5)**. These are derived from common governance themes across NIST/OECD/ISO. Adjust as needed:

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



### Run the analysis

```bash
python src/analyze.py --input data/standards.csv --outdir figures
```

Outputs (saved in `figures/`):
- `bar_overall_scores.png`
- `heatmap_metric_correlations.png`
- `radar_EU_AI_Act_2024.png`, `radar_US_EO_14110_2023.png`, `radar_Saudi_SDAIA_2023_2025.png`

---

## How We Scored (Workflow Draft)

1. Read policy text and **extract evidence** per metric (quotes/sections).
2. Map evidence to a **score 1–5** using the rubric.
3. Double-review scores (two group members) to reduce subjectivity.
4. Record traceability: **framework → metric → evidence → score**.
5. Re-run `analyze.py` to regenerate figures for the paper.

---

# 📊 Scoring Justification Table — AI Regulation Benchmark

This table provides transparent justification for the **metric scores** assigned to each AI regulatory framework — namely:

- **EU Artificial Intelligence Act (2024)**
- **U.S. Executive Order 14110 (2023)**
- **Saudi SDAIA AI Framework (2023–2025)**

The scores (1–5) were derived through a structured **text-based analysis** of each document. Each metric maps to a legal article or policy clause, with qualitative interpretation of its **strength, enforcement clarity, and ethical alignment**.

---

| **Metric** | **EU AI Act (2024)** | **US EO 14110 (2023)** | **Saudi SDAIA (2023–25)** | **Legal / Text Evidence** | **Explanation (Why this score?)** |
|-------------|---------------------|--------------------------|-----------------------------|----------------------------|-----------------------------------|
| Human Oversight | 5 | 4 | 3 | EU Art. 14; EO § 4(d); SDAIA Principle #3 | EU mandates human-in-loop for high-risk AI. US encourages oversight but voluntary; Saudi mentions it without strict enforcement. |
| Transparency | 4 | 3 | 3 | EU Art. 52; EO § 8(a); SDAIA Principle #2 | EU requires disclosure and explainability. US promotes transparency but leaves implementation flexible. Saudi encourages but lacks legal force. |
| Accountability | 5 | 4 | 3 | EU Art. 71; EO § 10(b); SDAIA Framework §3 | EU assigns liability for misuse. US delegates to agencies. Saudi assigns moral accountability. |
| Privacy Protection | 5 | 4 | 4 | GDPR; EO § 9; SDAIA AI § 2.3 | EU links AI rules directly to GDPR. US references privacy laws; Saudi enforces national data laws. |
| Security & Robustness | 4 | 5 | 4 | EU Annex IV; EO § 4(b); SDAIA AI § 3.1 | EU enforces testing tiers; US promotes cybersecurity best practices; Saudi applies resilience standards. |
| Risk Management | 5 | 4 | 4 | EU Art. 6; EO § 5; SDAIA AI § 4.1 | EU uses proportional risk tiers. US introduces NIST risk controls. Saudi defines AI risk taxonomy. |
| Enforcement Strength | 5 | 3 | 3 | EU Art. 99; EO § 10; SDAIA AI § 5.2 | EU allows penalties up to 6% turnover. US limited to administrative actions. Saudi compliance is advisory. |
| Fairness & Bias | 4 | 4 | 3 | EU Annex IV (2); EO § 7(c); SDAIA AI § 3.2 | EU mandates bias testing. US encourages fairness principles. Saudi references ethics but no binding test. |
| Data Quality | 4 | 4 | 4 | EU Annex IV (3); NIST RMF § 2.3; SDAIA AI § 3.3 | All ensure dataset quality; EU has audit protocols. |
| Monitoring & Audit | 4 | 4 | 4 | EU Art. 61; EO § 8(b); SDAIA AI § 5.4 | EU requires post-market monitoring. US builds AI Safety Institute. Saudi establishes auditing committee. |

---

### 📘 References
- **EU Artificial Intelligence Act (2024)** — Regulation (EU) 2024/1689. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)  
- **U.S. Executive Order 14110 (2023)** — The White House. [Link](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)  
- **Saudi SDAIA AI Ethics Framework (2023–2025)** — [SDAIA AI Ethics](https://ai.sa/AI-Ethics)  
- **OECD AI Principles (2019)** — [OECD Principles](https://oecd.ai/en/ai-principles)  
- **NIST AI Risk Management Framework (2023)** — [NIST RMF](https://www.nist.gov/itl/ai-risk-management-framework)

---

### 🔍 How to Interpret Scores and Figures
Each metric is **scored from 1–5** based on **evidence strength and enforcement depth**:
- 5️⃣ = Legally binding and detailed enforcement mechanisms  
- 4️⃣ = Strong policy guidance or delegated enforcement  
- 3️⃣ = Ethical or advisory principles only  
- 2️⃣ = Minimal reference, weak enforcement  
- 1️⃣ = No coverage or unclear policy

These values were visualized using **radar charts**, **bar graphs**, and **heatmaps** located in:
```
/khalid/standards-comparison/figures/
```
Each figure corresponds to how each framework performs across all 10 ethical and regulatory metrics.