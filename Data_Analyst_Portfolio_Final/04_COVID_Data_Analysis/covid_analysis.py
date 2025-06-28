
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": pd.date_range(start="2023-01-01", periods=10),
    "Cases": [10, 12, 20, 25, 18, 30, 35, 40, 38, 33],
}
df = pd.DataFrame(data)

df["7d_avg"] = df["Cases"].rolling(window=3).mean()

plt.plot(df["Date"], df["Cases"], label="Daily Cases")
plt.plot(df["Date"], df["7d_avg"], label="7-Day Avg", linestyle="--")
plt.legend()
plt.title("COVID-19 Daily Cases")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.grid()
plt.tight_layout()
plt.show()
