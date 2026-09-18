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
plt.style.use("dark_background")
telemetry = lap.get_car_data().add_distance()

print(telemetry.head())

# Speed, Accelerator and Brake graph
fig, ax = plt.subplots(3, figsize=(14,8), sharex=True)
# Speed
ax[0].plot(
    telemetry['Distance'],
    telemetry['Speed'],
    color='red'
)

ax[0].set_title("Verstappen's Speed - 2025 Monza Qualifying")
ax[0].set_xlabel("Distance (m)")
ax[0].set_ylabel("Speed (km/h)")

# Accelerator
ax[1].plot(
    telemetry['Distance'],
    telemetry['Throttle'],
    color='green'
)

ax[1].set_title("Accelerator")

# Brake
ax[2].plot(
    telemetry['Distance'],
    telemetry['Brake'],
    color='orange'
)

ax[2].set_title("Brake")

plt.xlabel("Distance (m)")

plt.grid(True)
plt.show()