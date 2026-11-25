import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"

df = pd.read_excel(file_path)

print("=== STATISTIK DESKRIPTIF ===")
print(df[[
    "jumlah_sekolah",
    "jumlah_peserta_didik",
    "jumlah_guru"
]].describe())

print("\n=== TOTAL BERDASARKAN JENJANG SEKOLAH ===")
hasil = df.groupby("jenjang_sekolah")[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].sum()

print(hasil)

print("\n=== TOTAL BERDASARKAN STATUS SEKOLAH ===")
status = df.groupby("status_sekolah")[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].sum()

print(status)