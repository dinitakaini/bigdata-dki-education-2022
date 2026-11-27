import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data = pd.read_csv("tables/feature_importance.csv")

data = data.sort_values(
    by="tingkat_pengaruh",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    data["fitur"],
    data["tingkat_pengaruh"]
)

plt.xlabel("Tingkat Pengaruh")
plt.ylabel("Fitur")
plt.title("Feature Importance Random Forest")
plt.tight_layout()

Path("figures").mkdir(exist_ok=True)

plt.savefig(
    "figures/feature_importance.png",
    dpi=300
)

plt.close()

print("Visualisasi feature importance berhasil disimpan.")