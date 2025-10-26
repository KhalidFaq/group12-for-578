# Standards Comparison (Final Summary)

This part compares how **the European Union (EU)**, **the United States (US)**, and **Saudi Arabia (SDAIA)** regulate Artificial Intelligence.  
It’s designed to simplify complex legal texts into clear insights through tables, explanations, and visual charts.

---

## Updated Comparison Table (Final Scores)

| **Metric** | **EU AI Act (2024)** | **US EO 14110 (2023)** | **SDAIA (2023)** | **Main Legal Sources** | **Simple Explanation** |
|-------------|:-------------------:|:----------------------:|:----------------:|------------------------|------------------------|
| **Human Oversight** | **5** | **4** | **4** | EU: Art. 14 • US: Sec 2(c), Sec 8(b) • SA: Principle 3 | EU mandates human control in high-risk AI; US promotes oversight but keeps it flexible; SDAIA embeds it as an ethical principle. |
| **Transparency** | **5** | **4** | **4** | EU: Art. 50 • US: Sec 4.2 & 8(a) • SA: Principle 6 | EU enforces disclosure of AI use; US encourages transparency; SDAIA includes explainability in ethics. |
| **Accountability** | **4** | **4** | **4** | EU: Art. 26 & 27 • US: Sec 7.1 & 10 • SA: Principle 7 | All stress accountability, but the EU has stricter governance rules for deployers. |
| **Privacy Protection** | **5** | **4** | **4** | EU: Art. 10 • US: Sec 9 • SA: Principle 2 + PDPL 2023 | EU ties privacy to GDPR; US and Saudi apply data-protection frameworks. |
| **Security & Robustness** | **5** | **5** | **4** | EU: Art. 15 • US: Sec 4.1 (NIST) • SA: Principles 2 & 5 | EU and US have strong cybersecurity requirements; Saudi ensures reliability and safety. |
| **Risk Management** | **5** | **4** | **4** | EU: Art. 6 & 9 • US: Sec 4.1 + AI RMF • SA: AI Adoption § 3 | EU uses a four-tier risk system; US aligns with NIST; SDAIA builds similar guidance. |
| **Enforcement Strength** | **5** | **3** | **3** | EU: Art. 99 • US: Sec 7.1 & 10.1(b)(ix) • SA: PDPL + voluntary compliance | EU enforces heavy penalties; US and Saudi rely on agency or voluntary systems. |
| **Fairness & Bias** | **4** | **4** | **4** | EU: Art. 10 • US: Sec 2(d), Sec 7 • SA: Principle 1 | All promote fairness; EU and US apply bias testing; Saudi focuses on ethical integrity. |
| **Data Quality** | **4** | **4** | **4** | EU: Art. 10(2-4) • US: Sec 4.1(B) • SA: Principle 9 | All ensure training data is reliable and representative, with varying enforcement. |
| **Monitoring & Audit** | **5** | **4** | **4** | EU: Art. 72 • US: Sec 4.3 & 8(b) • SA: Principle 10 | EU mandates continuous monitoring; US uses federal audits; SDAIA includes compliance checks. |

---

## What the Scores Mean

| Score | Meaning |
|-------|----------|
| **5** | Legally binding, strong enforcement |
| **4** | Comprehensive with clear standards |
| **3** | Principle-based, moderate enforcement |
| **2** | Limited regulation |
| **1** | No formal oversight |

---

## Visual Outputs

This project generates multiple visuals using Python (Matplotlib & Pandas):

| Chart | Description | Output File |
|--------|--------------|-------------|
| **Bar Chart** | Metric-by-metric comparison | `figures/bar_comparison.png` |
| **Radar Overlay** | Unified radar for all frameworks | `figures/radar_overlay.png` |
| **Individual Radars** | One radar per framework | `figures/radar_eu_ai_act.png`, `radar_us_14110.png`, `radar_sdaia.png` |

Each visualization illustrates how each framework performs across the ten governance metrics.

---

## How to Run

```bash
cd khalid/standards-comparison/python-code
python bar_comparison.py
python radar_comparison.py
python radar_per_framework.py
