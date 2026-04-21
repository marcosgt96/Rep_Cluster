"""
Exemplos de Integração com Hardware Real
Para adicionar sensores de verdade ao Raspberry Pi
"""

# ============================================================================
# EXEMPLO 1: Integração com Adaptador OBD2 (ELM327 via Serial)
# ============================================================================

"""
Dependência: pip install pyserial obd

Conexão:
- Adaptador ELM327 → USB do Raspberry Pi
- Ou Bluetooth: RFCOMM

Código:
"""

# import obd
# from vehicle_sensors import VehicleData
# from datetime import datetime

# class OBD2SensorReader:
#     def __init__(self, port="/dev/ttyUSB0", baudrate=38400):
#         self.connection = obd.OBD(port)
#         if not self.connection.is_connected():
#             print("Erro: ELM327 não conectado")
#     
#     def read_speed(self) -> float:
#         """Lê velocidade via OBD2"""
#         speed_cmd = obd.commands.SPEED
#         response = self.connection.query(speed_cmd)
#         return response.value.magnitude if response.is_null() == False else 0.0
#     
#     def read_rpm(self) -> float:
#         """Lê RPM via OBD2"""
#         rpm_cmd = obd.commands.RPM
#         response = self.connection.query(rpm_cmd)
#         return response.value.magnitude if response.is_null() == False else 0.0
#     
#     def read_fuel_level(self) -> float:
#         """Lê nível de combustível via OBD2"""
#         fuel_cmd = obd.commands.FUEL_LEVEL
#         response = self.connection.query(fuel_cmd)
#         return response.value.magnitude if response.is_null() == False else 0.0
#     
#     def read_all(self) -> VehicleData:
#         """Lê todos os dados disponíveis"""
#         return VehicleData(
#             timestamp=datetime.now(),
#             speed_kmh=self.read_speed(),
#             rpm=self.read_rpm(),
#             fuel_level=self.read_fuel_level(),
#             coolant_temp=self._get_pid(0x05),  # Coolant Temperature
#             oil_pressure=self._get_pid(0x5D),  # Oil Pressure
#             transmission_oil_temp=0.0  # Pode não estar disponível via OBD2
#         )
#     
#     def _get_pid(self, pid_value) -> float:
#         """Lê um PID específico"""
#         try:
#             cmd = obd.OBDCommand("", "", pid_value)
#             response = self.connection.query(cmd)
#             return float(response.value) if response else 0.0
#         except:
#             return 0.0


# ============================================================================
# EXEMPLO 2: Sensores Analógicos via GPIO (Raspberry Pi)
# ============================================================================

"""
Dependência: pip install adafruit-circuitpython-ads1x15 busio

Conexão (I2C):
- ADS1115 → Raspberry Pi I2C (GPIO 2/3)
- Sensor Analógico → ADS1115 A0-A3

Pinagem Raspberry Pi:
- GPIO 2 (Pin 3) → SDA
- GPIO 3 (Pin 5) → SCL
- GND → GND
- 3.3V → VCC
"""

# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS
# from vehicle_sensors import VehicleData
# from datetime import datetime

# class GPIO_SensorReader:
#     def __init__(self):
#         # Inicializar I2C
#         i2c = busio.I2C(board.SCL, board.SDA)
#         ads = ADS.ADS1115(i2c)
#         
#         # Criar canais (um para cada sensor analógico)
#         self.speed_channel = AnalogIn(ads, ADS.P0)  # Sensor de Velocidade
#         self.fuel_channel = AnalogIn(ads, ADS.P1)   # Sensor de Combustível
#         self.temp_channel = AnalogIn(ads, ADS.P2)   # Sensor de Temperatura
#         self.pressure_channel = AnalogIn(ads, ADS.P3)  # Sensor de Pressão
#     
#     def _analog_to_kmh(self, voltage: float) -> float:
#         """Converte tensão do sensor para km/h"""
#         # Ajustar conforme o sensor: 0-5V = 0-200km/h
#         return (voltage / 3.3) * 200
#     
#     def _analog_to_fuel(self, voltage: float) -> float:
#         """Converte tensão do sensor para % de combustível"""
#         # Ajustar conforme o sensor: 0.3-3.0V = 0-100%
#         return max(0, min(100, ((voltage - 0.3) / 2.7) * 100))
#     
#     def _analog_to_temp(self, voltage: float) -> float:
#         """Converte tensão do sensor para °C"""
#         # NTC Thermistor: tensão → temperatura
#         # Fórmula é específica do sensor usado
#         return (voltage / 3.3) * 150  # Exemplo simplificado
#     
#     def read_all(self) -> VehicleData:
#         return VehicleData(
#             timestamp=datetime.now(),
#             speed_kmh=self._analog_to_kmh(self.speed_channel.voltage),
#             rpm=0.0,  # Não disponível com este setup
#             fuel_level=self._analog_to_fuel(self.fuel_channel.voltage),
#             coolant_temp=self._analog_to_temp(self.temp_channel.voltage),
#             oil_pressure=(self.pressure_channel.voltage / 3.3) * 5.0,
#             transmission_oil_temp=0.0  # Requer segundo sensor de temperatura
#         )


# ============================================================================
# EXEMPLO 3: Sensor Digital via Velocidade (Pulsos)
# ============================================================================

"""
Conexão:
- Sensor magnético/óptico → GPIO do Raspberry Pi
- Conta pulsos por segundo para calcular velocidade

Calibração:
- Pulsos por voltagem: é.g., 4 pulsos = 1 km
"""

# import RPi.GPIO as GPIO
# from vehicle_sensors import VehicleData
# from datetime import datetime
# import time

# class PulseSensorReader:
#     def __init__(self, gpio_pin=17, pulses_per_km=4):
#         self.gpio_pin = gpio_pin
#         self.pulses_per_km = pulses_per_km
#         self.pulse_count = 0
#         self.last_reset = datetime.now()
#         
#         # Configurar GPIO
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(gpio_pin, GPIO.IN)
#         GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback=self._pulse_callback)
#     
#     def _pulse_callback(self, channel):
#         """Callback para cada pulso"""
#         self.pulse_count += 1
#     
#     def get_speed(self) -> float:
#         """Calcula velocidade baseado em pulsos"""
#         now = datetime.now()
#         elapsed = (now - self.last_reset).total_seconds()
#         
#         if elapsed >= 1.0:  # Atualiza a cada segundo
#             # Pulsos por segundo = velocidade em km/s * pulses_per_km
#             speed_kmh = (self.pulse_count / self.pulses_per_km / elapsed) * 3.6
#             self.pulse_count = 0
#             self.last_reset = now
#             return speed_kmh
#         
#         return 0.0


# ============================================================================
# EXEMPLO 4: CAN Bus (Barramento Veicular Nativo)
# ============================================================================

"""
Dependência: pip install python-can

Hardware necessário:
- Interface CAN → Raspberry Pi (via SPI ou USB)
- Exemplo: MCP2515 via SPI com transceptor TJA1050

Conexão MCP2515:
- CS → GPIO 8 (CE0)
- CLK → GPIO 11 (SCLK)
- MOSI → GPIO 10 (MOSI)
- MISO → GPIO 9 (MISO)
- INT → GPIO 7 (CE1)
- GND → GND
- VCC → 3.3V
"""

# import can
# from vehicle_sensors import VehicleData
# from datetime import datetime

# class CANBusSensorReader:
#     def __init__(self, channel='can0', bitrate=500000):
#         """
#         Inicializa leitor CAN Bus
#         
#         Configurar interface:
#         sudo ip link set can0 up type can bitrate 500000
#         """
#         self.bus = can.interface.Bus(channel=channel, bustype='socketcan', bitrate=bitrate)
#         self.pids = {}
#     
#     def _parse_message(self, msg: can.Message):
#         """Parse de mensagem CAN"""
#         # IDs comuns no CAN:
#         # 0x100 = Engine data (RPM, Speed)
#         # 0x200 = Fuel data
#         # 0x300 = Temperature sensors
#         
#         if msg.arbitration_id == 0x100:
#             self.pids['rpm'] = int.from_bytes(msg.data[0:2], 'big') / 4
#             self.pids['speed'] = msg.data[2]
#         elif msg.arbitration_id == 0x200:
#             self.pids['fuel'] = (msg.data[0] / 255) * 100
#         elif msg.arbitration_id == 0x300:
#             self.pids['coolant_temp'] = msg.data[0] - 40
#             self.pids['oil_temp'] = msg.data[1] - 40
#     
#     def read_all(self) -> VehicleData:
#         """Lê mensagens do barramento CAN"""
#         # Processar mensagens recebidas
#         msg = self.bus.recv(timeout=1.0)
#         if msg:
#             self._parse_message(msg)
#         
#         return VehicleData(
#             timestamp=datetime.now(),
#             speed_kmh=self.pids.get('speed', 0.0),
#             rpm=self.pids.get('rpm', 0.0),
#             fuel_level=self.pids.get('fuel', 0.0),
#             coolant_temp=self.pids.get('coolant_temp', 0.0),
#             oil_pressure=0.0,
#             transmission_oil_temp=self.pids.get('oil_temp', 0.0)
#         )


# ============================================================================
# EXEMPLO 5: Integração no cluster_gui.py
# ============================================================================

"""
Para usar sensores reais, modifique cluster_gui.py:

# No lugar de:
self.sensor = VehicleSensorSimulator()

# Use:
from hardware_sensors import OBD2SensorReader  # ou GPIO_SensorReader, etc
self.sensor = OBD2SensorReader("/dev/ttyUSB0")

# E na função _update_display() modifique:
data = self.sensor.read_all()  # Em vez de get_current_data()
"""


# ============================================================================
# Dicas e Boas Práticas
# ============================================================================

"""
1. CALIBRAÇÃO DE SENSORES:
   - Cada sensor tem uma curva de resposta diferente
   - Medir em pontos conhecidos (ex: 0, 50, 100%)
   - Criar funções de mapeamento (mapping)
   - Usar splines para precisão melhor

2. FILTRAGEM DE RUÍDO:
   - Implementar média móvel (moving average)
   - Usar filtro Kalman para dados GPS/GNSS
   - Descartar outliers

3. TAXA DE ATUALIZAÇÃO:
   - OBD2: 10-100 ms (depende do adaptador)
   - GPIO: até 100 kHz (sensor dependente)
   - CAN Bus: 100-1000 ms

4. SEGURANÇA:
   - Validar todos os dados recebidos
   - Implementar timeouts
   - Logging de erros
   - Proteção contra valores impossíveis

5. PERFORMANCE:
   - Threading para não bloquear GUI
   - Cache de dados se necessário
   - Reduzir frequência de atualização em recursos baixos

6. TESTES:
   - Simular falhas de sensores
   - Testar limites de valores
   - Verificar comportamento em condições extremas
"""
