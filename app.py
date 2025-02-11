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
# Fill missing values in numerical columns with their mean
numerical_columns = data.select_dtypes(include=[np.number]).columns
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# Encode the target variable 'Status' (Dropout and Graduate) as a numerical value
le = LabelEncoder()
data['Status'] = le.fit_transform(data['Status'])

# Select only the relevant feature (Curricular_units_2nd_sem_approved)
X = data[['Curricular_units_2nd_sem_approved']]  # Only this feature as input
y = data['Status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Display the classification report and confusion matrix
st.write("Classification Report:")
st.write(classification_report(y_test, y_pred))
st.write("Confusion Matrix:")
st.write(confusion_matrix(y_test, y_pred))

# Title of the Streamlit App
st.title("Student Dropout Prediction")

# Add input field for the user to enter the value for Curricular_units_2nd_sem_approved
curricular_units_approved = st.number_input('Enter the number of Curricular Units Approved in 2nd Semester', min_value=0, max_value=100, value=0)

# Prepare user input for prediction
user_input = pd.DataFrame({'Curricular_units_2nd_sem_approved': [curricular_
