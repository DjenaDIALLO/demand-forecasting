import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/air_passengers.csv")
print(df.head()) 
print(df.info())

#Build a date column from year + month, which will become the index
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format = '%Y-%B')
df = df.set_index('date')
print(df.head())

#plot the time series
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['passengers'])
plt.title("Monthly Air Passengers (1949-1960)")
plt.xlabel("Date")
plt.ylabel("Number of Passengers (thousands)")
plt.tight_layout()
plt.savefig("reports/air_passengers_timeseries.png")
plt.show()

# Boxplot by month to clearly visualize seasonality)
df['month_num'] = df.index.month  # extract the month number (1 to 12) from the date

plt.figure(figsize=(10, 5))
df.boxplot(column='passengers', by='month_num')
plt.title("Air Passengers by Month (Seasonality Check)")
plt.suptitle("")  
plt.xlabel("Month (1=Jan, 12=Dec)")
plt.ylabel("Number of Passengers (thousands)")
plt.tight_layout()
plt.savefig("reports/air_passengers_boxplot_by_month.png")
plt.show()

# --- Summary: Exploratory Data Analysis (EDA)---
# Exploratory analysis of the Air Passengers dataset (1949-1960) reveals three
# defining characteristics of the time series: a continuous upward trend in air
# traffic over the period, a marked annual seasonality with recurring peaks in
# summer (July-August) and troughs in winter confirmed month by month across
# all 12 years and a growing seasonal amplitude over time suggesting
# multiplicative rather than additive seasonality. These observations guide
# the choice of a SARIMA model capable of capturing both the trend and
# seasonal components.
