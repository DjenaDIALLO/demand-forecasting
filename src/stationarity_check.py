"""Stationarity checks for the Air Passengers series (Augmented Dickey-Fuller test)."""

# %%
from statsmodels.tsa.stattools import adfuller

from data_loader import load_air_passengers


def run_adf_test(series, label: str) -> None:
    result = adfuller(series)
    print(f"--- ADF Test: {label} ---")
    print(f"ADF Statistic: {result[0]:.4f}")
    print(f"p-value: {result[1]:.4f}")
    conclusion = "stationary" if result[1] < 0.05 else "NOT stationary"
    print(f"=> Series is {conclusion}\n")


# %%
df = load_air_passengers()

# %%
run_adf_test(df["passengers"], "Raw series")

# %%
# Seasonal differencing (period=12) to remove trend and seasonality
df["passengers_diff"] = df["passengers"].diff(12)
df_diff = df["passengers_diff"].dropna()

run_adf_test(df_diff, "Differenced series (seasonal, period=12)")

