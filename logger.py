import csv
import random
import time

filename = "data/sensor_data.csv"


with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time(s)", "Temperature(C)"])


for i in range(20):
    temp = round(random.uniform(20.0, 30.0), 2)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i, temp])
    time.sleep(1)