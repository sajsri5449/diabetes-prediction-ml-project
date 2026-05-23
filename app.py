import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load dataset
diabetes_dataset = pd.read_csv("diabetes.csv")

# Split features and labels
X = diabetes_dataset.drop(columns='Outcome')
Y = diabetes_dataset['Outcome']

# Standardize data
scaler = StandardScaler()
scaler.fit(X)

X = scaler.transform(X)

# Train test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    stratify=Y,
    random_state=2
)

# Train model
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Accuracy
X_test_prediction = classifier.predict(X_test)
test_accuracy = accuracy_score(X_test_prediction, Y_test)

# Streamlit page title
st.title("🩺 Diabetes Prediction Web App")

st.write("Enter patient details below:")

# Show model accuracy
st.write(f"Model Accuracy: {test_accuracy*100:.2f}%")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0.0)
glucose = st.number_input("Glucose Level", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin Level", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0.0)

# Prediction button
if st.button("Predict"):

    input_data = np.array([
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]).reshape(1, -1)

    # Standardize input
    std_data = scaler.transform(input_data)

    # Prediction
    prediction = classifier.predict(std_data)

    # Result
    if prediction[0] == 0:
        st.success("✅ The person is NOT diabetic")
    else:
        st.error("⚠️ The person is diabetic")