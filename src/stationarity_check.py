import pandas as pd
from statsmodels.tsa.stattools import adfuller


df = pd.read_csv("data/air_passengers.csv")
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format='%Y-%B')
df = df.set_index('date')

# Run the Augmented Dickey-Fuller test on the raw series
result = adfuller(df['passengers'])

print("--- ADF Test: Raw series ---")
print(f"ADF Statistic: {result[0]:.4f}")
print(f"p-value: {result[1]:.4f}")
if result[1] < 0.05:
    print("=> Series is stationary")
else:
    print("=> Series is NOT stationary")