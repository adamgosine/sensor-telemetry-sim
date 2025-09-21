import random
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Simulate 3 sensor types
def simulate_temperature():
    return round(random.uniform(20.0, 90.0), 2)

def simulate_voltage():
    return round(random.uniform(11.0, 14.8), 2)

def simulate_acceleration():
    return round(random.uniform(-1.5, 1.5), 2)

# Logging setup
data_log = []

print("[✓] Starting sensor simulation...")

# Simulate for 60 seconds
for _ in range(60):
    timestamp = datetime.now().strftime("%H:%M:%S")
    temp = simulate_temperature()
    volt = simulate_voltage()
    accel = simulate_acceleration()

    data_log.append({
        "Timestamp": timestamp,
        "Temperature (°C)": temp,
        "Voltage (V)": volt,
        "Acceleration (m/s^2)": accel
    })

    # Simple alert triggers
    if temp > 75:
        print(f"[!] ALERT: High temperature ({temp}°C) at {timestamp}")
    if volt < 11.5:
        print(f"[!] ALERT: Low voltage ({volt}V) at {timestamp}")
    if abs(accel) > 1.3:
        print(f"[!] ALERT: Sudden acceleration ({accel} m/s^2) at {timestamp}")

    time.sleep(1)


# Save to CSV
df = pd.DataFrame(data_log)
df.to_csv("sensor_log.csv", index=False)
print("[✓] Sensor data saved to 'sensor_log.csv'")

# Plotting
df.plot(x="Timestamp", y=["Temperature (°C)", "Voltage (V)", "Acceleration (m/s^2)"], figsize=(12, 6))
plt.title("Sensor Readings Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("sensor_plot.png")
plt.show()

