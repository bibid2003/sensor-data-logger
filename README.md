 Sensor Data Logger 

A simple Python project to simulate temperature sensor data logging and visualize it using a line chart.

 Features

- Logs simulated temperature readings (20°C to 30°C) into a CSV file
- Records a temperature value every second for 20 seconds
- Plots the temperature data over time using `matplotlib`

 Project Structure

sensor-data-logger/
data/
  sensor_data.csv  Logged temperature data
logger.py Script to simulate and log temperature data
plotter.py Script to read CSV and plot the data
README.md  Project documentation


  How to Run

1. Generate data:

```bash
python logger.py
```
2. Visualize Data

python plotter.py


3. Output

A .csv file inside the data/ folder
A simple line plot showing temperature over time


4. Author

Bibid B
GitHub: @bibid2003
