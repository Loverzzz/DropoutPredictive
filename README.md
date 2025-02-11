# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Tingginya angka dropout di Jaya Jaya Institut yang berdampak pada reputasi dan sumber daya yang dikeluarkan.

### Permasalahan Bisnis
Jaya Jaya Institut mengalami masalah tingginya jumlah siswa yang tidak menyelesaikan pendidikannya (dropout). Ini berdampak pada reputasi institusi dan efisiensi penggunaan sumber daya. Oleh karena itu, Jaya Jaya Institut ingin mengembangkan sistem prediksi untuk mendeteksi siswa yang berpotensi melakukan dropout sehingga dapat diberikan bimbingan atau intervensi lebih awal.

### Cakupan Proyek

### 1. **Pemahaman Bisnis**
   - Masalah utama adalah tingginya jumlah dropout siswa. Oleh karena itu, tujuan proyek ini adalah untuk memprediksi kemungkinan dropout agar langkah preventif dapat dilakukan lebih awal.

### 2. **Pemrosesan Data**
   - Mengimpor dan memeriksa dataset.
   - Membersihkan data dengan menangani nilai yang hilang dan mengubah data kategorikal menjadi numerikal.

### 3. **Pembangunan Model Machine Learning**
   - Menggunakan **Random Forest Classifier** untuk membangun model prediksi.
   - Menggunakan metrik seperti akurasi, precision, recall, dan confusion matrix untuk mengevaluasi model.

### 4. **Pembuatan Dashboard**
   - Dashboard interaktif untuk memvisualisasikan data dan performa siswa menggunakan alat seperti **Metabase** atau **Tableau**.

### 5. **Streamlit Prototype**
   - Pembuatan aplikasi prototipe menggunakan **Streamlit** untuk menampilkan hasil prediksi model secara interaktif.

### 6. **Rekomendasi Action Items**
   - Berdasarkan hasil model, rekomendasikan langkah-langkah yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi jumlah dropout.

### Persiapan

Sumber data: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
conda create --name proyek_pyspark python=3.9

conda activate proyek_pyspark

pip install -r requirements.txt
```

## Business Dashboard
Dashboard yang telah dibuat bertujuan untuk membantu Jaya Jaya Institut memantau performa siswa dan mengidentifikasi faktor-faktor yang berkontribusi terhadap angka dropout. 
Dashboard ini dapat diakses di Link Streamlit Deploy : https://dropoutpredictive.streamlit.app/

## Menjalankan Sistem Machine Learning
Prototipe sistem machine learning ini dibangun menggunakan Streamlit. Untuk menjalankan prototipe, ikuti langkah-langkah berikut:

1. Unduh atau clone repositori proyek.
2. Instal dependensi yang diperlukan dengan menjalankan:
```
pip install -r requirements.txt
```
3. Jalankan aplikasi Streamlit dengan perintah: 
```
streamlit run app.py
```

## Conclusion
Melalui proyek ini, berhasil mengembangkan sistem prediksi yang dapat membantu Jaya Jaya Institut mendeteksi siswa yang berisiko melakukan dropout. Dengan prediksi yang lebih cepat, pihak institusi dapat memberikan intervensi yang lebih tepat waktu untuk mendukung siswa yang membutuhkan.

Feature Importance : 

![image](https://github.com/user-attachments/assets/5bfc7a55-858c-484f-ae19-4e588d9f8362)

Penjelasan Grafik Feature Importance:
* Label Sumbu X:

Pada sumbu X, kita melihat nama-nama fitur yang digunakan dalam model.
Fitur yang berada di sisi kiri (teratas) memiliki importance yang lebih tinggi, yang berarti fitur tersebut lebih berkontribusi dalam pembuatan prediksi oleh model.
* Label Sumbu Y:

Pada sumbu Y, kita melihat nilai importance atau kontribusi relatif dari masing-masing fitur.
Nilai ini menunjukkan seberapa besar pengaruh setiap fitur terhadap prediksi yang dilakukan oleh model Random Forest. Semakin tinggi nilai tersebut, semakin penting fitur tersebut dalam menentukan apakah seorang siswa akan melakukan dropout atau tidak.
* Fitur Paling Penting:

Fitur seperti Curricular_units_2nd_sem_approved, Curricular_units_1st_sem_approved, dan Curricular_units_2nd_sem_enrolled memiliki nilai importance yang paling tinggi, yang berarti bahwa jumlah unit kurikuler yang telah disetujui atau terdaftar di semester pertama dan kedua sangat berpengaruh pada keputusan model tentang apakah seorang siswa berisiko dropout.
* Fitur dengan Importance Lebih Rendah:

Fitur seperti Educational_special_needs, Daytime_evening_attendance, dan Gender berada di posisi paling bawah pada grafik. Ini menunjukkan bahwa fitur-fitur tersebut memiliki kontribusi yang lebih kecil dalam membuat prediksi dropout.

Dashboard Metabase : 
![image](https://github.com/user-attachments/assets/54cf4206-d8f9-4e30-bd80-b5894cf297c9)
Insight : 
1. Dropout vs Graduate vs Enrolled (Status vs Student Count):
   Tabel ini menunjukkan jumlah siswa yang memiliki status Dropout, Graduate, dan Enrolled:
   ```
   Dropout: 1,421 siswa
   Graduate: 2,209 siswa
   Enrolled: 794 siswa
   ```
   Ini memberikan gambaran tentang distribusi status siswa yang terkait dengan model prediksi. Sebagian besar siswa berstatus Graduate, sementara lebih sedikit yang Enrolled atau Dropout.
2. Grafik 1 - Average Curricular 2nd Sem Grade vs Status:
   Grafik ini menunjukkan rata-rata nilai unit kurikuler pada semester 2 berdasarkan status siswa.
   ```
   Dropout: Rata-rata nilai sekitar 6
   Enrolled: Rata-rata nilai sekitar 9
   Graduate: Rata-rata nilai sekitar 12
   ```
   Analisis: siswa dengan status Graduate memiliki nilai rata-rata yang lebih tinggi, sementara siswa yang Dropout memiliki nilai yang lebih rendah. Ini menunjukkan bahwa siswa dengan performa yang lebih baik cenderung untuk menyelesaikan studi mereka, sedangkan siswa dengan nilai rendah lebih cenderung untuk dropout.
3. Grafik 2 - Avg Curricular Units 2nd Sem Approved vs Status:
   Grafik ini menunjukkan rata-rata unit kurikuler yang disetujui di semester 2 berdasarkan status siswa.
   ```
   Dropout: Rata-rata sekitar 2 unit kurikuler disetujui
   Enrolled: Rata-rata sekitar 4 unit kurikuler disetujui
   Graduate: Rata-rata sekitar 6 unit kurikuler disetujui
   ```
   Analisis: siswa yang Graduate menyelesaikan lebih banyak unit kurikuler di semester 2 dibandingkan dengan siswa yang Dropout atau Enrolled. siswa yang lebih banyak menyelesaikan unit kurikuler memiliki peluang lebih besar untuk lulus.
4. Grafik 3 - Average of Admission Grade vs Status:
   Grafik ini menunjukkan rata-rata nilai penerimaan berdasarkan status siswa.
   Rata-rata nilai penerimaan hampir sama untuk siswa Dropout, Enrolled, dan Graduate.
   Analisis: Nilai penerimaan tampaknya tidak terlalu memengaruhi status siswa dibandingkan dengan jumlah unit kurikuler yang disetujui pada semester 2. Ini menunjukkan bahwa meskipun nilai penerimaan penting, faktor-faktor lain seperti kinerja akademik selama semester lebih berpengaruh pada keputusan siswa untuk tetap terdaftar atau dropout.
5.  Percentage of Students Approved in the Second Semester:
   Persentase siswa yang Disetujui di Semester 2: 71.18% siswa berhasil menyelesaikan unit kurikuler yang disetujui di semester 2.
   Analisis: Ini menunjukkan bahwa sebagian besar siswa masih berhasil menyelesaikan tugas mereka di semester 2, namun ada ruang untuk meningkatkan jumlah siswa yang berhasil menyelesaikan semester tersebut, terutama bagi yang berstatus Dropout.

### Rekomendasi Action Items
Berdasarkan hasil model, berikut adalah beberapa rekomendasi yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout:

## Action Items:
1. Memperhatikan jumlah unit kurikuler yang disetujui di semester 2 berperan penting dalam memprediksi kemungkinan dropout. Ini menunjukkan bahwa siswa yang tertinggal dalam pekerjaan akademik lebih cenderung untuk keluar.
2. Mengingat pentingnya Unit Kurikuler yang Disetujui di Semester 2 dalam memprediksi dropout, siswa yang tertinggal seharusnya segera dikenali dan dibantu. Penawaran konseling akademik, bimbingan, dan mentor dapat membantu siswa ini mengejar ketertinggalan sebelum akhirnya keluar.
