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
