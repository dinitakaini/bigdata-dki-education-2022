import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"

df = pd.read_excel(file_path)

print("=== PEMERIKSAAN DATA HASIL CLEANING ===")
print("Jumlah baris dan kolom:", df.shape)

print("\nData kosong:")
print(df.isnull().sum())

print("\nJumlah data duplikat:")
print(df.duplicated().sum())

print("\n5 data pertama:")
print(df.head())