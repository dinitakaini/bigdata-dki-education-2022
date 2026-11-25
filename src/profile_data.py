import pandas as pd
from pathlib import Path

# Menentukan lokasi file dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "raw" / "Filedata Jumlah Sekolah Guru dan Murid Menurut Jenis Sekolah Tahun 2022.xlsx"

# Membaca dataset
df = pd.read_excel(file_path)

# Menampilkan informasi dasar dataset
print("=== INFORMASI DATASET ===")
print("Jumlah baris dan kolom:", df.shape)

print("\n=== NAMA KOLOM ===")
print(df.columns.tolist())

print("\n=== TIPE DATA ===")
print(df.dtypes)

print("\n=== DATA KOSONG ===")
print(df.isnull().sum())

print("\n=== DATA DUPLIKAT ===")
print("Jumlah duplikat:", df.duplicated().sum())

print("\n=== 5 DATA PERTAMA ===")
print(df.head())

print("\n=== STATISTIK DESKRIPTIF ===")
print(df.describe(include="all"))

print("\n=== PEMERIKSAAN KATEGORI ===")

print("\nWilayah:")
print(df["wilayah"].value_counts())

print("\nJenjang Sekolah:")
print(df["jenjang_sekolah"].value_counts())

print("\nStatus Sekolah:")
print(df["status_sekolah"].value_counts())

print("\nTahun:")
print(df["tahun"].value_counts())

print("\n=== PEMERIKSAAN KOMBINASI DATA ===")

kombinasi = df.groupby(
    ["wilayah", "jenjang_sekolah"]
)["status_sekolah"].nunique()

print("Kombinasi wilayah dan jenjang:")
print(kombinasi)

print("\nJumlah kombinasi dengan satu status:")
print((kombinasi == 1).sum())

print("\nJumlah kombinasi dengan dua status:")
print((kombinasi == 2).sum())

print("\n=== PEMERIKSAAN NILAI TIDAK WAJAR ===")

kolom_numerik = [
    "jumlah_sekolah",
    "jumlah_peserta_didik",
    "jumlah_guru"
]

for kolom in kolom_numerik:
    print(f"\n{kolom}")
    print("Nilai nol:", (df[kolom] == 0).sum())
    print("Nilai negatif:", (df[kolom] < 0).sum())
    print("Nilai minimum:", df[kolom].min())
    print("Nilai maksimum:", df[kolom].max())
