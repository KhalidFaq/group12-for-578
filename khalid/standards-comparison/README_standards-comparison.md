
# standards comparison (50%)

Here I focused on building and testing the complete framework for comparing different AI and cybersecurity standards. 
The goal was to get all the data, Python code, and figures working before adding the final scores and analysis.

###################################

# What Has Been Completed

* 1. **Data**
- **standards.csv** lists all the metrics for each standard (numbers still empty for now).
- **scoring_rubric.csv** explains how each metric is evaluated and benchmarked.

**2. Python Code**
- **analyze.py** reads the CSV files, processes the data, and produces analytical results.
- **radar.py** generates radar charts and other figures; it’s already tested with sample data and works successfully.

**3. Figures (Draft Examples)**
Several draft figures have been generated to confirm that it works correctly:
- `bar_overall_scores_draft.png`
- `heatmap_metric_correlations_draft.png`
- `leaderboard_per_metric.csv`
- `radar_EU_AI_Act_2024.png`, `radar_US_EO_14110_2023.png`, `radar_Saudi_SDAIA_2025.png`
- `summary_overall_scores.csv`

###################################

# Next Steps

- Fill in the final scoring numbers for each standard in `standards.csv`.
- Regenerate all figures and tables with real data.
- Write short explanations for each figure and finalize the comparative analysis.