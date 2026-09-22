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

# Fastes lap
lap_ver = session.laps.pick_drivers("VER").pick_fastest()
lap_nor = session.laps.pick_drivers("NOR").pick_fastest()

# We obtain telemetry
plt.style.use("dark_background")
telemetry_ver = lap_ver.get_car_data().add_distance()
telemetry_nor = lap_nor.get_car_data().add_distance()

position_ver = lap_ver.get_pos_data()

print(position_ver.head())



print("Verstappen lap:", lap_ver["LapTime"])
print("Norris lap:", lap_nor["LapTime"])

print("Verstappen max speed:", telemetry_ver["Speed"].max())
print("Norris max speed:", telemetry_nor["Speed"].max())



# Speed, Accelerator and Brake graph
fig, ax = plt.subplots(3, figsize=(14,8), sharex=True)
fig.subplots_adjust(hspace=0.4)

# Speed
ax[0].plot(
    telemetry_ver['Distance'],
    telemetry_ver['Speed'],
    color='red'
)

ax[0].plot(
    telemetry_nor['Distance'],
    telemetry_nor['Speed'],
    color='blue'
)

ax[0].set_title("Verstappen's Max Speed (Red) - Norris Max Speed (Blue)")
ax[0].set_ylabel("Speed (km/h)")
ax[0].legend()

# Accelerator
ax[1].plot(
    telemetry_ver['Distance'],
    telemetry_ver['Throttle'],
    color='red'
)
ax[1].plot(
    telemetry_nor['Distance'],
    telemetry_nor['Throttle'],
    color='blue'
)

ax[1].set_title("Accelerator")

# Brake
ax[2].plot(
    telemetry_ver['Distance'],
    telemetry_ver['Brake'],
    color='red'
)
ax[2].plot(
    telemetry_nor['Distance'],
    telemetry_nor['Brake'],
    color='blue'
)

ax[2].set_title("Brake")

plt.xlabel("Distance (m)")

plt.grid(True)
plt.show()

# Circuit map
fig2, ax2 = plt.subplots(figsize=(10, 8))

ax2.plot(
    position_ver["X"],
    position_ver["Y"]
)

ax2.set_title("RaceLab - Monza Circuit")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

ax2.grid(True)
# With this, the circuit will look the same
ax2.set_aspect("equal")

plt.show()