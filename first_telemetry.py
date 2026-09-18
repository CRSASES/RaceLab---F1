from pathlib import Path
import fastf1
from matplotlib import pyplot as plt

# Absolute path to the project's data folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = PROJECT_ROOT / "data"

CACHE_DIR.mkdir(exist_ok=True) # It creates it if it doesn't exist
fastf1.Cache.enable_cache(CACHE_DIR)

# Download session
session = fastf1.get_session(2025, 'Monza', 'Q')

session.load()

# Driver fastes lap (VER = Verstappen)
lap = session.laps.pick_drivers("VER").pick_fastest()

# We obtain telemetry
telemetry = lap.get_car_data().add_distance()

print(telemetry.head())

plt.figure(figsize=(14,5))

plt.plot(
    telemetry['Distance'],
    telemetry['Speed'],
    color='red'
)

plt.title("Verstappen's Speed - 2025 Monza Qualifying")
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")

plt.grid(True)

# Accelerator and brake graph
fig, ax = plt.subplots(2, figsize=(14,8), sharex=True)

# Accelerator
ax[0].plot(
    telemetry['Distance'],
    telemetry['Throttle'],
    color='green'
)

ax[0].set_title("Accelerator")

# Brake
ax[1].plot(
    telemetry['Distance'],
    telemetry['Brake'],
    color='orange'
)

ax[1].set_title("Brake")

plt.xlabel("Distance (m)")

plt.style.use("dark_background")

plt.figure(figsize=(14,5))

plt.plot(
    telemetry['Distance'],
    telemetry['Speed'],
    linewidth=2
)

plt.title("RaceLab - Telemetry F1")
plt.xlabel("Distance")
plt.ylabel("Speed")

plt.show()