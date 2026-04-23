"""
Testes para o módulo de Sensores Automotivos
"""

import pytest
from vehicle_sensors import VehicleData, VehicleSensorSimulator
from datetime import datetime


class TestVehicleSensorSimulator:
    """Testes do simulador de sensores"""
    
    def test_initialization(self):
        """Testa inicialização do simulador"""
        sensor = VehicleSensorSimulator()
        assert sensor.speed == 0.0
        assert sensor.rpm == 0.0
        assert sensor.fuel == 80.0
        assert sensor.engine_running == False
    
    def test_start_engine(self):
        """Testa ligar o motor"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        assert sensor.engine_running == True
        assert sensor.rpm == 800  # RPM ocioso
        assert sensor.coolant_temp == 20.0
        assert sensor.oil_pressure == 1.5
    
    def test_stop_engine(self):
        """Testa desligar o motor"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        sensor.stop_engine()
        
        assert sensor.engine_running == False
        assert sensor.rpm == 0.0
        assert sensor.speed == 0.0
    
    def test_accelerate(self):
        """Testa aceleração"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        initial_rpm = sensor.rpm
        sensor.accelerate(100)
        
        assert sensor.rpm > initial_rpm
        assert sensor.speed > 0.0
        assert sensor.coolant_temp > 20.0
        assert sensor.oil_pressure > 1.5
    
    def test_decelerate(self):
        """Testa desaceleração"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        sensor.accelerate(500)
        
        initial_rpm = sensor.rpm
        sensor.decelerate(100)
        
        assert sensor.rpm < initial_rpm
        assert sensor.rpm >= 800  # Não desce abaixo de RPM ocioso
    
    def test_consume_fuel(self):
        """Testa consumo de combustível"""
        sensor = VehicleSensorSimulator()
        initial_fuel = sensor.fuel
        
        sensor.consume_fuel(10)
        assert sensor.fuel == initial_fuel - 10
    
    def test_fuel_cannot_go_negative(self):
        """Testa que o combustível não fica negativo"""
        sensor = VehicleSensorSimulator()
        sensor.fuel = 5.0
        sensor.consume_fuel(10)
        
        assert sensor.fuel == 0.0
    
    def test_rpm_limits(self):
        """Testa limites do RPM"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        # Acelerar ao máximo
        for _ in range(100):
            sensor.accelerate(1000)
        
        assert sensor.rpm <= 7000
    
    def test_speed_limits(self):
        """Testa limites de velocidade"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        # Acelerar ao máximo
        for _ in range(100):
            sensor.accelerate(1000)
        
        assert sensor.speed <= 200
    
    def test_temperature_limits(self):
        """Testa limites de temperatura"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        # Acelerar ao máximo
        for _ in range(100):
            sensor.accelerate(1000)
        
        assert sensor.coolant_temp <= 110
        assert sensor.transmission_oil_temp <= 100
        assert sensor.oil_pressure <= 5.0
    
    def test_get_current_data(self):
        """Testa obtenção de dados atuais"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        sensor.accelerate(200)
        
        data = sensor.get_current_data()
        
        assert isinstance(data, VehicleData)
        assert isinstance(data.timestamp, datetime)
        assert data.speed_kmh > 0
        assert data.rpm > 0
        assert 0 <= data.fuel_level <= 100


class TestVehicleData:
    """Testes da classe VehicleData"""
    
    def test_vehicle_data_creation(self):
        """Testa criação de um VehicleData"""
        data = VehicleData(
            timestamp=datetime.now(),
            speed_kmh=100.0,
            rpm=3000.0,
            fuel_level=50.0,
            coolant_temp=90.0,
            oil_pressure=2.5,
            transmission_oil_temp=70.0
        )
        
        assert data.speed_kmh == 100.0
        assert data.rpm == 3000.0
        assert data.fuel_level == 50.0
    
    def test_vehicle_data_string_representation(self):
        """Testa representação em string"""
        data = VehicleData(
            timestamp=datetime.now(),
            speed_kmh=100.0,
            rpm=3000.0,
            fuel_level=50.0,
            coolant_temp=90.0,
            oil_pressure=2.5,
            transmission_oil_temp=70.0
        )
        
        str_repr = str(data)
        assert "100.0" in str_repr
        assert "3000" in str_repr
        assert "50.0" in str_repr


class TestSensorRanges:
    """Testes para ranges de sensores realistas"""
    
    def test_speed_range(self):
        """Testa range realista de velocidade"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        for _ in range(50):
            sensor.accelerate(200)
        
        data = sensor.get_current_data()
        assert 0 <= data.speed_kmh <= 200
    
    def test_rpm_range(self):
        """Testa range realista de RPM"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        data = sensor.get_current_data()
        assert 800 <= data.rpm <= 7000
    
    def test_fuel_range(self):
        """Testa range realista de combustível"""
        sensor = VehicleSensorSimulator()
        
        data = sensor.get_current_data()
        assert 0 <= data.fuel_level <= 100
    
    def test_coolant_temp_range(self):
        """Testa range realista de temperatura do líquido de arrefecimento"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        for _ in range(50):
            sensor.accelerate(200)
        
        data = sensor.get_current_data()
        assert 20 <= data.coolant_temp <= 120
    
    def test_oil_pressure_range(self):
        """Testa range realista de pressão de óleo"""
        sensor = VehicleSensorSimulator()
        sensor.start_engine()
        
        data = sensor.get_current_data()
        assert 1.5 <= data.oil_pressure <= 5.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
