import pandas as pd
from pathlib import Path

# Menentukan lokasi folder
project_folder = Path(__file__).resolve().parent.parent

# Membaca data mentah
raw_path = project_folder / "data" / "raw" / "Filedata Jumlah Sekolah Guru dan Murid Menurut Jenis Sekolah Tahun 2022.xlsx"

df = pd.read_excel(raw_path)

# Memastikan format data konsisten
kolom_teks = [
    "wilayah",
    "jenjang_sekolah",
    "status_sekolah"
]

for kolom in kolom_teks:
    df[kolom] = df[kolom].str.strip()

# Menyimpan data hasil pengolahan
processed_path = project_folder / "data" / "processed"
processed_path.mkdir(parents=True, exist_ok=True)

output_file = processed_path / "data_bersih.xlsx"
df.to_excel(output_file, index=False)

print("Data berhasil diproses!")
print("Jumlah baris:", len(df))
print("Jumlah kolom:", len(df.columns))
print("File tersimpan di:", output_file)
