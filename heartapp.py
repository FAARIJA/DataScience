import streamlit as st
import pandas as pd
import joblib

# Load the trained model (heart_disease_model.pkl)
model = joblib.load('heart_disease_model.pkl')

# Title for the app
st.title("Heart Disease Prediction App (Intern ID- CC92627)")


# Input fields for health metrics
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', ('Male', 'Female'))
cp = st.selectbox('Chest Pain Type', (0, 1, 2, 3))  # Assume 0-3 represent different types of chest pain

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (1, 0))  # 1: true, 0: false
restecg = st.selectbox('Resting Electrocardiographic Results', (0, 1, 2))

thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=202, value=150)
exang = st.selectbox('Exercise Induced Angina (exang)', (1, 0))  # 1: yes, 0: no
oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=6.2, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', (0, 1, 2))
ca = st.number_input('Number of Major Vessels (0-4) Colored by Fluoroscopy', min_value=0, max_value=4, value=0)
thal = st.selectbox('Thalassemia', (0, 1, 2, 3))


# When the user clicks the "Predict" button
if st.button('Predict'):
    # Convert inputs to a DataFrame for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [1 if sex == 'Male' else 0],  # Convert 'Male' to 1 and 'Female' to 0
        'cp': [cp],
        'trtbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalachh': [thalach],
        'exng': [exang],
        'oldpeak': [oldpeak],
        'slp': [slope],
        'caa': [ca],
        'thall': [thal]
    })

    # Predict using the trained model
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.error("The model predicts you have a high risk of heart disease.")
    else:
        st.success("The model predicts you have a low risk of heart disease.")
