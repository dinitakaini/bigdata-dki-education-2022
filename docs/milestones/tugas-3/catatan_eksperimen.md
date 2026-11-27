# Catatan Eksperimen Tugas 3

## 1. Informasi Eksperimen

- Nama eksperimen: Prediksi Jumlah Peserta Didik DKI Jakarta Tahun 2022
- Dataset: data_bersih.xlsx
- Lokasi dataset: data/processed/data_bersih.xlsx
- Jumlah data: 77 baris
- Jumlah wilayah: 6 wilayah
- Target: jumlah_peserta_didik
- Metode utama: Random Forest Regressor
- Model pembanding: Dummy Regressor

## 2. Persiapan Data

Data yang digunakan merupakan hasil pengolahan dari Tugas 2. Sebelum pemodelan, dilakukan pemeriksaan data dan feature engineering.

Fitur kategorikal berupa jenjang sekolah dan status sekolah diubah menggunakan one-hot encoding. Hasil pengolahan disimpan dalam file `data/processed/fitur_model.csv`.

## 3. Parameter Eksperimen

Parameter Random Forest:
- n_estimators: 100
- max_depth: 5
- random_state: 42

Parameter baseline:
- Model: Dummy Regressor
- strategy: mean

Pengujian kestabilan:
- Metode: Leave-One-Group-Out
- Kelompok: wilayah

## 4. Pembagian Data

Pembagian dilakukan berdasarkan wilayah menggunakan GroupShuffleSplit.

- Training: 4 wilayah
- Validation: 1 wilayah
- Testing: 1 wilayah
- Random seed: 42

Wilayah training terdiri dari Jakarta Barat, Jakarta Selatan, Jakarta Timur, dan Jakarta Utara. Jakarta Pusat digunakan untuk validation, sedangkan Kabupaten Kepulauan Seribu digunakan untuk testing.

## 5. Hasil Eksperimen

Hasil pengujian Random Forest:
- Validation MAE: 2.953,38
- Validation RMSE: 4.248,36
- Validation R²: 0,909
- Testing MAE: 542,11
- Testing RMSE: 621,29
- Testing R²: 0,289

Hasil pengujian kestabilan menggunakan Leave-One-Group-Out:
- Rata-rata MAE: 4.386,82
- Rata-rata RMSE: 8.032,21
- Rata-rata R²: 0,786

## 6. Keputusan Model

Random Forest dipilih sebagai model utama karena menghasilkan nilai evaluasi yang lebih baik dibandingkan Dummy Regressor pada validation dan testing.

Walaupun demikian, hasil testing dan pengujian kestabilan menunjukkan bahwa performa model belum konsisten pada seluruh wilayah. Oleh karena itu, model dipertahankan untuk keperluan analisis akademik dengan mencantumkan keterbatasannya.

## 7. File Hasil

- `tables/model_metrics.csv`
- `tables/predictions.csv`
- `tables/error_analysis.csv`
- `tables/stability_results.csv`
- `tables/feature_importance.csv`
- `figures/actual_vs_predicted.png`
- `figures/residual_plot.png`
- `figures/feature_importance.png`

## 8. Catatan Keterbatasan

Eksperimen menggunakan data pendidikan satu tahun dengan jumlah 77 baris dan enam kelompok wilayah. Hasil pengujian dapat dipengaruhi oleh perbedaan karakteristik antarwilayah dan jumlah data yang terbatas.

Versi pustaka dan identitas versi dataset perlu dicatat berdasarkan lingkungan dan file yang benar-benar digunakan saat eksperimen dijalankan.

## 9. Lingkungan Pemrograman dan Versi Dataset

Lingkungan yang digunakan dalam eksperimen ini adalah:
- Python: 3.15.2
- Pandas: 3.1.1
- Scikit-learn: 1.9.1
- Matplotlib: 3.11.2

Identitas dataset diperiksa menggunakan SHA-256 untuk memastikan file yang digunakan dapat dikenali kembali.

SHA-256:
`c75502671b4404776ae2de0c887ee36f41fef7c2c115ff4ec5ae123be4904eb0`

File dataset yang digunakan adalah `data/processed/data_bersih.xlsx`.