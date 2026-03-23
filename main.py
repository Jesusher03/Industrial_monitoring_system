import time
from sensor_simulator import get_sensor_data
from data_logger import log_data
from alert_system import check_alerts
from analyzer import analyze_data

def run_system():
    for _ in range(20):  # Simula 20 ciclos de lectura
        data = get_sensor_data()
        print(f"Datos obtenidos: {data}")
            
        log_data(data)
        check_alerts(data)
            
        time.sleep(1)
            
    analyze_data()
        
if __name__ == "__main__":
    run_system()