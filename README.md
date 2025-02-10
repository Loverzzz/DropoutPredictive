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
Dashboard ini dapat diakses di 

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

### Rekomendasi Action Items
Berdasarkan hasil model, berikut adalah beberapa rekomendasi yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout:

## Action Items:

* Action Item 1: Pemberian Bimbingan atau Dukungan Dini
Identifikasi siswa yang berisiko tinggi melakukan dropout berdasarkan hasil prediksi dan berikan bimbingan, konseling, atau bantuan finansial untuk membantu mereka bertahan dalam pendidikan.

* Action Item 2: Penyuluhan tentang Pembelajaran dan Adaptasi
Berikan penyuluhan kepada siswa yang mengalami kesulitan akademik atau sosial, serta menyediakan platform untuk mendiskusikan kesulitan mereka dan memberikan pelatihan tentang cara-cara belajar yang efektif.

* Action Item 3: Monitoring Berkelanjutan
Setelah memberikan intervensi awal, lakukan pemantauan secara berkelanjutan untuk mengidentifikasi siswa yang mungkin membutuhkan bantuan lebih lanjut. Gunakan prediksi model sebagai referensi untuk evaluasi ulang.

* Action Item 4: Meningkatkan Keterlibatan Orang Tua
Meningkatkan komunikasi dengan orang tua siswa untuk memberikan dukungan lebih lanjut kepada siswa di rumah. Orang tua dapat berperan penting dalam menjaga motivasi dan menyelesaikan masalah yang dihadapi siswa.
