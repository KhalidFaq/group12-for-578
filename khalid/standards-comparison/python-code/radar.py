# Minimal radar/spider plot helper using matplotlib only
import numpy as np
import matplotlib.pyplot as plt

def radar_plot(metrics, values, title, outfile):
    # metrics: list[str], values: list[float]
    N = len(metrics)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values = values + values[:1]  # close the loop
    angles += angles[:1]

    fig = plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.set_thetagrids(np.degrees(angles[:-1]), metrics)
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.1)
    ax.set_title(title, y=1.08)
    ax.set_rlabel_position(0)
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(outfile, dpi=200, bbox_inches="tight")
    plt.close(fig)


# --- Example draft for testing only ---
import matplotlib.pyplot as plt
import numpy as np

# Example data for one standard
metrics = ['Transparency', 'Accountability', 'Privacy', 'Human Oversight', 'Fairness']
values = [3, 4, 2, 5, 4]  # sample/fake values (scale 1–5)

# Close the radar circle
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, linewidth=2, linestyle='solid', label='Sample Standard')
ax.fill(angles, values, alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics)
ax.set_title('Example Radar Draft (Test Only)')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Save the example draft figure
plt.savefig("figures/example_radar_test.png")
plt.close()
