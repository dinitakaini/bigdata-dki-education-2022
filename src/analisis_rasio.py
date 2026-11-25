import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"

df = pd.read_excel(file_path)

# Menghitung total berdasarkan jenjang sekolah
rasio_jenjang = df.groupby("jenjang_sekolah")[
    ["jumlah_peserta_didik", "jumlah_guru"]
].sum()

rasio_jenjang["rasio_murid_guru"] = (
    rasio_jenjang["jumlah_peserta_didik"] /
    rasio_jenjang["jumlah_guru"]
)

print("=== RASIO MURID TERHADAP GURU BERDASARKAN JENJANG ===")
print(rasio_jenjang.round(2))

# Menghitung total berdasarkan status sekolah
rasio_status = df.groupby("status_sekolah")[
    ["jumlah_peserta_didik", "jumlah_guru"]
].sum()

rasio_status["rasio_murid_guru"] = (
    rasio_status["jumlah_peserta_didik"] /
    rasio_status["jumlah_guru"]
)

print("\n=== RASIO MURID TERHADAP GURU BERDASARKAN STATUS ===")
print(rasio_status.round(2))
