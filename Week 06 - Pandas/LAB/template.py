"""
RECORD CHECK - completed IT lane mini-project
Run from this LAB folder: python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# LOAD: read the IT server data
df = pd.read_csv("mini_project_data.csv")

# PROCESS: calculate the percentage used
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# TYPICAL: classify each server
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# OUTPUT: print all rows and only the rows needing attention
print("All servers:")
print(df)

print("\nServers needing attention:")
print(df[df["status"] != "OK"])

# EXCELLENT: count statuses, save the full report, and chart the counts
print("\nCount by status:")
print(df["status"].value_counts())

df.to_csv("mini_project_report.csv", index=False)
df["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig("mini_project_status.png")
plt.close()

print("\nSaved mini_project_report.csv and mini_project_status.png")
