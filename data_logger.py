import csv 
from datetime import datetime

def log_data(data):
    with open('sensor_data_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now, data['temperature'], data['pressure'], data['humidity']])