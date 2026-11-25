# Data Acquisition

## 1. Sumber Data

Data yang digunakan dalam penelitian ini diperoleh dari portal data terbuka pemerintah, yaitu:

1. Data.go.id  
   https://data.go.id/dataset/dataset/jumlah-sekolah-guru-dan-murid-menurut-jenis-sekolah-tahun-2022

2. Satu Data Jakarta  
   https://satudata.jakarta.go.id/open-data/detail?kategori=dataset&page_url=jumlah-sekolah-guru-dan-murid-menurut-jenis-sekolah&data_no=1

## 2. Informasi Dataset

- Nama dataset: Jumlah Sekolah, Guru, dan Murid Menurut Jenis Sekolah Tahun 2022
- Instansi: Dinas Pendidikan Provinsi DKI Jakarta
- Wilayah cakupan: DKI Jakarta
- Tahun data: 2022
- Format file: Microsoft Excel (.xlsx)
- Jumlah data: 77 baris dan 8 kolom

## 3. Proses Akuisisi Data

Proses pengumpulan data dilakukan dengan mengunduh dataset dari portal data terbuka yang tersedia. File Excel yang diperoleh kemudian diperiksa dan dimasukkan ke dalam folder `data/raw` pada proyek GitHub.

Data mentah tetap disimpan dalam bentuk aslinya dan tidak diubah secara langsung. Proses pengolahan dilakukan menggunakan Python dengan bantuan library Pandas agar tahapan pengolahan data dapat dilakukan kembali.

## 4. Penyimpanan Data

Dataset disimpan dengan struktur folder sebagai berikut:

- `data/raw/`: menyimpan file dataset asli.
- `data/processed/`: menyimpan hasil pengolahan data.
- `src/`: menyimpan kode Python untuk pemeriksaan, pembersihan, dan analisis data.
- `figures/`: menyimpan hasil visualisasi data.

## 5. Tujuan Penggunaan Data

Dataset digunakan untuk menganalisis jumlah sekolah, peserta didik, dan guru berdasarkan wilayah, jenjang pendidikan, serta status sekolah Negeri dan Swasta di DKI Jakarta pada tahun 2022.

## Informasi File dan Checksum

- Nama file: Filedata Jumlah Sekolah Guru dan Murid Menurut Jenis Sekolah Tahun 2022.xlsx
- Ukuran file: 9.105 bytes
- Format: XLSX
- Jumlah baris: 77
- Jumlah kolom: 8
- Algoritma checksum: SHA-256
- Nilai checksum: 80a501f08639985f989b343a825f45ecaabe6761f068544ca6972cbfac13cfe8

Checksum digunakan sebagai identitas file untuk membantu memastikan bahwa file data mentah tidak mengalami perubahan.