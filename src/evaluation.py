import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Membaca hasil prediksi testing
data = pd.read_csv("tables/predictions.csv")

# Menghitung residual dan kesalahan prediksi
data["residual"] = (
    data["aktual"] - data["prediksi_random_forest"]
)

data["absolute_error"] = data["residual"].abs()

data["percentage_error"] = (
    data["absolute_error"] / data["aktual"]
) * 100

# Menyimpan tabel error analysis
Path("tables").mkdir(exist_ok=True)
Path("figures").mkdir(exist_ok=True)

data.to_csv("tables/error_analysis.csv", index=False)

print("=== HASIL ERROR ANALYSIS ===")
print(data.to_string(index=False))

print("\nRata-rata absolute error:", data["absolute_error"].mean())
print("Rata-rata percentage error:", data["percentage_error"].mean())

# Visualisasi aktual dan prediksi
plt.figure(figsize=(8, 5))
plt.scatter(
    data["aktual"],
    data["prediksi_random_forest"]
)

batas = max(
    data["aktual"].max(),
    data["prediksi_random_forest"].max()
)

plt.plot([0, batas], [0, batas], linestyle="--")
plt.xlabel("Jumlah Murid Aktual")
plt.ylabel("Jumlah Murid Prediksi")
plt.title("Perbandingan Aktual dan Prediksi")
plt.tight_layout()
plt.savefig("figures/actual_vs_predicted.png", dpi=300)
plt.close()

# Visualisasi residual
plt.figure(figsize=(8, 5))
plt.scatter(
    data["prediksi_random_forest"],
    data["residual"]
)

plt.axhline(y=0, linestyle="--")
plt.xlabel("Jumlah Murid Prediksi")
plt.ylabel("Residual")
plt.title("Residual Plot Random Forest")
plt.tight_layout()
plt.savefig("figures/residual_plot.png", dpi=300)
plt.close()

print("\nVisualisasi berhasil disimpan.")
