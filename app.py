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

# Encode the target variable 'Status' (Dropout and Graduate) as a numerical value
le = LabelEncoder()
data['Status'] = le.fit_transform(data['Status'])

# Split data into features (X) and target (y)
X = data.drop('Status', axis=1)
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

# Add input fields for users to enter values for each feature
input_values = {}
for col in numerical_columns:
    input_values[col] = st.number_input(f"Enter the value for {col}", value=0)

# Prepare user input for prediction (convert to DataFrame)
user_input = pd.DataFrame([input_values])

# Predict the status using the trained Random Forest model
if st.button('Predict Status'):
    user_prediction = model.predict(user_input)
    prediction = le.inverse_transform(user_prediction)
    st.write(f"Predicted Status: {prediction[0]}")
