import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "raw" / "Filedata Jumlah Sekolah Guru dan Murid Menurut Jenis Sekolah Tahun 2022.xlsx"

df = pd.read_excel(file_path)

kolom_kategori = [
    "wilayah",
    "jenjang_sekolah",
    "status_sekolah"
]

for kolom in kolom_kategori:
    print(f"\n=== {kolom.upper()} ===")
    print("Kategori yang ditemukan:")
    print(df[kolom].unique())

    print("Jumlah spasi di awal/akhir:")
    print(df[kolom].astype(str).ne(df[kolom].astype(str).str.strip()).sum())