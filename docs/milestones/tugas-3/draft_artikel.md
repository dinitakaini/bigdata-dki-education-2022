# Metode Analitik dan Hasil

## 1. Metode Analitik

Penelitian ini menggunakan pendekatan analisis data dengan metode regresi untuk memprediksi jumlah peserta didik berdasarkan data pendidikan DKI Jakarta tahun 2022. Data yang digunakan merupakan data hasil pengolahan pada tugas sebelumnya dengan jumlah 77 baris data yang mencakup enam wilayah di DKI Jakarta.

Metode yang digunakan adalah Random Forest Regressor. Sebagai pembanding, penelitian ini juga menggunakan Dummy Regressor dengan strategi mean sebagai baseline. Pemilihan Random Forest dilakukan karena metode ini dapat mempelajari pola hubungan antara beberapa fitur dan target melalui kumpulan pohon keputusan.

Variabel yang digunakan sebagai fitur meliputi jumlah sekolah, jumlah guru, jenjang pendidikan, dan status sekolah. Sementara itu, variabel target adalah jumlah peserta didik. Fitur kategorikal berupa jenjang dan status sekolah diubah menggunakan teknik one-hot encoding agar dapat diproses oleh model.

Pembagian data dilakukan berdasarkan kelompok wilayah menggunakan GroupShuffleSplit. Empat wilayah digunakan untuk training, satu wilayah untuk validation, dan satu wilayah untuk testing. Parameter Random Forest yang digunakan adalah n_estimators sebesar 100, max_depth sebesar 5, dan random_state sebesar 42.

Evaluasi model dilakukan menggunakan Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), dan R-squared (R²). Selain itu, dilakukan analisis residual, feature importance, serta pengujian kestabilan menggunakan Leave-One-Group-Out berdasarkan wilayah.

## 2. Hasil dan Pembahasan

Hasil pengujian menunjukkan bahwa Random Forest memperoleh nilai MAE sebesar 2.953,38, RMSE sebesar 4.248,36, dan R² sebesar 0,909 pada tahap validation. Pada tahap testing, model memperoleh MAE sebesar 542,11, RMSE sebesar 621,29, dan R² sebesar 0,289.

Hasil tersebut menunjukkan bahwa model Random Forest lebih baik dibandingkan baseline dalam pengujian yang dilakukan. Namun, nilai R² pada testing menunjukkan bahwa kemampuan model dalam menjelaskan variasi jumlah peserta didik pada wilayah pengujian masih terbatas. Data testing hanya terdiri dari tujuh baris yang berasal dari Kabupaten Kepulauan Seribu, sehingga hasilnya belum dapat mewakili seluruh wilayah DKI Jakarta.

Pada analisis kesalahan prediksi, diperoleh rata-rata absolute error sebesar 542,11 dan rata-rata percentage error sebesar 153,25%. Seluruh residual pada data testing bernilai negatif, yang menunjukkan bahwa model menghasilkan prediksi lebih tinggi daripada nilai aktual pada seluruh data pengujian.

Pengujian kestabilan menggunakan Leave-One-Group-Out menghasilkan rata-rata MAE sebesar 4.386,82, RMSE sebesar 8.032,21, dan R² sebesar 0,786. Perbedaan hasil antarwilayah menunjukkan bahwa kemampuan model tidak sama pada setiap kelompok wilayah.

Berdasarkan analisis feature importance, jumlah guru menjadi fitur yang paling dominan dengan nilai sekitar 93,33%. Jumlah sekolah memiliki nilai sekitar 2,73%, sedangkan fitur lainnya memiliki nilai yang lebih kecil. Hasil ini menunjukkan bahwa jumlah guru paling banyak dimanfaatkan oleh model dalam menghasilkan prediksi. Namun, nilai feature importance tidak menunjukkan hubungan sebab-akibat antara jumlah guru dan jumlah peserta didik.

## 3. Keterbatasan Analisis

Analisis ini memiliki beberapa keterbatasan. Pertama, data yang digunakan hanya mencakup tahun 2022 dengan jumlah 77 baris. Kedua, data testing hanya berasal dari satu wilayah dengan jumlah tujuh baris. Ketiga, pengujian kestabilan menunjukkan adanya perbedaan performa antarwilayah.

Selain itu, model belum mempertimbangkan faktor lain yang mungkin berkaitan dengan jumlah peserta didik, seperti kondisi sosial ekonomi, fasilitas pendidikan, dan akses terhadap sekolah. Oleh karena itu, hasil penelitian ini masih bersifat analisis awal dan belum dapat dijadikan dasar tunggal untuk pengambilan keputusan di bidang pendidikan.

## 4. Kesimpulan

Berdasarkan hasil analisis, Random Forest dapat digunakan untuk memprediksi jumlah peserta didik menggunakan fitur jumlah sekolah, jumlah guru, jenjang pendidikan, dan status sekolah. Model menghasilkan performa yang lebih baik dibandingkan baseline pada pengujian yang dilakukan.

Meskipun demikian, perbedaan performa antarwilayah dan keterbatasan jumlah data menunjukkan bahwa model masih perlu dikembangkan dan diuji menggunakan data yang lebih luas. Hasil analisis ini dapat menjadi gambaran awal dalam penerapan metode machine learning pada data pendidikan DKI Jakarta.