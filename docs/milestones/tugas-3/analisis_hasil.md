# Analisis Hasil dan Evaluasi Model Tugas 3

## 1. Hasil Evaluasi Model

Berdasarkan pengujian yang telah dilakukan, model Random Forest menunjukkan hasil yang lebih baik dibandingkan model baseline Dummy Regressor. Pada tahap validation, Random Forest memperoleh MAE sebesar 2.953,38, RMSE sebesar 4.248,36, dan R² sebesar 0,909.

Sementara itu, pada tahap testing, Random Forest memperoleh MAE sebesar 542,11, RMSE sebesar 621,29, dan R² sebesar 0,289. Hasil tersebut menunjukkan bahwa rata-rata selisih prediksi dengan jumlah peserta didik sebenarnya pada data testing sekitar 542 peserta didik.

Walaupun nilai MAE dan RMSE pada testing terlihat lebih rendah dibandingkan validation, nilai R² yang hanya sebesar 0,289 menunjukkan bahwa kemampuan model dalam menjelaskan variasi jumlah peserta didik pada wilayah pengujian masih terbatas.

## 2. Analisis Kesalahan Prediksi

Analisis kesalahan dilakukan dengan membandingkan hasil prediksi dengan jumlah peserta didik sebenarnya. Dari tujuh data testing di Kabupaten Kepulauan Seribu, diperoleh rata-rata absolute error sebesar 542,11 dan rata-rata percentage error sebesar 153,25%.

Seluruh residual memiliki nilai negatif. Hal ini menunjukkan bahwa model cenderung menghasilkan prediksi yang lebih tinggi dibandingkan jumlah peserta didik sebenarnya pada data pengujian tersebut.

Hasil ini menunjukkan bahwa model masih memiliki kesalahan prediksi, terutama pada data dengan jumlah peserta didik yang relatif kecil.

## 3. Pengujian Kestabilan Model

Pengujian kestabilan dilakukan menggunakan Leave-One-Group-Out berdasarkan enam wilayah di DKI Jakarta. Hasil pengujian memperoleh rata-rata MAE sebesar 4.386,82, RMSE sebesar 8.032,21, dan R² sebesar 0,786.

Namun, nilai metrik menunjukkan perbedaan antarwilayah. Kabupaten Kepulauan Seribu memperoleh R² sebesar 0,278, sedangkan Kota Jakarta Barat memperoleh R² sebesar 0,941.

Perbedaan tersebut menunjukkan bahwa performa model belum sepenuhnya konsisten ketika diuji pada wilayah yang berbeda. Karakteristik data dan perbedaan jumlah peserta didik antarwilayah dapat menjadi salah satu faktor yang memengaruhi hasil prediksi.

## 4. Analisis Feature Importance

Berdasarkan hasil feature importance, jumlah guru menjadi fitur yang paling dominan dengan nilai sebesar 0,933 atau sekitar 93,33%. Selanjutnya, jumlah sekolah memiliki nilai sebesar 0,027 atau sekitar 2,73%, sedangkan fitur jenjang dan status sekolah memiliki nilai yang lebih kecil.

Hasil ini menunjukkan bahwa model Random Forest lebih banyak memanfaatkan informasi jumlah guru dalam melakukan prediksi jumlah peserta didik.

Namun, feature importance hanya menggambarkan tingkat kepentingan fitur dalam model dan tidak dapat digunakan untuk menyimpulkan hubungan sebab-akibat.

## 5. Kesimpulan Evaluasi

Berdasarkan hasil pengujian, Random Forest mampu menghasilkan performa yang lebih baik dibandingkan baseline pada data validation dan testing. Meskipun demikian, hasil pengujian kestabilan dan nilai R² pada testing menunjukkan bahwa kemampuan model masih berbeda antarwilayah.

Dengan jumlah data yang terbatas dan hanya menggunakan data tahun 2022, model ini masih perlu dikembangkan menggunakan data dari tahun lain dan pengujian yang lebih luas. Oleh karena itu, hasil analisis ini lebih tepat digunakan sebagai gambaran awal penerapan metode regresi pada data pendidikan DKI Jakarta.

## 6. Perbandingan dengan Teori dan Penelitian Terdahulu

Metode Random Forest yang digunakan dalam analisis ini mengacu pada konsep yang dijelaskan oleh Breiman (2001). Random Forest merupakan metode ensemble yang menggabungkan beberapa pohon keputusan untuk menghasilkan prediksi. Pada permasalahan regresi, hasil prediksi diperoleh dengan menggabungkan prediksi dari pohon-pohon yang dibentuk.

Berdasarkan konsep tersebut, penggunaan Random Forest dalam penelitian ini sesuai karena target yang diprediksi berupa jumlah peserta didik atau data numerik. Model memanfaatkan beberapa fitur, seperti jumlah sekolah, jumlah guru, jenjang pendidikan, dan status sekolah untuk menghasilkan prediksi.

Hasil analisis menunjukkan bahwa jumlah guru menjadi fitur yang paling dominan dalam model dengan nilai feature importance sekitar 93,33%. Hal ini memperlihatkan bahwa model lebih banyak memanfaatkan informasi jumlah guru dalam proses prediksi. Temuan ini merupakan hasil dari dataset yang digunakan dan tidak dapat langsung dianggap sebagai hubungan sebab-akibat.

Pengujian kestabilan juga menggunakan pendekatan Leave-One-Group-Out. Pendekatan ini sesuai dengan dokumentasi scikit-learn, yaitu menguji model dengan mengeluarkan satu kelompok data secara bergantian. Dalam penelitian ini, kelompok yang digunakan adalah wilayah di DKI Jakarta.

Hasil pengujian menunjukkan adanya perbedaan performa model antarwilayah. Dengan demikian, hasil penelitian mendukung pentingnya melakukan evaluasi berdasarkan kelompok data, bukan hanya mengandalkan satu hasil pembagian data.

Secara keseluruhan, metode yang digunakan telah sesuai dengan konsep Random Forest dan evaluasi berbasis kelompok. Namun, hasil penelitian ini merupakan penerapan pada dataset pendidikan DKI Jakarta tahun 2022, sehingga tidak dapat dianggap sebagai pembuktian bahwa model akan menghasilkan performa yang sama pada dataset lain.

## Daftar Pustaka

Breiman, L. (2001). Random Forests. *Machine Learning, 45*, 5–32. https://doi.org/10.1023/A:1010933404324

Scikit-learn Developers. (n.d.). *LeaveOneGroupOut*. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html