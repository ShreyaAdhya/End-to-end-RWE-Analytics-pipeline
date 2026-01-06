import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

df = pd.read_csv("data/healthcare_dataset.csv")

# Binary outcome example
df["disease_flag"] = (df["Diagnosis"] != "Healthy").astype(int)

features = ["Age", "BMI", "Blood_Pressure", "Heart_Rate", "Cholesterol_Level"]
X = df[features]
y = df["disease_flag"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(classification_report(y_test, preds))

