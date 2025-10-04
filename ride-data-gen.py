import pandas as pd
import numpy as np

dates = pd.date_range("2025-10-01", "2025-10-03")
rows = []

for d in dates:
    for r in range(10):
        rows.append({
            "ds": str(d.date()),
            "ride_id": np.random.randint(1, 100000),
            "fare_cad": round(np.random.uniform(10, 75), 2),
            "pickup_time": pd.Timestamp(d) + pd.to_timedelta(np.random.randint(0, 1440), "m")
        })

df = pd.DataFrame(rows)
df.to_parquet(
    "hot/rides",
    partition_cols=["ds"],
    index=False
)