"""Builds the two charts in /visuals from the CSV files in /data.

Run from the repository root:  python scripts/make_charts.py
Needs: pandas, matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

SURFACE, INK, INK_2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e6e5e1"
SPOTIFY, APPLE = "#2a78d6", "#eb6834"  # categorical slots 1 and 2 (colourblind-checked)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11, "text.color": INK,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK_2, "xtick.color": INK_2, "ytick.color": INK_2,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
})

prices = pd.read_csv("data/pricing.csv")
changes = pd.read_csv("data/india_price_changes.csv")
india = prices[prices.market == "India"].set_index(["service", "plan"]).monthly_price


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(length=0)


# ---------- Chart 1: India one-person price over time ----------
months = pd.period_range("2025-11", "2026-10", freq="M")
cut = changes[(changes.service == "Spotify") & (changes.change == "Standard price cut")].iloc[0]
hike = changes[(changes.service == "Apple Music") & (changes.change == "Individual price increase")].iloc[0]
cut_m = pd.Period(cut.date_reported, "M")
hike_m = pd.Period(hike.date_reported, "M")
spotify = [cut.old_monthly_price_inr if m < cut_m else cut.new_monthly_price_inr for m in months]
apple = [hike.old_monthly_price_inr if m < hike_m else hike.new_monthly_price_inr for m in months]
x = range(len(months))

fig, ax = plt.subplots(figsize=(9, 5.2), dpi=200)
style(ax)
ax.grid(axis="y", color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.step(x, spotify, where="post", color=SPOTIFY, linewidth=2.2, label="Spotify Premium Standard")
ax.step(x, apple, where="post", color=APPLE, linewidth=2.2, label="Apple Music Individual")
i_cut, i_hike = months.get_loc(cut_m), months.get_loc(hike_m)
ax.plot([i_cut], [cut.new_monthly_price_inr], "o", ms=8, color=SPOTIFY, mec=SURFACE, mew=2)
ax.plot([i_hike], [hike.new_monthly_price_inr], "o", ms=8, color=APPLE, mec=SURFACE, mew=2)
ax.annotate(f"May 2026: Spotify cuts ₹{cut.old_monthly_price_inr:.0f} → ₹{cut.new_monthly_price_inr:.0f}",
            (i_cut, cut.new_monthly_price_inr), xytext=(i_cut - 0.2, 165), color=INK_2, fontsize=10, ha="right")
ax.annotate(f"Jul 2026: Apple raises ₹{hike.old_monthly_price_inr:.0f} → ₹{hike.new_monthly_price_inr:.0f}",
            (i_hike, hike.new_monthly_price_inr), xytext=(i_hike - 0.2, 98), color=INK_2, fontsize=10, ha="right")
ax.text(len(months) - 1, 150, "Both ₹139", color=INK, fontsize=10.5, weight="bold", ha="right")
ax.set_xticks(list(x))
ax.set_xticklabels([m.strftime("%b\n%Y") if m.month in (1, 11) else m.strftime("%b") for m in months])
ax.set_ylim(0, 230)
ax.set_yticks([0, 50, 100, 150, 200])
ax.set_yticklabels([f"₹{v}" for v in [0, 50, 100, 150, 200]])
ax.legend(loc="lower left", frameon=False, fontsize=10, labelcolor=INK_2)
fig.text(0.03, 0.95, "In India, Spotify and Apple Music now cost the same for one person", fontsize=14,
         weight="bold", color=INK)
fig.text(0.03, 0.905, "Monthly list price for new subscribers, Nov 2025 – Oct 2026", fontsize=11, color=INK_2)
fig.text(0.03, 0.02, "Sources: MediaNama (May 2026), Republic World (Jul 2026), spotify.com and apple.com "
         "(checked 9 Oct 2026). Data: data/india_price_changes.csv", fontsize=8.5, color=MUTED)
fig.subplots_adjust(left=0.08, right=0.97, top=0.84, bottom=0.17)
fig.savefig("visuals/india_one_person_price.png")
plt.close(fig)


# ---------- Chart 2: India plans side by side (Oct 2026) ----------
groups = [
    ("Student", ("Spotify", "Premium Student"), ("Apple Music", "Student")),
    ("One person", ("Spotify", "Premium Standard"), ("Apple Music", "Individual")),
    ("Largest group plan", ("Spotify", "Premium Platinum"), ("Apple Music", "Family")),
]
acc = prices[prices.market == "India"].set_index(["service", "plan"]).max_accounts

fig, ax = plt.subplots(figsize=(9, 5.2), dpi=200)
style(ax)
ax.grid(axis="x", color=GRID, linewidth=1)
ax.set_axisbelow(True)
h = 0.36
for gi, (name, s_key, a_key) in enumerate(groups):
    y = len(groups) - 1 - gi
    for off, key, colr in ((h / 2 + 0.02, s_key, SPOTIFY), (-h / 2 - 0.02, a_key, APPLE)):
        price, people = india[key], acc[key]
        ax.barh(y + off, price, height=h, color=colr, edgecolor=SURFACE, linewidth=2)
        label = f"₹{price:.0f}  {key[1].replace('Premium ', '')}"
        if people > 1:
            label += f" · up to {people} people (₹{price / people:.0f} each)"
        ax.text(price + 4, y + off, label, va="center", fontsize=9.5, color=INK_2)
ax.set_yticks(range(len(groups)))
ax.set_yticklabels([g[0] for g in reversed(groups)], fontsize=11, color=INK)
ax.set_xlim(0, 600)
ax.set_xticks([0, 100, 200, 300])
ax.set_xticklabels(["₹0", "₹100", "₹200", "₹300"])
ax.legend(handles=[Line2D([], [], color=SPOTIFY, lw=8, label="Spotify"),
                   Line2D([], [], color=APPLE, lw=8, label="Apple Music")],
          loc="upper right", frameon=False, fontsize=10, labelcolor=INK_2)
fig.text(0.03, 0.95, "Single plans match; group plans don't", fontsize=14, weight="bold", color=INK)
fig.text(0.03, 0.905, "Monthly price in India for new subscribers, October 2026", fontsize=11, color=INK_2)
fig.text(0.03, 0.02, "Sources: spotify.com/in-en/premium and apple.com/in/apple-music (checked 9 Oct 2026). "
         "Data: data/pricing.csv", fontsize=8.5, color=MUTED)
fig.subplots_adjust(left=0.2, right=0.97, top=0.84, bottom=0.13)
fig.savefig("visuals/india_plans_compared.png")
plt.close(fig)
print("Charts written to visuals/")
