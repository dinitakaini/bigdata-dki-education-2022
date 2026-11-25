# Data Preparation

## 1. Tahapan Persiapan Data

Persiapan data dilakukan sebelum masuk ke tahap analisis. Proses ini menggunakan bahasa pemrograman Python dengan library Pandas untuk membaca dan mengolah dataset.

Tahapan yang dilakukan meliputi:

1. Membaca dataset Excel yang tersimpan di folder `data/raw`.
2. Memeriksa jumlah baris dan kolom pada dataset.
3. Memeriksa tipe data setiap kolom.
4. Memeriksa keberadaan data kosong dan duplikat.
5. Memeriksa nilai nol dan negatif pada kolom numerik.
6. Membersihkan spasi berlebih pada kolom teks.
7. Menyimpan hasil pengolahan ke folder `data/processed`.

## 2. Proses Cleaning Data

Proses cleaning dilakukan menggunakan script `src/clean_data.py`.

Pembersihan dilakukan dengan menghilangkan spasi berlebih pada bagian awal dan akhir teks di kolom wilayah, jenjang sekolah, dan status sekolah.

Tidak dilakukan penghapusan baris karena hasil pemeriksaan sebelumnya tidak menemukan data kosong maupun data duplikat.

Nilai numerik juga tetap dipertahankan karena tidak ditemukan nilai nol atau negatif.

## 3. Proses Transformasi Data

Data dikelompokkan berdasarkan jenjang sekolah dan status sekolah untuk memperoleh jumlah sekolah, peserta didik, dan guru pada setiap kelompok.

Proses pengelompokan dilakukan pada tahap Exploratory Data Analysis (EDA) menggunakan fungsi `groupby()` dari Pandas.

## 4. Hasil Data Preparation

Setelah proses cleaning dilakukan, dataset memiliki kondisi sebagai berikut:

| Keterangan | Sebelum | Sesudah |
|---|---:|---:|
| Jumlah baris | 77 | 77 |
| Jumlah kolom | 8 | 8 |
| Data kosong | 0 | 0 |
| Data duplikat | 0 | 0 |

Hasil pengolahan disimpan dalam file `data/processed/data_bersih.xlsx`.

## 5. Kesimpulan

Berdasarkan proses persiapan data, dataset tidak memerlukan banyak perubahan karena kondisi awalnya sudah cukup baik. Pembersihan dilakukan untuk memastikan format teks lebih konsisten, sedangkan seluruh baris dan nilai numerik tetap dipertahankan agar informasi dari sumber data tidak berubah.
