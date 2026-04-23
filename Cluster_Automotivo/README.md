# 🚗 Cluster Automotivo
**Painel de Instrumento Digital para Veículos**

Sistema completo de painel de instrumento digital otimizado para Raspberry Pi, simulando todos os sensores de um veículo automotivo.

## 📋 Funcionalidades

- ✅ **Simulador de Sensores**: 6 sensores automotivos simulados realisticamente
- ✅ **Interface Web**: Painel digital moderno servido por Flask e Socket.IO
- ✅ **HTML standalone**: `index.html` funciona como demo offline
- ✅ **Cenários de Simulação**: 6 cenários diferentes de condução
- ✅ **Controles Interativos**: Botões e atualizações em tempo real
- ✅ **Testes Unitários**: 18 testes validando toda a lógica
- ✅ **Otimização Raspberry Pi**: Compatível com telas 7-10"
- ✅ **Exemplos de Hardware**: Integração com OBD2, GPIO, CAN Bus

## 🎯 Sensores Implementados

| Sensor | Unidade | Range | Descrição |
|--------|---------|-------|-----------|
| 🏎️ **Velocidade** | km/h | 0-200 | Velocidade do veículo |
| ⚙️ **RPM** | rpm | 0-7000 | Rotações por minuto |
| ⛽ **Combustível** | % | 0-100 | Nível do tanque |
| 🌡️ **Temp. Arrefecimento** | °C | 20-120 | Líquido do motor |
| 💧 **Pressão Óleo** | bar | 0-5 | Óleo do motor |
| 🔥 **Temp. Transmissão** | °C | 40-100 | Óleo da transmissão |

## 🚀 Como Usar

### Instalação

```bash
cd Cluster_Automotivo
pip install -r requirements.txt
```

### Executar o Sistema

```bash
# Teste rápido (5 minutos)
python cluster_quick_test.py

# Demonstração completa (10 minutos)
python cluster_demo.py

# Interface web completa
python cluster_gui.py

# Abrir demo HTML standalone
start index.html  # Windows
xdg-open index.html  # Linux
open index.html  # macOS

# Menu interativo
python cluster_setup.py

# Executar testes
pytest tests/test_vehicle_sensors.py -v
```

### Acesso à interface web

- Abra `http://localhost:5000` no navegador após executar `python cluster_gui.py`
- A página usa Socket.IO para dados em tempo real
- `index.html` também roda offline com simulação de dados

## 📁 Estrutura do Projeto

```
Cluster_Automotivo/
├── vehicle_sensors.py              # Módulo principal de sensores
├── cluster_gui.py                  # Servidor web Flask + Socket.IO
├── index.html                      # Interface web standalone / demo
├── cluster_demo.py                 # Cenários de simulação
├── cluster_quick_test.py           # Teste visual rápido
├── cluster_setup.py                # Menu interativo
├── CLUSTER_README.md               # Documentação completa
├── CLUSTER_INDEX.py                # Índice e guia rápido
├── hardware_integration_examples.py # Exemplos de hardware
├── requirements.txt                # Dependências
└── tests/
    ├── __init__.py
    └── test_vehicle_sensors.py     # 18 testes unitários
```

## 🎮 Cenários de Simulação

### 1. **Partida do Motor**
- Simula ligar o motor
- RPM sobe para 800 (ocioso)
- Temperaturas começam frias

### 2. **Aceleração Progressiva**
- Aceleração gradual até ~100 km/h
- Aquecimento do motor
- Consumo de combustível

### 3. **Condução Normal**
- Simulação de 10 segundos de condução
- Variações realistas de velocidade
- Consumo contínuo

### 4. **Velocidade Alta**
- Aceleração até ~200 km/h
- Máximos RPM e temperaturas
- Consumo elevado

### 5. **Resfriamento**
- Motor desligado
- Temperaturas diminuem gradualmente

### 6. **Condições de Alerta**
- Combustível crítico (< 10%)
- Temperatura alta (> 110°C)
- Pressão de óleo baixa (< 1.0 bar)

## 🖥️ Interface Web

O sistema agora oferece uma interface web moderna:

- `cluster_gui.py` serve a GUI web via Flask e Socket.IO
- `index.html` pode ser aberto diretamente no navegador como demo
- Atualizações em tempo real mostram RPM, velocidade, combustível, temperaturas, bateria, marcha, odômetro e alertas
- Interface compatível com demo offline quando não há servidor Python conectado

### Layout
- **Topo**: Velocidade e RPM (grandes)
- **Centro**: Combustível, Temp. Arrefecimento, Pressão Óleo, Temp. Transmissão
- **Fundo**: Controles e status

### Controles
- ▶ **Ligar**: Inicia o motor
- ⏹ **Desligar**: Para o motor
- Exibe marcha, odômetro, trip A/B, CAN BUS e status em tempo real

### Tema
- Fundo escuro com visual neon
- Elementos em laranja, verde e azul para leitura rápida
- Layout responsivo para tela cheia

## 🧪 Testes

```bash
# Todos os testes
pytest tests/test_vehicle_sensors.py -v

# Com cobertura
pytest tests/test_vehicle_sensors.py --cov=vehicle_sensors

# Teste específico
pytest tests/test_vehicle_sensors.py::TestVehicleSensorSimulator::test_accelerate -v
```

**Cobertura**: 18 testes unitários validando:
- Inicialização de sensores
- Liga/desliga motor
- Aceleração/desaceleração
- Limites de valores
- Consumo de combustível
- Ranges realistas

## 💻 Requisitos do Sistema

### Desenvolvimento
- **Python**: 3.7+
- **Flask**: servidor web
- **Flask-SocketIO**: atualização em tempo real
- **pytest**: para testes

### Produção (Raspberry Pi)
- **Raspberry Pi**: 3B+ ou superior
- **SO**: Raspbian/Raspberry Pi OS
- **Tela**: HDMI ou touchscreen 7-10"
- **Memória**: 1GB+ RAM

> Observação: `python3-tk` é opcional se você utilizar apenas a interface web. Instale-o apenas para scripts que dependem de Tkinter.

## 🔌 Integração com Hardware Real

### OBD2 (Adaptador ELM327)
```python
# Exemplo de uso
from hardware_integration_examples import OBD2SensorReader

sensor = OBD2SensorReader("/dev/ttyUSB0")
data = sensor.read_all()
print(f"Velocidade: {data.speed_kmh} km/h")
```

### GPIO (Sensores Diretos)
```python
# Exemplo com ADS1115
from hardware_integration_examples import GPIO_SensorReader

sensor = GPIO_SensorReader()
data = sensor.read_all()
print(f"RPM: {data.rpm}")
```

### CAN Bus (Barramento Veicular)
```python
# Exemplo com MCP2515
from hardware_integration_examples import CANBusSensorReader

sensor = CANBusSensorReader('can0')
data = sensor.read_all()
print(f"Combustível: {data.fuel_level}%")
```

## 📊 Arquitetura

### Classes Principais

```python
@dataclass
class VehicleData:
    timestamp: datetime
    speed_kmh: float
    rpm: float
    fuel_level: float
    coolant_temp: float
    oil_pressure: float
    transmission_oil_temp: float

class VehicleSensorSimulator:
    # Simulador completo de sensores
    def start_engine(self)
    def accelerate(self, delta)
    def get_current_data(self) -> VehicleData

class ClusterWebApp:
    # Servidor Flask que entrega a interface web
    def run(self)
```

## 🎨 Personalização

### Alterar Cores
```python
# Em cluster_gui.py
self.configure(bg='#1a1a1a')  # Fundo
# Texto: fg='#00ff00' (verde)
```

### Alterar Intervalo de Atualização
```python
# Em cluster_gui.py
# Ajuste o loop de atualização ou a taxa de envio de dados
# Exemplo: sleep(0.1) para atualizações a cada 100 ms
```

### Adicionar Novos Sensores
1. Adicionar em `VehicleData`
2. Implementar em `VehicleSensorSimulator`
3. Expor novos dados em `cluster_gui.py`
4. Adicionar testes

## 🚨 Sistema de Alertas

### Alertas Implementados
- **Combustível**: < 10% → "COMBUSTÍVEL CRITICO"
- **Temperatura**: > 110°C → "TEMPERATURA DO MOTOR CRITICA"
- **Pressão Óleo**: < 1.0 bar → "PRESSÃO DE ÓLEO BAIXA"

### Como Expandir
```python
# Em cluster_gui.py
def _check_alerts(self, data):
    alerts = []
    if data.fuel_level < 10:
        alerts.append("COMBUSTÍVEL CRITICO")
    # Adicionar mais alertas...
    return alerts
```

## 📈 Próximas Funcionalidades

- [ ] Dashboard web em tempo real
- [ ] Logging de dados em SQLite
- [ ] Alertas por email/SMS
- [ ] Modo noturno/diurno automático
- [ ] Suporte a múltiplos idiomas
- [ ] Touchscreen customizado
- [ ] Integração GPS
- [ ] Análise de consumo

## 📋 Dependências

```txt
Flask>=2.0.0
Flask-SocketIO>=5.0.0
pytest>=7.0.0
pytest-cov>=4.0.0

# Opcionais para hardware real:
# pyserial>=3.5          # OBD2
# RPi.GPIO>=0.7.0       # GPIO Raspberry
# python-can>=4.0.0     # CAN Bus
# adafruit-circuitpython-ads1x15>=1.3.0  # ADS1115
```

## 🚀 Instalação no Raspberry Pi

### Passo 1: Preparar o Sistema
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3-pip
```

### Passo 2: Instalar Projeto
```bash
cd ~/Documents
# Copiar arquivos do projeto
cd Cluster_Automotivo
pip install -r requirements.txt
```

### Passo 3: Executar
```bash
# Teste
python cluster_quick_test.py

# Produção (interface web)
python cluster_gui.py
```

### Passo 4: Inicialização Automática
```bash
# Criar serviço systemd
sudo nano /etc/systemd/system/cluster.service

# Conteúdo:
[Unit]
Description=Vehicle Cluster Display
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Documents/Cluster_Automotivo
ExecStart=/usr/bin/python3 cluster_gui.py
Restart=always

[Install]
WantedBy=multi-user.target

# Habilitar e iniciar
sudo systemctl daemon-reload
sudo systemctl enable cluster
sudo systemctl start cluster
```

## 📄 Licença

Este projeto é para fins educacionais e de desenvolvimento.

---

**Versão:** 1.0.0  
**Data:** 13 de abril de 2026  
**Status:** ✅ Funcional | 🔄 Pronto para hardware real