import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Muat model yang sudah disimpan
best_rf = joblib.load('rfmodel.pkl')

# Muat dataset untuk preprocessing
data = pd.read_csv('data.csv', delimiter=";")

# Mengambil nama kolom fitur yang digunakan oleh model
features = best_rf.feature_names_in_

# Judul Aplikasi Streamlit
st.title("Prediksi Dropout Mahasiswa")

# Menampilkan informasi aplikasi
st.write("Prediksi dropout, tetap terdaftar, atau lulus berdasarkan data akademiknya.")

# Menambahkan kolom input bagi pengguna untuk memasukkan data
curricular_units_approved = st.number_input('Masukkan jumlah Curricular Units yang disetujui pada Semester 2 (0 - 7)', min_value=0, max_value=7, value=0)
curricular_units_2nd_sem_grade = st.number_input('Masukkan Nilai Curricular Units di Semester 2 (0 - 12)', min_value=0, max_value=12, value=0)
admission_grade = st.number_input('Masukkan Nilai Admission Grade (95 - 190)', min_value=0, max_value=190, value=0)

# Membuat DataFrame dengan data input yang ada
input_data = pd.DataFrame({
    'Curricular_units_2nd_sem_approved': [curricular_units_approved],
    'Curricular_units_1st_sem_approved': [curricular_units_2nd_sem_grade],
    'Admission_grade': [admission_grade]
})

# Menambahkan kolom yang hilang dengan nilai NaN sesuai dengan fitur yang digunakan oleh model
for col in features:
    if col not in input_data.columns:
        input_data[col] = np.nan

# Menangani nilai hilang: untuk numerik dengan rata-rata, dan kategorikal dengan modus
numerical_columns = input_data.select_dtypes(include=[np.number]).columns
categorical_columns = input_data.select_dtypes(include=[object]).columns

# Isi nilai hilang pada kolom numerik dengan rata-rata kolom yang sama
for col in numerical_columns:
    input_data[col] = input_data[col].fillna(input_data[col].mean())

# Isi nilai hilang pada kolom kategorikal dengan modus
for col in categorical_columns:
    input_data[col] = input_data[col].fillna(input_data[col].mode()[0])

# Menyesuaikan urutan kolom input_data dengan urutan fitur yang digunakan saat pelatihan
input_data = input_data[features]

# Menampilkan data input untuk debugging
st.write("Data Input yang Digunakan:")
st.write(input_data)

# Prediksi dengan model
prediction = best_rf.predict(input_data)

# Menampilkan hasil prediksi
prediction_label = prediction[0]
if prediction_label == 0:
    st.write("Siswa kemungkinan akan dropout.")
elif prediction_label == 1:
    st.write("Siswa kemungkinan akan tetap terdaftar.")
else:
    st.write("Siswa kemungkinan akan lulus.")
