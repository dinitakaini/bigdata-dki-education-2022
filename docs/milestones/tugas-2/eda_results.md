# Hasil Exploratory Data Analysis (EDA)

## 1. Statistik Deskriptif

Berdasarkan hasil analisis menggunakan Pandas, diperoleh statistik deskriptif sebagai berikut:

| Variabel | Rata-rata | Minimum | Median | Maksimum |
|---|---:|---:|---:|---:|
| Jumlah Sekolah | 115,03 | 1 | 39 | 1.269 |
| Jumlah Peserta Didik | 21.892,94 | 181 | 11.897 | 182.465 |
| Jumlah Guru | 1.230,32 | 20 | 712 | 7.701 |

Hasil tersebut menunjukkan bahwa jumlah sekolah, peserta didik, dan guru memiliki persebaran yang berbeda pada setiap kelompok data.

## 2. Analisis Berdasarkan Jenjang Sekolah

| Jenjang | Jumlah Sekolah | Jumlah Peserta Didik | Jumlah Guru |
|---|---:|---:|---:|
| PAUD | 4.101 | 138.458 | 12.833 |
| PKBM | 285 | 39.582 | 1.753 |
| SD | 2.241 | 765.202 | 37.962 |
| SLB | 89 | 6.056 | 1.261 |
| SMA | 495 | 190.240 | 11.283 |
| SMK | 571 | 196.409 | 11.210 |
| SMP | 1.075 | 349.809 | 18.433 |

Berdasarkan hasil pengelompokan, SD memiliki jumlah peserta didik dan guru paling banyak. Sementara itu, SLB memiliki jumlah sekolah dan peserta didik paling sedikit.

## 3. Analisis Berdasarkan Status Sekolah

| Status | Jumlah Sekolah | Jumlah Peserta Didik | Jumlah Guru |
|---|---:|---:|---:|
| Negeri | 2.009 | 931.282 | 42.848 |
| Swasta | 6.848 | 754.474 | 51.887 |

Hasil analisis menunjukkan bahwa sekolah swasta memiliki jumlah sekolah dan guru lebih banyak dibandingkan sekolah negeri. Namun, jumlah peserta didik di sekolah negeri lebih tinggi dibandingkan sekolah swasta.

## 4. Visualisasi Data

Visualisasi dibuat menggunakan library Matplotlib untuk membantu melihat perbandingan data berdasarkan jenjang sekolah.

Grafik yang dihasilkan terdiri dari:

1. Grafik jumlah sekolah berdasarkan jenjang sekolah.
2. Grafik jumlah peserta didik berdasarkan jenjang sekolah.
3. Grafik jumlah guru berdasarkan jenjang sekolah.

File grafik disimpan di folder `figures` dengan format PNG.

## 5. Kesimpulan EDA

Berdasarkan hasil analisis awal, terdapat perbedaan jumlah sekolah, peserta didik, dan guru pada setiap jenjang serta status sekolah di DKI Jakarta tahun 2022.

Jenjang SD memiliki jumlah peserta didik dan guru paling tinggi, sedangkan SLB memiliki jumlah sekolah paling sedikit. Jika dilihat berdasarkan statusnya, sekolah swasta memiliki jumlah unit sekolah lebih banyak, tetapi jumlah peserta didik lebih banyak terdapat pada sekolah negeri.

Hasil EDA ini dapat digunakan sebagai dasar untuk analisis lebih lanjut mengenai kondisi pendidikan di DKI Jakarta.
