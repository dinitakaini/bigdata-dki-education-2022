import pandas as pd
from pathlib import Path

from sklearn.model_selection import GroupShuffleSplit
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Membaca data hasil feature engineering
data = pd.read_csv("data/processed/fitur_model.csv")

# Menentukan fitur, target, dan kelompok wilayah
X = data.drop(columns=["wilayah", "jumlah_peserta_didik"])
y = data["jumlah_peserta_didik"]
groups = data["wilayah"]

# Membagi data: 1 wilayah untuk testing
split_test = GroupShuffleSplit(
    n_splits=1,
    test_size=1/6,
    random_state=42
)

train_val_idx, test_idx = next(
    split_test.split(X, y, groups)
)

# Membagi sisa data: 1 wilayah untuk validation
X_train_val = X.iloc[train_val_idx]
y_train_val = y.iloc[train_val_idx]
groups_train_val = groups.iloc[train_val_idx]

split_val = GroupShuffleSplit(
    n_splits=1,
    test_size=1/5,
    random_state=42
)

train_idx, val_idx = next(
    split_val.split(X_train_val, y_train_val, groups_train_val)
)

# Menentukan data training, validation, dan testing
X_train = X_train_val.iloc[train_idx]
y_train = y_train_val.iloc[train_idx]

X_val = X_train_val.iloc[val_idx]
y_val = y_train_val.iloc[val_idx]

X_test = X.iloc[test_idx]
y_test = y.iloc[test_idx]

# Menampilkan wilayah pada setiap pembagian
print("=== PEMBAGIAN DATA ===")
print("Training:", sorted(groups.iloc[X_train.index].unique()))
print("Validation:", sorted(groups.iloc[X_val.index].unique()))
print("Testing:", sorted(groups.iloc[X_test.index].unique()))

# Membuat model baseline
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)

# Membuat model Random Forest
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train)

# Fungsi evaluasi
def evaluasi(nama_model, model, X_data, y_data, tahap):
    prediksi = model.predict(X_data)

    return {
        "tahap": tahap,
        "model": nama_model,
        "MAE": mean_absolute_error(y_data, prediksi),
        "RMSE": mean_squared_error(y_data, prediksi) ** 0.5,
        "R2": r2_score(y_data, prediksi)
    }

# Evaluasi validation
hasil_validasi = [
    evaluasi("Dummy Regressor", baseline, X_val, y_val, "Validation"),
    evaluasi("Random Forest", model, X_val, y_val, "Validation")
]

# Model final dilatih ulang menggunakan training + validation
X_final_train = pd.concat([X_train, X_val])
y_final_train = pd.concat([y_train, y_val])

baseline_final = DummyRegressor(strategy="mean")
baseline_final.fit(X_final_train, y_final_train)

model_final = RandomForestRegressor(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model_final.fit(X_final_train, y_final_train)

# Evaluasi akhir pada testing
hasil_testing = [
    evaluasi("Dummy Regressor", baseline_final, X_test, y_test, "Testing"),
    evaluasi("Random Forest", model_final, X_test, y_test, "Testing")
]

# Menggabungkan hasil evaluasi
hasil = pd.DataFrame(hasil_validasi + hasil_testing)

Path("tables").mkdir(exist_ok=True)
Path("data/processed").mkdir(exist_ok=True)

hasil.to_csv("tables/model_metrics.csv", index=False)

# Menyimpan hasil prediksi testing
prediksi_test = pd.DataFrame({
    "wilayah": groups.iloc[test_idx].values,
    "aktual": y_test.values,
    "prediksi_baseline": baseline_final.predict(X_test),
    "prediksi_random_forest": model_final.predict(X_test)
})

prediksi_test.to_csv(
    "tables/predictions.csv",
    index=False
)

print("\n=== HASIL EVALUASI ===")
print(hasil.to_string(index=False))

print("\n=== PREDIKSI DATA TESTING ===")
print(prediksi_test.to_string(index=False))

print("\nFile hasil berhasil disimpan.")

# Menghitung dan menyimpan feature importance
feature_importance = pd.DataFrame({
    "fitur": X.columns,
    "tingkat_pengaruh": model_final.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="tingkat_pengaruh",
    ascending=False
)

feature_importance.to_csv(
    "tables/feature_importance.csv",
    index=False
)

print("\n=== FEATURE IMPORTANCE ===")
print(feature_importance.to_string(index=False))

print("\nFeature importance berhasil disimpan.")
