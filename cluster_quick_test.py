"""
Teste rápido da GUI do Cluster Automotivo
Versão simplificada para testes rápidos (sem dependências pesadas)
"""

import tkinter as tk
from tkinter import font, Frame, Label, Button
from vehicle_sensors import VehicleSensorSimulator
import time


def quick_test():
    """Teste rápido visual da interface"""
    
    # Criar janela
    root = tk.Tk()
    root.title("Cluster Automotivo - Teste Rápido")
    root.geometry("600x400")
    root.configure(bg='#1a1a1a')
    
    # Sensor
    sensor = VehicleSensorSimulator()
    
    # Labels
    main_frame = Frame(root, bg='#1a1a1a')
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    title = Label(main_frame, text="⚙️ TESTE DO CLUSTER", 
                 font=("Arial", 20, "bold"), bg='#1a1a1a', fg='#00ff00')
    title.pack(pady=10)
    
    # Frame de indicadores
    display_frame = Frame(main_frame, bg='#222222', relief='sunken', bd=2)
    display_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Velocidade
    vel_label = Label(display_frame, text="Velocidade: 000 km/h", 
                     font=("Arial", 16), bg='#222222', fg='#00ff00')
    vel_label.pack(pady=5)
    
    # RPM
    rpm_label = Label(display_frame, text="RPM: 0000", 
                     font=("Arial", 16), bg='#222222', fg='#00ff00')
    rpm_label.pack(pady=5)
    
    # Combustível
    fuel_label = Label(display_frame, text="Combustível: 00.0%", 
                      font=("Arial", 16), bg='#222222', fg='#00ff00')
    fuel_label.pack(pady=5)
    
    # Temperatura
    temp_label = Label(display_frame, text="Temp: 00.0°C", 
                      font=("Arial", 16), bg='#222222', fg='#00ff00')
    temp_label.pack(pady=5)
    
    # Status
    status_label = Label(main_frame, text="⚫ MOTOR DESLIGADO", 
                        font=("Arial", 12), bg='#1a1a1a', fg='#ffff00')
    status_label.pack(pady=5)
    
    # Botões
    btn_frame = Frame(main_frame, bg='#1a1a1a')
    btn_frame.pack(fill='x', pady=10)
    
    def update_display():
        """Atualiza display"""
        data = sensor.get_current_data()
        
        vel_label.config(text=f"Velocidade: {data.speed_kmh:03.0f} km/h")
        rpm_label.config(text=f"RPM: {data.rpm:04.0f}")
        fuel_label.config(text=f"Combustível: {data.fuel_level:05.1f}%")
        temp_label.config(text=f"Temperatura: {data.coolant_temp:05.1f}°C")
        
        status = "🔵 MOTOR LIGADO" if sensor.engine_running else "⚫ MOTOR DESLIGADO"
        status_label.config(text=status)
        
        root.after(100, update_display)
    
    def start_engine():
        sensor.start_engine()
    
    def stop_engine():
        sensor.stop_engine()
    
    def accelerate():
        for _ in range(5):
            sensor.accelerate(200)
            root.update()
            time.sleep(0.05)
    
    def decelerate():
        for _ in range(10):
            sensor.decelerate(100)
            root.update()
            time.sleep(0.05)
    
    Button(btn_frame, text="▶ Ligar", command=start_engine,
           bg='#00aa00', fg='white', padx=10, pady=5).pack(side='left', padx=5)
    Button(btn_frame, text="⏹ Desligar", command=stop_engine,
           bg='#cc0000', fg='white', padx=10, pady=5).pack(side='left', padx=5)
    Button(btn_frame, text="⬆ Acelerar", command=accelerate,
           bg='#ff6600', fg='white', padx=10, pady=5).pack(side='left', padx=5)
    Button(btn_frame, text="⬇ Desacelerar", command=decelerate,
           bg='#0066ff', fg='white', padx=10, pady=5).pack(side='left', padx=5)
    
    # Iniciar atualização
    update_display()
    
    root.mainloop()


if __name__ == "__main__":
    print("Iniciando teste rápido da interface...")
    print("Clique nos botões para testar o simulador")
    print("Feche a janela para sair.\n")
    
    quick_test()
