import random
import time

def get_sensor_data():
    data = {
        "temperature": round(random.uniform(20, 100), 2),
        "pressure": round(random.uniform(1, 10), 2),
        "humidity": round(random.uniform(30, 90), 2)
    }
    return data