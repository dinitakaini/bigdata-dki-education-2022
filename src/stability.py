import pandas as pd
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("data/processed/fitur_model.csv")

X = data.drop(columns=["wilayah", "jumlah_peserta_didik"])
y = data["jumlah_peserta_didik"]
groups = data["wilayah"]

logo = LeaveOneGroupOut()
hasil = []

for train_idx, test_idx in logo.split(X, y, groups):
    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]
    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)
    prediksi = model.predict(X_test)

    hasil.append({
        "wilayah_pengujian": groups.iloc[test_idx].iloc[0],
        "jumlah_data": len(test_idx),
        "MAE": mean_absolute_error(y_test, prediksi),
        "RMSE": mean_squared_error(y_test, prediksi) ** 0.5,
        "R2": r2_score(y_test, prediksi)
    })

hasil_df = pd.DataFrame(hasil)

print("=== HASIL PENGUJIAN KESTABILAN MODEL ===")
print(hasil_df.to_string(index=False))

print("\n=== RATA-RATA METRIK ===")
print(hasil_df[["MAE", "RMSE", "R2"]].mean())

print("\n=== STANDAR DEVIASI METRIK ===")
print(hasil_df[["MAE", "RMSE", "R2"]].std())

hasil_df.to_csv("tables/stability_results.csv", index=False)
print("\nHasil kestabilan berhasil disimpan.")