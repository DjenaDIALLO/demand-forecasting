"""Exploratory analysis of the Air Passengers dataset: trend and seasonality."""

# %%
from pathlib import Path

import matplotlib.pyplot as plt

from data_loader import load_air_passengers

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


def plot_time_series(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["passengers"])
    ax.set_title("Monthly Air Passengers (1949-1960)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Passengers (thousands)")
    fig.tight_layout()
    return fig


def plot_seasonality_boxplot(df):
    df = df.copy()
    df["month"] = df.index.month
    fig, ax = plt.subplots(figsize=(10, 5))
    df.boxplot(column="passengers", by="month", ax=ax)
    ax.set_title("Air Passengers by Month (Seasonality Check)")
    fig.suptitle("")
    ax.set_xlabel("Month (1=Jan, 12=Dec)")
    ax.set_ylabel("Number of Passengers (thousands)")
    fig.tight_layout()
    return fig


# %%
df = load_air_passengers()
df.head()

# %%
fig1 = plot_time_series(df)
plt.show()

# %%
fig1.savefig(f"{REPORTS_DIR}/air_passengers_timeseries.png")

# %%
fig2 = plot_seasonality_boxplot(df)
plt.show()

# %%
fig2.savefig(f"{REPORTS_DIR}/air_passengers_boxplot_by_month.png")
# %%
