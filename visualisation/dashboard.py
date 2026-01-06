import streamlit as st
import pandas as pd

st.title("Healthcare RWE Analytics Dashboard")

df = pd.read_csv("data/healthcare_dataset.csv")

st.sidebar.header("Filters")
diagnosis = st.sidebar.selectbox(
    "Select Diagnosis",
    df["Diagnosis"].unique()
)

filtered = df[df["Diagnosis"] == diagnosis]

st.subheader("Cohort Summary")
st.write(filtered.describe())

st.subheader("Age Distribution")
st.bar_chart(filtered["Age"].value_counts().sort_index())

st.subheader("Risk Factor Overview")
st.write(
    filtered[["BMI", "Blood_Pressure", "Cholesterol_Level"]].mean()
)
