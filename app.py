import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the saved model (RandomForest)
rf_model = joblib.load('rfmodel.pkl')

# Load the dataset to preprocess and match user inputs
data = pd.read_csv('data.csv', delimiter=";")

# Preprocess data (similar to how it's done in your notebook)
numerical_columns = data.select_dtypes(include=[np.number]).columns
categorical_columns = data.select_dtypes(include=[object]).columns

# Fill missing values in numerical columns with their mean
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# For categorical columns, fill missing values with the mode (most frequent value)
for col in categorical_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# Encode the target variable 'Status' (Dropout and Graduate) as a numerical value
le = LabelEncoder()
data['Status'] = le.fit_transform(data['Status'])

# Title of the Streamlit App
st.title("Student Dropout Prediction")

# Display some helpful information
st.write("This app predicts whether a student will dropout, graduate, or remain enrolled based on their academic data.")

# Add input fields for the user to enter data
curricular_units_approved = st.number_input('Enter the number of Curricular Units Approved in 2nd Semester', min_value=0, max_value=100, value=0)
curricular_units_1st_sem_approved = st.number_input('Enter the number of Curricular Units Approved in 1st Semester', min_value=0, max_value=100, value=0)
admission_grade = st.number_input('Enter the Admission Grade', min_value=0, max_value=100, value=0)

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Curricular_units_2nd_sem_approved': [curricular_units_approved],
    'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
    'Admission_grade': [admission_grade]
})

# Make prediction using the trained Random Forest model
if st.button('Predict Status'):
    prediction = rf_model.predict(input_data)
    prediction_label = le.inverse_transform(prediction)[0]
    
    if prediction_label == 0:
        st.write("The student is likely to dropout.")
    elif prediction_label == 1:
        st.write("The student is likely to be enrolled.")
    else:
        st.write("The student is likely to graduate.")
