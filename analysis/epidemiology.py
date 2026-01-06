import pandas as pd

df = pd.read_csv("data/healthcare_dataset.csv")

# Create age groups
df["age_group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 45, 60, 75, 100],
    labels=["<30", "30-45", "45-60", "60-75", "75+"]
)

# Disease prevalence by age group
prevalence = (
    df.groupby(["age_group", "Diagnosis"])
      .size()
      .reset_index(name="count")
)

total_by_age = df.groupby("age_group").size().reset_index(name="total")

prevalence = prevalence.merge(total_by_age, on="age_group")
prevalence["prevalence_pct"] = (
    prevalence["count"] / prevalence["total"] * 100
)

print(prevalence)
