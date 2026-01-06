import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

df = pd.read_csv("data/healthcare_dataset.csv")

# Simulated follow-up (months)
df["time_to_event"] = df["Age"] * 0.5
df["event"] = (df["Diagnosis"] != "Healthy").astype(int)

kmf = KaplanMeierFitter()

plt.figure(figsize=(8, 6))  # create a figure

for disease in df["Diagnosis"].unique():
    subset = df[df["Diagnosis"] == disease]
    kmf.fit(subset["time_to_event"], subset["event"], label=disease)
    kmf.plot_survival_function()

plt.title("Kaplan–Meier Survival Curves")
plt.xlabel("Time (months)")
plt.ylabel("Survival Probability")


plt.savefig("kaplan_meier_survival_curves.png", dpi=300, bbox_inches="tight")

plt.show()

print("Kaplan–Meier survival curves generated and saved.")
