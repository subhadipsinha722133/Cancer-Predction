import pandas as pd

a = pd.read_csv(
    "The_Cancer_data_1500_V2.csv"
)

a.info()
a.drop(columns="Gender",inplace=True)
x = a.iloc[:, :-1]
y = a.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.2
)

from sklearn.preprocessing import StandardScaler

st = StandardScaler()
x_train = st.fit_transform(x_train)
x_test = st.transform(x_test)

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import plot_tree

dec = DecisionTreeClassifier(max_depth=44, criterion="log_loss")
dec.fit(x_train, y_train)

print()
print(dec.score(x_test, y_test))


b = plot_tree(dec)
print(b)


import streamlit as st

st.title("Cancer Prediction Web App")
st.write(
    "This is a simple web app to predict Cancer based on symptoms and demographics"
)

st.sidebar.title("Input Features")
Age = st.sidebar.slider(
    "Age",
    int(a["Age"].min()),
    int(a["Age"].max()),
)


BMI = st.sidebar.slider(
    "BMI",
    float(a["BMI"].min()),
    float(a["BMI"].max()),
)
Smoking = st.sidebar.slider(
    "Smoking",
    float(a["Smoking"].min()),
    float(a["Smoking"].max()),
)

GeneticRisk = st.sidebar.slider(
    "GeneticRisk",
    float(a["GeneticRisk"].min()),
    float(a["GeneticRisk"].max()),
)
PhysicalActivity = st.sidebar.slider(
    "PhysicalActivity",
    float(a["PhysicalActivity"].min()),
    float(a["PhysicalActivity"].max()),
)
AlcoholIntake = st.sidebar.slider(
    "AlcoholIntake",
    float(a["AlcoholIntake"].min()),
    float(a["AlcoholIntake"].max()),
)
CancerHistory = st.sidebar.slider(
    "CancerHistory ",
    float(a["CancerHistory"].min()),
    float(a["CancerHistory"].max()),
)

input_data = [
    [
        Age,
        BMI,
        Smoking,
        GeneticRisk,
        PhysicalActivity,
        AlcoholIntake,
        CancerHistory,
    ]
]
prediction = dec.predict(input_data)
target_name = ["No Cancer", "Has Cancer "]
predicted_species = target_name[prediction[0]]


st.write("Prediction")
st.write(f"The predicted species is:====> {predicted_species}")

st.line_chart(a)
st.write(a)

