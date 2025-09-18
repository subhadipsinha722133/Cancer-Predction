import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load the data
a = pd.read_csv("The_Cancer_data_1500_V2.csv")

# Data preprocessing
a.info()
a.drop(columns="Gender", inplace=True)

# Convert categorical columns to numeric if they're not already
categorical_cols = ['Smoking', 'GeneticRisk', 'CancerHistory']
label_encoders = {}

for col in categorical_cols:
    if a[col].dtype == 'object':
        le = LabelEncoder()
        a[col] = le.fit_transform(a[col])
        label_encoders[col] = le

# Prepare features and target
x = a.iloc[:, :-1]
y = a.iloc[:, -1]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.2
)

# Scale the features
st_scaler = StandardScaler()
x_train = st_scaler.fit_transform(x_train)
x_test = st_scaler.transform(x_test)

# Train the model
dec = DecisionTreeClassifier(max_depth=44, criterion="log_loss")
dec.fit(x_train, y_train)

print(f"Model accuracy: {dec.score(x_test, y_test)}")

# Streamlit app
st.title("Cancer Prediction Web App")
st.write(
    "This is a simple web app to predict Cancer based on symptoms and demographics"
)

st.sidebar.title("Input Features")

Age = st.sidebar.slider(
    "Age",
    int(a["Age"].min()),
    int(a["Age"].max()),
    int(a["Age"].mean())
)

BMI = st.sidebar.slider(
    "BMI",
    float(a["BMI"].min()),
    float(a["BMI"].max()),
    float(a["BMI"].mean())
)

# Create radio buttons for categorical features
Smoking = st.sidebar.radio("Smoking", ["No", "Yes"])
GeneticRisk = st.sidebar.radio("Genetic Risk", ["No", "Yes"])
CancerHistory = st.sidebar.radio("Cancer History", ["No", "Yes"])

PhysicalActivity = st.sidebar.slider(
    "Physical Activity",
    float(a["PhysicalActivity"].min()),
    float(a["PhysicalActivity"].max()),
    float(a["PhysicalActivity"].mean())
)

AlcoholIntake = st.sidebar.slider(
    "Alcohol Intake",
    float(a["AlcoholIntake"].min()),
    float(a["AlcoholIntake"].max()),
    float(a["AlcoholIntake"].mean())
)

# Convert categorical inputs to numerical values
smoking_val = 1 if Smoking == "Yes" else 0
genetic_risk_val = 1 if GeneticRisk == "Yes" else 0
cancer_history_val = 1 if CancerHistory == "Yes" else 0

input_data = [
    [
        Age,
        BMI,
        smoking_val,
        genetic_risk_val,
        PhysicalActivity,
        AlcoholIntake,
        cancer_history_val,
    ]
]

# Scale the input data
input_data_scaled = st_scaler.transform(input_data)

# Make prediction
prediction = dec.predict(input_data_scaled)
target_name = ["No Cancer", "Has Cancer"]
predicted_species = target_name[prediction[0]]

st.write("## Prediction")
st.write(f"### The prediction is: {predicted_species}")

# Display some data visualizations
st.write("## Data Overview")
st.line_chart(a.select_dtypes(include='number').iloc[:, :5])  # Show first 5 numeric columns
st.write(a)

# Show feature importance
st.write("## Feature Importance")
feature_importance = pd.DataFrame({
    'feature': x.columns,
    'importance': dec.feature_importances_
}).sort_values('importance', ascending=False)

st.bar_chart(feature_importance.set_index('feature'))
