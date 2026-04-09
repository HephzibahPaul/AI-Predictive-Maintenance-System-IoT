import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000
time = np.arange(rows)

temperature = 70 + 10*np.sin(time/20) + np.random.normal(0, 2, rows)
vibration = 3 + np.sin(time/15) + np.random.normal(0, 0.5, rows)
current = 10 + np.sin(time/25) + np.random.normal(0, 1, rows)

data = pd.DataFrame({
    "time": time,
    "temperature": temperature,
    "vibration": vibration,
    "current": current
})

data["failure"] = (
    (data["temperature"] > 85) |
    (data["vibration"] > 5) |
    (data["current"] > 15)
).astype(int)

data.to_csv("data/time_series_data.csv", index=False)
print("Dataset created!")