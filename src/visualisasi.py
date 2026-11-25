import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"

df = pd.read_excel(file_path)

# Menghitung total berdasarkan jenjang sekolah
hasil = df.groupby("jenjang_sekolah")[
    ["jumlah_sekolah", "jumlah_peserta_didik", "jumlah_guru"]
].sum()

# Membuat folder penyimpanan grafik
folder_gambar = project_folder / "figures"
folder_gambar.mkdir(parents=True, exist_ok=True)

# Membuat tiga grafik
daftar_grafik = [
    ("jumlah_sekolah", "Jumlah Sekolah", "grafik_jumlah_sekolah.png"),
    ("jumlah_peserta_didik", "Jumlah Peserta Didik", "grafik_jumlah_murid.png"),
    ("jumlah_guru", "Jumlah Guru", "grafik_jumlah_guru.png")
]

for kolom, judul, nama_file in daftar_grafik:
    plt.figure(figsize=(9, 5))
    hasil[kolom].plot(kind="bar")
    plt.title(judul + " Berdasarkan Jenjang Sekolah")
    plt.xlabel("Jenjang Sekolah")
    plt.ylabel(judul)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(folder_gambar / nama_file)
    plt.close()

print("Semua grafik berhasil dibuat!")
print("Lokasi penyimpanan:", folder_gambar)