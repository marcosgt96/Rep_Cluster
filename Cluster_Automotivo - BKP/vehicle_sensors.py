"""
Módulo de Sensores Automotivos - Cluster de Painel de Instrumento
Gerencia leitura e armazenamento de dados de sensores do veículo
"""

from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class VehicleData:
    """Classe para armazenar dados do veículo"""
    timestamp: datetime
    speed_kmh: float  # Velocidade em km/h
    rpm: float  # Rotações por minuto
    fuel_level: float  # Nível de combustível (0-100%)
    coolant_temp: float  # Temperatura do líquido de arrefecimento (°C)
    oil_pressure: float  # Pressão do óleo (bar)
    transmission_oil_temp: float  # Temperatura do óleo da transmissão (°C)
    
    def __str__(self):
        return (
            f"Velocidade: {self.speed_kmh:.1f} km/h | "
            f"RPM: {self.rpm:.0f} | "
            f"Combustível: {self.fuel_level:.1f}% | "
            f"Temp. Ar.: {self.coolant_temp:.1f}°C | "
            f"Press. Óleo: {self.oil_pressure:.2f} bar | "
            f"Temp. Trans.: {self.transmission_oil_temp:.1f}°C"
        )


class VehicleSensorSimulator:
    """Simulador de sensores para testes (sem hardware real)"""
    
    def __init__(self):
        self.speed = 0.0
        self.rpm = 0.0
        self.fuel = 80.0
        self.coolant_temp = 90.0
        self.oil_pressure = 2.5
        self.transmission_oil_temp = 60.0
        self.engine_running = False
    
    def start_engine(self):
        """Simula ligar o motor"""
        self.engine_running = True
        self.rpm = 800  # RPM ocioso
        self.coolant_temp = 20.0  # Começa frio
        self.oil_pressure = 1.5
    
    def stop_engine(self):
        """Simula desligar o motor"""
        self.engine_running = False
        self.rpm = 0.0
        self.speed = 0.0
        
    def accelerate(self, delta=100):
        """Simula aceleração"""
        if self.engine_running:
            self.rpm = min(self.rpm + delta, 7000)
            self.speed = min(self.speed + (delta / 100), 200)
            # Aquecimento do motor
            self.coolant_temp = min(self.coolant_temp + 0.5, 110)
            self.oil_pressure = min(self.oil_pressure + 0.3, 5.0)
            self.transmission_oil_temp = min(self.transmission_oil_temp + 0.2, 100)
    
    def decelerate(self, delta=100):
        """Simula desaceleração"""
        if self.engine_running:
            self.rpm = max(self.rpm - delta, 800)
            self.speed = max(self.speed - (delta / 100), 0.0)
    
    def consume_fuel(self, amount=0.1):
        """Simula consumo de combustível"""
        self.fuel = max(self.fuel - amount, 0.0)
    
    def get_current_data(self) -> VehicleData:
        """Retorna os dados atuais dos sensores"""
        return VehicleData(
            timestamp=datetime.now(),
            speed_kmh=round(self.speed, 1),
            rpm=round(self.rpm, 0),
            fuel_level=round(self.fuel, 1),
            coolant_temp=round(self.coolant_temp, 1),
            oil_pressure=round(self.oil_pressure, 2),
            transmission_oil_temp=round(self.transmission_oil_temp, 1)
        )


class VehicleSensorHardware:
    """Interface para leitura real de sensores (OBD2, GPIO, etc.)
    Esta classe seria implementada quando houver hardware real disponível
    """
    
    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 38400):
        """
        Inicializa conexão com o adaptador OBD2 ou sensores GPIO
        
        Args:
            port: Porta serial (ex: /dev/ttyUSB0 no Raspberry Pi)
            baudrate: Velocidade da comunicação serial
        """
        self.port = port
        self.baudrate = baudrate
        self.connected = False
        # Aqui seria feita a conexão real com os sensores
    
    def connect(self) -> bool:
        """Conecta aos sensores"""
        try:
            # Implementar conexão real quando houver hardware
            self.connected = True
            return True
        except Exception as e:
            print(f"Erro ao conectar aos sensores: {e}")
            return False
    
    def disconnect(self):
        """Desconecta dos sensores"""
        self.connected = False
    
    def get_current_data(self) -> Optional[VehicleData]:
        """Lê dados reais dos sensores"""
        if not self.connected:
            return None
        
        try:
            # Implementar leitura real quando houver hardware
            # Isso seria através de:
            # - OBD2Decoders (barramento CAN)
            # - GPIO (Raspberry Pi)
            # - Outros protocolos específicos
            
            return VehicleData(
                timestamp=datetime.now(),
                speed_kmh=0.0,
                rpm=0.0,
                fuel_level=0.0,
                coolant_temp=0.0,
                oil_pressure=0.0,
                transmission_oil_temp=0.0
            )
        except Exception as e:
            print(f"Erro ao ler sensores: {e}")
            return None
