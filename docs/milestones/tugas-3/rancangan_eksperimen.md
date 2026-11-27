# Rancangan Eksperimen Tugas 3

## 1. Tujuan Analisis

Analisis ini dilakukan untuk memprediksi jumlah peserta didik berdasarkan data pendidikan DKI Jakarta tahun 2022. Data yang digunakan merupakan hasil pengolahan dari Tugas 2 dengan jumlah 77 baris data.

## 2. Metode yang Digunakan

Metode yang digunakan adalah regresi dengan algoritma Random Forest Regressor. Algoritma ini dipilih karena dapat digunakan untuk mempelajari hubungan antara beberapa fitur dengan nilai target yang berbentuk numerik.

Sebagai pembanding, digunakan Dummy Regressor dengan strategi rata-rata (mean) sebagai model baseline.

## 3. Fitur dan Target

Fitur yang digunakan:
- Jumlah sekolah
- Jumlah guru
- Jenjang sekolah
- Status sekolah

Target yang diprediksi adalah jumlah peserta didik.

Fitur kategori, yaitu jenjang dan status sekolah, diubah menjadi bentuk numerik menggunakan teknik one-hot encoding.

## 4. Parameter Model

Parameter Random Forest yang digunakan:
- n_estimators = 100
- max_depth = 5
- random_state = 42

Model baseline menggunakan Dummy Regressor dengan strategi mean.

## 5. Pembagian Data

Pembagian data dilakukan berdasarkan kelompok wilayah menggunakan GroupShuffleSplit agar data dari wilayah yang sama tidak tersebar ke kelompok training, validation, dan testing.

Hasil pembagian:
- Training: Kota Jakarta Barat, Kota Jakarta Selatan, Kota Jakarta Timur, dan Kota Jakarta Utara.
- Validation: Kota Jakarta Pusat.
- Testing: Kabupaten Kepulauan Seribu.

Data testing terdiri dari 7 baris.

## 6. Evaluasi Model

Evaluasi menggunakan tiga metrik, yaitu:
- Mean Absolute Error (MAE), untuk mengetahui rata-rata selisih absolut antara hasil prediksi dan nilai aktual.
- Root Mean Squared Error (RMSE), untuk mengukur besarnya kesalahan prediksi dengan memberikan penalti lebih besar pada kesalahan yang tinggi.
- R-squared (R²), untuk melihat kemampuan model dalam menjelaskan variasi nilai target.

Selain evaluasi utama, dilakukan analisis residual, perbandingan nilai aktual dan prediksi, serta pengujian kestabilan menggunakan Leave-One-Group-Out berdasarkan wilayah.

## 7. Analisis Keterbatasan

Data yang digunakan hanya mencakup satu tahun, yaitu 2022, dengan jumlah 77 baris dan enam kelompok wilayah. Oleh karena itu, hasil model belum dapat digunakan untuk menggambarkan kondisi pendidikan pada tahun lain.

Pengujian pada Kabupaten Kepulauan Seribu juga hanya menggunakan tujuh data, sehingga hasil evaluasinya perlu ditafsirkan secara hati-hati. Model ini digunakan untuk kebutuhan analisis akademik dan belum ditujukan sebagai sistem prediksi untuk pengambilan keputusan secara langsung.