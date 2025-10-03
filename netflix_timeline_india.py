# ✅ Dependencies (install via pip if needed)
# pip install matplotlib

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------
# Timeline main points (the big dots)
# ---------------------------------------
tl_dates = [
    "1997\nFounded",
    "1998\nMail Service",
    "2003\nGoes Public",
    "2007\nStreaming service",
    "2016\nGoes Global",
    "2021\nNetflix & Chill"
]
tl_x = [1, 2, 4, 5.3, 8, 9]

# ---------------------------------------
# Timeline sub events (with labels)
# ---------------------------------------
tl_sub_x = [1.5, 3, 5, 6.5, 8]
tl_sub_times = ["1998", "2000", "2006", "2010", "2016"]
tl_text = [
    "Netflix.com launched",
    "Starts\nPersonal\nRecommendations",
    "Billionth DVD Delivery",
    "Canadian\nLaunch",
    "India Launch\n(my birthplace)"
]

# ---------------------------------------
# Plot Setup
# ---------------------------------------
fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
ax.set_ylim(-2, 1.75)
ax.set_xlim(0, 10)

# Timeline base line
ax.axhline(0, xmin=0.1, xmax=0.9, c='#4a4a4a', zorder=1)

# Major event points
ax.scatter(tl_x, np.zeros(len(tl_x)), s=120, c='#4a4a4a', zorder=2)
ax.scatter(tl_x, np.zeros(len(tl_x)), s=30, c='#fafafa', zorder=3)

# Minor event points
ax.scatter(tl_sub_x, np.zeros(len(tl_sub_x)), s=50, c='#4a4a4a', zorder=4)

# Date labels (bottom)
for x, date in zip(tl_x, tl_dates):
    ax.text(x, -0.55, date, ha='center',
            fontfamily='serif', fontweight='bold',
            color='#4a4a4a', fontsize=12)

# Stem plot vertical lines
levels = np.zeros(len(tl_sub_x))
levels[::2] = 0.3
levels[1::2] = -0.3
markerline, stemline, baseline = ax.stem(tl_sub_x, levels)
plt.setp(baseline, zorder=0)
plt.setp(markerline, marker=',', color='#4a4a4a')
plt.setp(stemline, color='#4a4a4a')

# Text annotations (alternating top/bottom)
for idx, x, time, txt in zip(range(1, len(tl_sub_x)+1), tl_sub_x, tl_sub_times, tl_text):
    ax.text(x, 1.3*(idx % 2) - 0.5, time, ha='center',
            fontfamily='serif', fontweight='bold',
            color='#b20710' if idx == len(tl_sub_x) else '#4a4a4a', fontsize=11)

    ax.text(x, 1.3*(idx % 2) - 0.6, txt, va='top', ha='center',
            fontfamily='serif',
            color='#b20710' if idx == len(tl_sub_x) else '#4a4a4a')

# Clean look
for spine in ["left", "top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

# Title
ax.set_title("Netflix through the years", fontweight="bold",
             fontfamily='serif', fontsize=16, color="#1e1d1d")
ax.text(2.4, 1.57, "From DVD rentals to a global audience of over 150m people – welcome to India, Netflix!", fontfamily='serif', fontsize=10, color='#4a4a4a')

# Save chart as PNG
plt.savefig("netflix_timeline_india_v3.png", dpi=300, bbox_inches='tight')

plt.show()
