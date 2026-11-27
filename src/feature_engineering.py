import pandas as pd
from pathlib import Path

# Membaca data hasil cleaning Tugas 2
data = pd.read_excel("data/processed/data_bersih.xlsx")

# Memilih fitur dan target
fitur = data[
    [
        "jumlah_sekolah",
        "jumlah_guru",
        "jenjang_sekolah",
        "status_sekolah"
    ]
]

target = data["jumlah_peserta_didik"]

# Mengubah data kategori menjadi kolom numerik
fitur_encoded = pd.get_dummies(
    fitur,
    columns=["jenjang_sekolah", "status_sekolah"],
    dtype=int
)

# Menyimpan wilayah sebagai identitas kelompok evaluasi
hasil = pd.concat(
    [
        data[["wilayah"]].reset_index(drop=True),
        fitur_encoded.reset_index(drop=True),
        target.rename("jumlah_peserta_didik").reset_index(drop=True)
    ],
    axis=1
)

# Menyimpan hasil feature engineering
Path("data/processed").mkdir(parents=True, exist_ok=True)

hasil.to_csv(
    "data/processed/fitur_model.csv",
    index=False
)

print("=== FEATURE ENGINEERING SELESAI ===")
print("Jumlah baris dan kolom:", hasil.shape)
print("\nData hasil feature engineering:")
print(hasil.head())
print("\nNama kolom:")
print(hasil.columns.tolist())
