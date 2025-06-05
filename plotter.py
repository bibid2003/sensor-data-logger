import csv
import matplotlib.pyplot as plt

times = []
temps = []

with open("data/sensor_data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(int(row["Time(s)"]))
        temps.append(float(row["Temperature(C)"]))

plt.plot(times, temps, marker='o')
plt.title("Temperature Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
