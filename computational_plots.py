"""
Computational Illustration: Heat Engines & Pollution
Course: Physics of Climate Change — TU Darmstadt
Author: Muhammad Zuhad

This script generates three publication-quality plots:
  1. Carnot efficiency vs. hot reservoir temperature
  2. Otto efficiency vs. compression ratio
  3. Bar chart of major pollutants from combustion engines
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Global style ────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.dpi": 150,
})

BLUE   = "#1565C0"
ORANGE = "#E65100"
GREEN  = "#2E7D32"
GRAY   = "#546E7A"

# ════════════════════════════════════════════════════════════════════════════
# PLOT 1 — Carnot Efficiency vs Hot Reservoir Temperature
# ════════════════════════════════════════════════════════════════════════════
# Physics:
#   η_Carnot = 1 − T_C / T_H
#   T_C = cold reservoir temperature (fixed, e.g. ambient = 300 K)
#   T_H = hot reservoir temperature (variable)
#
# Key insight: Higher T_H → higher efficiency, but always < 100%
# Real petrol engines: T_H ≈ 500–700 K → η ≈ 40–57% (ideal), ~25–35% (real)

T_C = 300          # Cold reservoir: ambient temperature (K)
T_H = np.linspace(301, 1500, 500)   # Hot reservoir range (K)

eta_carnot = 1 - T_C / T_H          # Carnot efficiency (fraction)

fig1, ax1 = plt.subplots(figsize=(7, 4.5))

ax1.plot(T_H, eta_carnot * 100, color=BLUE, linewidth=2.5, label="Carnot efficiency")

# Annotate real petrol engine operating range
ax1.axvspan(500, 700, alpha=0.12, color=ORANGE, label="Typical petrol engine T_H range")
ax1.axhline(y=(1 - T_C/600)*100, color=ORANGE, linestyle=":", linewidth=1.5)
ax1.annotate(
    f"At T_H=600 K: η ≈ {(1-T_C/600)*100:.0f}% (ideal)\nReal engine: ~25–35%",
    xy=(600, (1-T_C/600)*100),
    xytext=(750, 30),
    fontsize=9,
    color=ORANGE,
    arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2),
)

ax1.set_xlabel("Hot reservoir temperature T_H (K)", fontsize=11)
ax1.set_ylabel("Carnot efficiency η (%)", fontsize=11)
ax1.set_title("Carnot Efficiency vs Hot Reservoir Temperature\n(Cold reservoir T_C = 300 K fixed)", fontsize=12, fontweight="bold")
ax1.legend(fontsize=9)
ax1.set_xlim(300, 1500)
ax1.set_ylim(0, 100)

# One-line takeaway
ax1.text(0.5, -0.18, "Takeaway: Higher combustion temperature → higher theoretical efficiency, but real engines always fall short.",
         transform=ax1.transAxes, fontsize=9, ha="center", color=GRAY, style="italic")

fig1.tight_layout()
fig1.savefig("plot1_carnot_efficiency.png", bbox_inches="tight")
print("Saved: plot1_carnot_efficiency.png")


# ════════════════════════════════════════════════════════════════════════════
# PLOT 2 — Otto Efficiency vs Compression Ratio
# ════════════════════════════════════════════════════════════════════════════
# Physics:
#   η_Otto = 1 − 1 / r^(γ−1)
#   r  = compression ratio (dimensionless)
#   γ  = heat capacity ratio (Cp/Cv) ≈ 1.4 for diatomic gases (air)
#
# Key insight: Higher r → higher efficiency, but gains diminish (diminishing returns)
# Practical limit: too high r → engine knock (pre-ignition) — typically r = 8–12

gamma = 1.4
r = np.linspace(1.01, 20, 500)      # Compression ratio

eta_otto = 1 - 1 / (r ** (gamma - 1))   # Otto efficiency (fraction)

fig2, ax2 = plt.subplots(figsize=(7, 4.5))

ax2.plot(r, eta_otto * 100, color=BLUE, linewidth=2.5, label="Otto efficiency")

# Highlight practical range (r = 8 to 12 for petrol engines)
ax2.axvspan(8, 12, alpha=0.12, color=GREEN, label="Typical petrol engine range (r = 8–12)")
ax2.axvline(x=10, color=GREEN, linestyle=":", linewidth=1.5)
eta_at_10 = (1 - 1/10**(gamma-1)) * 100
ax2.annotate(
    f"r = 10 → η ≈ {eta_at_10:.0f}%",
    xy=(10, eta_at_10),
    xytext=(13, eta_at_10 - 10),
    fontsize=9,
    color=GREEN,
    arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2),
)

ax2.set_xlabel("Compression ratio r", fontsize=11)
ax2.set_ylabel("Otto efficiency η (%)", fontsize=11)
ax2.set_title("Otto Cycle Efficiency vs Compression Ratio\n(γ = 1.4, air as working fluid)", fontsize=12, fontweight="bold")
ax2.legend(fontsize=9)
ax2.set_xlim(1, 20)
ax2.set_ylim(0, 100)

ax2.text(0.5, -0.18, "Takeaway: Increasing compression ratio improves efficiency, but engine knock limits practical values to r ≈ 8–12.",
         transform=ax2.transAxes, fontsize=9, ha="center", color=GRAY, style="italic")

fig2.tight_layout()
fig2.savefig("plot2_otto_efficiency.png", bbox_inches="tight")
print("Saved: plot2_otto_efficiency.png")


# ════════════════════════════════════════════════════════════════════════════
# PLOT 3 — Major Pollutants from Combustion Engines (Global, approx. values)
# ════════════════════════════════════════════════════════════════════════════
# Approximate global annual emissions from road transport (Mt/year, IEA/EEA data)
# CO2: ~6,000 Mt; CO: ~500 Mt; NOx: ~40 Mt; SO2: ~5 Mt; HC (unburnt): ~30 Mt

pollutants   = ["CO₂", "CO", "NOₓ", "Unburnt HC", "SO₂"]
emissions_Mt = [6000,   500,   40,      30,           5  ]  # Million tonnes/year
colors_bar   = [ORANGE, BLUE, GREEN, GRAY, "#8D1A1A"]

fig3, ax3 = plt.subplots(figsize=(7, 4.5))

bars = ax3.bar(pollutants, emissions_Mt, color=colors_bar, width=0.55, edgecolor="white", linewidth=0.8)

# Value labels on bars
for bar, val in zip(bars, emissions_Mt):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 80,
             f"{val:,} Mt", ha="center", va="bottom", fontsize=9, fontweight="bold")

ax3.set_ylabel("Annual emissions (Million tonnes/year)", fontsize=11)
ax3.set_title("Major Pollutants from Global Road Transport\n(Approximate annual values)", fontsize=12, fontweight="bold")
ax3.set_ylim(0, 7000)

ax3.text(0.5, -0.18, "Takeaway: CO₂ dominates by volume; NOₓ and CO are smaller but highly toxic and directly affect air quality.",
         transform=ax3.transAxes, fontsize=9, ha="center", color=GRAY, style="italic")

fig3.tight_layout()
fig3.savefig("plot3_pollutants.png", bbox_inches="tight")
print("Saved: plot3_pollutants.png")

plt.show()
print("\nAll 3 plots generated successfully.")
