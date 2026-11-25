# Data Profiling dan Data Quality

## 1. Data Profiling

Data profiling dilakukan untuk mengetahui kondisi awal dataset sebelum digunakan dalam proses analisis. Pemeriksaan dilakukan menggunakan Python dengan library Pandas.

Berdasarkan hasil pemeriksaan, dataset memiliki 77 baris dan 8 kolom. Data mencakup informasi jumlah sekolah, peserta didik, dan guru berdasarkan wilayah, jenjang sekolah, serta status sekolah di DKI Jakarta tahun 2022.

## 2. Pemeriksaan Kualitas Data

Hasil pemeriksaan kualitas data adalah sebagai berikut:

| Aspek Pemeriksaan | Hasil |
|---|---|
| Jumlah baris | 77 |
| Jumlah kolom | 8 |
| Data kosong | 0 |
| Data duplikat | 0 |
| Nilai nol pada kolom numerik | 0 |
| Nilai negatif pada kolom numerik | 0 |

Dari hasil tersebut, tidak ditemukan data kosong maupun data duplikat. Seluruh kolom numerik juga memiliki nilai positif.

## 3. Pemeriksaan Distribusi Data

Dataset memiliki beberapa kategori sebagai berikut:

- Wilayah: 6 wilayah administrasi.
- Jenjang sekolah: PAUD, PKBM, SD, SLB, SMA, SMK, dan SMP.
- Status sekolah: Negeri dan Swasta.
- Tahun pencatatan: 2022.

## 4. Statistik Deskriptif

| Variabel | Minimum | Median | Maksimum |
|---|---:|---:|---:|
| Jumlah Sekolah | 1 | 39 | 1.269 |
| Jumlah Peserta Didik | 181 | 11.897 | 182.465 |
| Jumlah Guru | 20 | 712 | 7.701 |

Hasil statistik menunjukkan bahwa jumlah sekolah, peserta didik, dan guru memiliki rentang nilai yang cukup beragam pada setiap kelompok data.

## 5. Catatan Hasil Pemeriksaan

Berdasarkan pemeriksaan kombinasi wilayah dan jenjang sekolah, terdapat beberapa kelompok yang hanya memiliki satu status sekolah, yaitu Negeri atau Swasta. Kondisi tersebut tidak langsung dianggap sebagai kesalahan data karena perlu disesuaikan dengan kondisi sebenarnya.

Nilai maksimum yang cukup besar juga tidak langsung dianggap sebagai kesalahan atau data pencilan karena masih perlu dilihat berdasarkan konteks wilayah dan jenjang sekolah.

## 6. Kesimpulan

Secara umum, dataset sudah memiliki kondisi yang cukup baik untuk digunakan dalam analisis awal. Tidak ditemukan nilai kosong, data duplikat, maupun nilai negatif pada kolom numerik. Oleh karena itu, proses pengolahan data dilanjutkan tanpa menghapus baris data.

## Pemeriksaan Perubahan Skema

Pemeriksaan dilakukan dengan membandingkan nama kolom dan tipe data pada dataset asli. Hasilnya menunjukkan terdapat 77 baris dan 8 kolom. Nama kolom serta tipe datanya sesuai dengan struktur yang digunakan dalam proses pengolahan. Tidak ditemukan perubahan skema pada dataset yang diperiksa.

## Pemeriksaan Outlier

Pemeriksaan outlier dilakukan menggunakan metode Interquartile Range (IQR). Hasil pemeriksaan menemukan 8 nilai outlier pada jumlah sekolah, 5 pada jumlah peserta didik, dan 3 pada jumlah guru.

Nilai yang terdeteksi sebagian besar berasal dari jumlah sekolah dan peserta didik SD Negeri serta PAUD Swasta di beberapa wilayah Jakarta. Nilai tersebut tidak langsung dihapus karena masih perlu mempertimbangkan kondisi dan karakteristik data. Oleh karena itu, seluruh data tetap dipertahankan agar informasi aslinya tidak hilang.

## Pemeriksaan Konsistensi Label

Pemeriksaan dilakukan pada kolom wilayah, jenjang sekolah, dan status sekolah. Hasilnya menunjukkan terdapat 6 kategori wilayah, 7 kategori jenjang sekolah, dan 2 kategori status sekolah. Tidak ditemukan spasi berlebih pada awal maupun akhir teks. Penulisan label kategori juga sudah konsisten sehingga tidak diperlukan perubahan tambahan.