def check_alerts(data):
    if data['temperature'] > 80:
        print("ALERTA: Temperatura alta detectada!")
    
    if data['pressure'] > 8:
        print("ALERTA: Presión alta detectada!")