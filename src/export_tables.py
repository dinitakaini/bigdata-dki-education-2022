import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"
folder_tabel = project_folder / "tables"

folder_tabel.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(file_path)

# Tabel statistik deskriptif
statistik = df[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].describe()

statistik.to_csv(folder_tabel / "statistik_deskriptif.csv")

# Tabel berdasarkan jenjang sekolah
jenjang = df.groupby("jenjang_sekolah")[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].sum()

jenjang.to_csv(folder_tabel / "total_berdasarkan_jenjang.csv")

# Tabel berdasarkan status sekolah
status = df.groupby("status_sekolah")[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].sum()

status.to_csv(folder_tabel / "total_berdasarkan_status.csv")

# Tabel rasio murid dan guru berdasarkan jenjang
rasio_jenjang = df.groupby("jenjang_sekolah")[
    ["jumlah_peserta_didik", "jumlah_guru"]
].sum()

rasio_jenjang["rasio_murid_guru"] = (
    rasio_jenjang["jumlah_peserta_didik"] /
    rasio_jenjang["jumlah_guru"]
)

rasio_jenjang.round(2).to_csv(
    folder_tabel / "rasio_murid_guru_berdasarkan_jenjang.csv"
)

# Tabel rasio murid dan guru berdasarkan status
rasio_status = df.groupby("status_sekolah")[
    ["jumlah_peserta_didik", "jumlah_guru"]
].sum()

rasio_status["rasio_murid_guru"] = (
    rasio_status["jumlah_peserta_didik"] /
    rasio_status["jumlah_guru"]
)

rasio_status.round(2).to_csv(
    folder_tabel / "rasio_murid_guru_berdasarkan_status.csv"
)

print("Semua tabel berhasil disimpan di folder tables!")