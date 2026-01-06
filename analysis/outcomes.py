import pandas as pd
from lifelines import KaplanMeierFitter

df = pd.read_csv("data/healthcare_dataset.csv")

# Simulated follow-up (months)
df["time_to_event"] = df["Age"] * 0.5
df["event"] = (df["Diagnosis"] != "Healthy").astype(int)

kmf = KaplanMeierFitter()

for disease in df["Diagnosis"].unique():
    subset = df[df["Diagnosis"] == disease]
    kmf.fit(subset["time_to_event"], subset["event"], label=disease)
    kmf.plot_survival_function()

print("Kaplan–Meier survival curves generated.")
