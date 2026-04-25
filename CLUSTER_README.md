# 🚗 Cluster Automotivo - Painel de Instrumento Digital

Um sistema completo de **painel de instrumento digital** para veículos, otimizado para executar em **Raspberry Pi**. Exibe em tempo real:

- 🏎️ **Velocidade** (km/h)
- ⚙️ **RPM** (Rotações por minuto)
- ⛽ **Nível de Combustível** (%)
- 🌡️ **Temperatura do Líquido de Arrefecimento** (°C)
- 💧 **Pressão de Óleo do Motor** (bar)
- 🔥 **Temperatura do Óleo da Transmissão** (°C)

## 📋 Componentes do Sistema

### 1. **vehicle_sensors.py**
Módulo principal contém:
- `VehicleData`: Classe para armazenar dados dos sensores
- `VehicleSensorSimulator`: Simulador de sensores para testes
- `VehicleSensorHardware`: Interface preparada para sensores reais (OBD2, GPIO)

### 2. **cluster_gui.py**
Interface gráfica Tkinter otimizada para Raspberry Pi com:
- Display grande para Velocidade e RPM
- Indicadores menores para outros sensores
- Tema escuro (estilo automotivo)
- Compatível com telas de pequeno tamanho
- Botões de simulação (ligar, desligar, acelerar, desacelerar)

### 3. **cluster_demo.py**
Script de demonstração com vários cenários:
- Partida do motor
- Aceleração progressiva
- Condução normal
- Velocidade alta
- Resfriamento após desligamento
- Simulação de condições de alerta

## 🚀 Como Usar

### Instalação

1. **Clonar ou baixar o projeto:**
```bash
cd ~/Testes\ Python/GC_sistem\ 0.1.3/
```

2. **Instalar dependências:**
```bash
# No Raspberry Pi ou Linux
pip install -r requirements.txt

# Ou instalar manualmente
pip install pytest
```

### Executar a GUI do Cluster (Modo Simulação)

```bash
python cluster_gui.py
```

**Funcionalidades:**
- ▶ Ligar: Inicia o motor (simula 800 RPM)
- ⏹ Desligar: Para o motor
- ⬆ Acelerar: Aumenta velocidade e RPM
- ⬇ Desacelerar: Diminui velocidade e RPM

### Executar Demonstração

```bash
python cluster_demo.py
```

Executa 6 cenários consecutivos de simulação com exibição de dados em tempo real.

### Executar Testes

```bash
# Todos os testes
pytest tests/test_vehicle_sensors.py -v

# Um teste específico
pytest tests/test_vehicle_sensors.py::TestVehicleSensorSimulator::test_accelerate -v
```

## 💻 Instalação no Raspberry Pi

### Requisitos Mínimos
- Raspberry Pi 3B+ ou superior
- Raspbian/Raspberry Pi OS
- Python 3.7+
- Tela HDMI ou touchscreen (7-10")

### Passo 1: Preparar o Raspberry Pi

```bash
sudo apt update
sudo apt upgrade -y

# Instalar Python e pip
sudo apt install -y python3 python3-pip

# Instalar dependências de GUI (se não tiver)
sudo apt install -y python3-tk
```

### Passo 2: Instalar o Projeto

```bash
cd ~/Documents
git clone <seu-repositorio> # ou copie os arquivos
cd GC_sistem\ 0.1.3

# Instalar dependências Python
pip install -r requirements.txt
```

### Passo 3: Executar em Fullscreen (recomendado)

O script `cluster_gui.py` já possui suporte a fullscreen:

```bash
# Modo fullscreen
python cluster_gui.py

# Modo janelado (para testes)
# Edite cluster_gui.py e mude: fullscreen=False
```

### Passo 4: Iniciar Automaticamente (Opcional)

Para iniciar o cluster ao ligar o Raspberry Pi:

```bash
# Editar arquivo de inicialização
nano ~/.bashrc

# Adicionar ao final:
# python3 /home/pi/Documents/GC_sistem\ 0.1.3/cluster_gui.py
```

Ou usar systemd:

```bash
sudo nano /etc/systemd/system/cluster.service
```

Copiar:
```ini
[Unit]
Description=Vehicle Cluster Display
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Documents/GC_sistem\ 0.1.3
ExecStart=/usr/bin/python3 /home/pi/Documents/GC_sistem\ 0.1.3/cluster_gui.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Depois:
```bash
sudo systemctl daemon-reload
sudo systemctl enable cluster
sudo systemctl start cluster
```

## 🔌 Integração com Hardware Real (OBD2, GPIO)

Quando tiver hardware real conectado:

### 1. Para Adaptador OBD2:

```python
from vehicle_sensors import VehicleSensorHardware
from cluster_gui import ClusterDisplay

# Usar hardware real em vez de simulador
app = ClusterDisplay(use_hardware=True)
app.mainloop()
```

Será necessário implementar:
- Conexão serial com adaptador OBD2
- Decodificação de comandos PID (Parameter ID)
- Filtros de dados e suavização

### 2. Para GPIO (Sensores Diretos):

```python
import RPi.GPIO as GPIO
from vehicle_sensors import VehicleSensorHardware

# O módulo VehicleSensorHardware pode ser estendido para:
# - Leitura de sensores analógicos via ADC
# - Sensores digitais conectados a GPIO
# - CAN Bus (barramento veicular)
```

## 📊 Estrutura de Dados

```python
@dataclass
class VehicleData:
    timestamp: datetime      # Quando os dados foram lidos
    speed_kmh: float         # 0-200+ km/h
    rpm: float              # 0-7000 rpm
    fuel_level: float       # 0-100%
    coolant_temp: float     # 20-120°C
    oil_pressure: float     # 0-5 bar
    transmission_oil_temp: float  # 40-100°C
```

## 🎨 Personalização

### Alterar Cores
Edit `cluster_gui.py` e procure por `#1a1a1a` (cores hex):
- `#1a1a1a` = Fundo preto
- `#00ff00` = Verde (texto/bordas)
- `#222222` = Cinza escuro (painéis)

### Alterar Tamanho de Fonte
No método `_create_widgets()`, procure por `font.Font()` e altere `size`.

### Alterar Intervalo de Atualização
Altere `self.update_interval = 100` (em ms) em `ClusterDisplay.__init__()`.

## 🧪 Estrutura de Testes

```
tests/
├── test_vehicle_sensors.py    # Testes unitários dos sensores
│   ├── TestVehicleSensorSimulator
│   ├── TestVehicleData
│   └── TestSensorRanges
└── test_models.py             # Testes do sistema de vendas original
```

### Executar com Cobertura

```bash
pip install pytest-cov
pytest tests/test_vehicle_sensors.py --cov=vehicle_sensors
```

## 📝 Logs e Dados

O sistema pode ser expandido para:
- Registrar dados em banco de dados SQLite
- Exportar CSV para análise
- WebSocket em tempo real
- Dashboard web

Exemplo de expand integrado com `db.py` existente:

```python
# Adicione à db.py
def log_vehicle_data(data: VehicleData):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vehicle_logs (timestamp, speed, rpm, fuel, coolant_temp, oil_pressure, transmission_temp) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (data.timestamp, data.speed_kmh, data.rpm, data.fuel_level, 
         data.coolant_temp, data.oil_pressure, data.transmission_oil_temp)
    )
    conn.commit()
    conn.close()
```

## ⚠️ Avisos de Segurança

Implementados na GUI:
- Combustível < 10%: Aviso visual
- Temperatura > 110°C: Alerta crítico
- Pressão óleo < 1.0 bar: Aviso
- RPM > 6500: Aviso

## 🔧 Troubleshooting

### GUI não abre no Raspberry Pi
```bash
# Verificar display
echo $DISPLAY
export DISPLAY=:0  # ou :0.0

# Executar com mais verbosidade
python -u cluster_gui.py
```

### Erro de importação Tkinter
```bash
sudo apt install python3-tk
```

### Performance lenta
- Aumentar intervalo: `self.update_interval = 200`
- Desabilitar algumas cores/efeitos

## 📚 Referências

- [Raspberry Pi GPIO](https://www.raspberrypi.com/documentation/computers/gpio.html)
- [OBD2 Protocol](https://en.wikipedia.org/wiki/OBD-II_PIDs)
- [Python Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CAN Bus (automotive)](https://en.wikipedia.org/wiki/CAN_bus)

## 📄 Licença

Este projeto é fornecido como está, para fins educacionais e de desenvolvimento.

## 👤 Autor

Desenvolvido como sistema de aprendizado para Python em Raspberry Pi.

---

**Versão:** 1.0.0  
**Data:** 2026-04-13  
**Status:** ✅ Funcional em simulação | 🔄 Pronto para hardware real
