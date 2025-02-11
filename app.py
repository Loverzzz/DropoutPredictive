import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('data.csv', delimiter=";")

# Preprocess data
# Separate numerical columns and categorical columns
numerical_columns = data.select_dtypes(include=[np.number]).columns
categorical_columns = data.select_dtypes(include=[object]).columns

# Fill missing values in numerical columns with their mean
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# For categorical columns, we can either fill missing values with a placeholder or the mode (most frequent value)
for col in categorical_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# Check the missing values after filling
data.isnull().sum()  # This should now return 0 for all columns

# Proceeding to encode the target variable 'Status' (Dropout and Graduate) as a numerical value
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Status'] = le.fit_transform(data['Status'])
# Calculate average for each status
avg_enrolled = data[data['Status'] == 1]['Curricular_units_2nd_sem_approved'].mean()
avg_graduate= data[data['Status'] == 2]['Curricular_units_2nd_sem_approved'].mean()
avg_dropout= data[data['Status'] == 0]['Curricular_units_2nd_sem_approved'].mean()

# Title of the Streamlit App
st.title("Student Dropout Prediction")

# Display the averages
st.write(f"Average Curricular Units Approved for Dropout: {avg_dropout:.2f}")
st.write(f"Average Curricular Units Approved for Enrolled: {avg_enrolled:.2f}")
st.write(f"Average Curricular Units Approved for Graduate: {avg_graduate:.2f}")

# Add input field for user to enter number of curricular units approved in the 2nd semester
curricular_units_approved = st.number_input('Enter the number of Curricular Units Approved in 2nd Semester', min_value=0, max_value=100, value=0)

# Predict dropout status based on the entered curricular units
if st.button('Predict Status'):
    # Compare the entered value with the average values
    if curricular_units_approved < avg_dropout:
        st.write("The student is likely to dropout.")
    elif curricular_units_approved > avg_graduate:
        st.write("The student is likely to graduate.")
    else:
        st.write("The student is likely to be enrolled.")
