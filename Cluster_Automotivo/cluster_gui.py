"""
GUI do Cluster Automotivo - Interface Web
Exibe RPM como medidor analógico + barras horizontais para outros sensores
Otimizado para Raspberry Pi e interface web
"""

import os
import threading
import time
import webbrowser
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from vehicle_sensors import VehicleSensorSimulator
from datetime import datetime

# HTML template served from templates/index.html
# Classe do cluster web
class ClusterWebApp:
    def __init__(self, use_hardware=False):
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        self.sensor = VehicleSensorSimulator()
        self.use_hardware = use_hardware
        self.running = True
        self.current_gear = 0
        self.current_speed = 0
        self.odo = 12345
        self.tripA = 12.3
        self.tripB = 45.6

        # Routes
        @self.app.route('/')
        def index():
            return render_template('index.html')

        # SocketIO events
        @self.socketio.on('connect')
        def handle_connect():
            print('Client connected')

        @self.socketio.on('disconnect')
        def handle_disconnect():
            print('Client disconnected')

    def _calculate_speed_from_rpm_and_gear(self, rpm, gear):
        """Calcula velocidade baseada no RPM e marcha"""
        if gear == 0:  # Ponto morto
            return 0
        
        # Ranges de velocidade por marcha
        gear_ranges = {
            1: (0, 60),
            2: (60, 90),
            3: (90, 120),
            4: (120, 160),
            5: (160, 200),
            6: (200, 220),
        }
        
        min_speed, max_speed = gear_ranges[gear]
        
        # RPM válido de 1000 a 7000
        rpm_normalized = max(0, min(7000, rpm) - 1000) / 6000  # 0 a 1
        
        # Calcular velocidade baseada no RPM
        speed = min_speed + (max_speed - min_speed) * rpm_normalized
        
        return min(max_speed, speed)

    def _update_display(self):
        """Atualiza os valores e envia via SocketIO"""
        while self.running:
            if self.sensor.engine_running:
                self.sensor.consume_fuel(0.01)
            
            # Obter dados
            data = self.sensor.get_current_data()
            
            # Calcular velocidade baseada na marcha
            if self.current_gear > 0 and self.sensor.engine_running:
                self.current_speed = self._calculate_speed_from_rpm_and_gear(
                    data.rpm, self.current_gear
                )
            else:
                self.current_speed = 0
            
            # Preparar dados para envio
            update_data = {
                'rpm': data.rpm,
                'speed': self.current_speed,
                'fuel': data.fuel_level,
                'coolant': data.coolant_temp,
                'oil_temp': data.oil_pressure * 10 + 80,  # Simular temp óleo
                'trans_temp': data.transmission_oil_temp,
                'battery': 13.5,
                'gear': self.current_gear,
                'odo': self.odo,
                'tripA': self.tripA,
                'tripB': self.tripB,
                'boost': 0.8,
                'warnings': {
                    'oil': data.oil_pressure < 2,
                    'temp': data.coolant_temp > 100,
                    'bat': False,
                }
            }
            
            # Enviar via SocketIO
            self.socketio.emit('update', update_data)
            
            time.sleep(0.1)

    def start_engine(self):
        self.sensor.start_engine()

    def stop_engine(self):
        self.sensor.stop_engine()
        self.current_speed = 0
        self.current_gear = 0

    def shift_up(self):
        if self.current_gear < 6:
            self.current_gear += 1

    def shift_down(self):
        if self.current_gear > 0:
            self.current_gear -= 1

    def run(self):
        """Inicia o servidor web e abre navegador"""
        # Iniciar thread de atualização
        update_thread = threading.Thread(target=self._update_display, daemon=True)
        update_thread.start()
        
        # Abrir navegador
        webbrowser.open('http://localhost:5000')
        
        # Iniciar servidor
        self.socketio.run(self.app, host='0.0.0.0', port=5000, debug=False)


if __name__ == "__main__":
    # Inicia cluster web
    cluster = ClusterWebApp(use_hardware=False)
    cluster.run()