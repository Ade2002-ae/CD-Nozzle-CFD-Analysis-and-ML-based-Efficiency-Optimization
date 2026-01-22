import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load CFD Data

data = pd.read_csv(r"C:\Users\admin\Desktop\GitHub Projects\CD Nozzle and CFD\cd_nozzle_results.csv")

Altitude = data["Altitude_km"].values.reshape(-1, 1)
Thrust = data["Thrust_N"].values
MassFlow = data["MassFlow_kg_s"].values

# Compute Efficiency (Specific Thrust)

efficiency = Thrust / MassFlow   # N·s/kg

# Polynomial Regression

poly = PolynomialFeatures(degree=3)
Altitude_poly = poly.fit_transform(Altitude)

model = LinearRegression()
model.fit(Altitude_poly, efficiency)

# Smooth prediction range
Altitude_fine = np.linspace(Altitude.min(), Altitude.max(), 300).reshape(-1, 1)

Altitude_fine_poly = poly.transform(Altitude_fine)
eff_pred = model.predict(Altitude_fine_poly)

# PHYSICAL CONSTRAINTS (ALTITUDE)

# Define valid operating altitude band (km)
alt_min = 1.0
alt_max = 7.0

valid_mask = ((Altitude_fine.flatten() >= alt_min) & (Altitude_fine.flatten() <= alt_max))
Altitude_valid = Altitude_fine[valid_mask]
eff_valid = eff_pred[valid_mask]

# Find optimal point ONLY within valid range

best_index = np.argmax(eff_valid)
best_altitude = Altitude_valid[best_index][0]
best_eff = eff_valid[best_index]

# Plot Results

plt.figure(figsize=(8, 5))
plt.scatter(Altitude, efficiency, color="red", label="CFD Data")
plt.plot(Altitude_fine, eff_pred, color="blue", label="Regression Fit")
plt.axvspan(alt_min, alt_max, color="gray", alpha=0.15, label="Valid Operating Range")
plt.axvline(best_altitude, linestyle="--", color="green", label=f"Optimal Altitude ≈ {best_altitude:.2f} km")
plt.xlabel("Altitude (km)")
plt.ylabel("Specific Thrust (N·s/kg)")
plt.title("Optimal Altitude")
plt.legend()
plt.grid(True)
plt.show()

# Print Results

print("Optimal Altitude:", round(best_altitude, 2), "km")
print("Maximum Specific Thrust:", round(best_eff, 2), "N·s/kg")
