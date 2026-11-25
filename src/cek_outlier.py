import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "processed" / "data_bersih.xlsx"

df = pd.read_excel(file_path)

kolom_numerik = [
    "jumlah_sekolah",
    "jumlah_peserta_didik",
    "jumlah_guru"
]

for kolom in kolom_numerik:
    Q1 = df[kolom].quantile(0.25)
    Q3 = df[kolom].quantile(0.75)
    IQR = Q3 - Q1

    batas_bawah = Q1 - 1.5 * IQR
    batas_atas = Q3 + 1.5 * IQR

    outlier = df[
        (df[kolom] < batas_bawah) |
        (df[kolom] > batas_atas)
    ]

    print(f"\n=== {kolom} ===")
    print("Batas bawah:", batas_bawah)
    print("Batas atas:", batas_atas)
    print("Jumlah nilai terdeteksi:", len(outlier))

    if not outlier.empty:
        print(outlier[[
            "wilayah",
            "jenjang_sekolah",
            "status_sekolah",
            kolom
        ]])