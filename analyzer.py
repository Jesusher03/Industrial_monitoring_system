import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    df = pd.read_csv('../data/sensor_data_log.csv')
    
    print("\n Promedios:") 
    print(df.mean(numeric_only=True))
    
def plot_data():
    df = pd.read_csv('../data/sensor_data_log.csv')
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)   
    plt.plot(df['temperature'], label='Temperatura', color='red')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(df['pressure'], label='Presión', color='blue')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(df['humidity'], label='Humedad', color='green')
    plt.legend()
    plt.tight_layout()
    plt.show()

        
    
  