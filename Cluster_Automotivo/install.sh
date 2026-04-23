#!/bin/bash
# ============================================
# Script de Instalação - Cluster Automotivo
# Raspberry Pi OS
# ============================================

set -e

echo "============================================"
echo "  🚗 Cluster Automotivo - Instalação"
echo "============================================"

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Função para exibir mensagens
info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Verificar se é Raspberry Pi
if [ ! -f /proc/cpuinfo ]; then
    warn "Este script é otimizado para Raspberry Pi, mas pode funcionar em outros sistemas Linux"
fi

# ============================================
# Passo 1: Atualizar sistema
# ============================================
info "Atualizando sistema..."
sudo apt update
sudo apt upgrade -y

# ============================================
# Passo 2: Instalar dependências
# ============================================
info "Instalando dependências..."

# Python e pip
sudo apt install -y python3 python3-pip python3-venv

# Tkinter (necessário para GUI)
sudo apt install -y python3-tk

# Dependências opcionais para hardware
read -p "Deseja instalar dependências para hardware real? (OBD2, GPIO, CAN) [s/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    info "Instalando dependências de hardware..."
    sudo apt install -y python3-serial python3-can
    
    # Instalar bibliotecas Python adicionais
    pip3 install pyserial python-can
    
    warn "Nota: RPi.GPIO só funciona em Raspberry Pi real"
fi

# ============================================
# Passo 3: Criar diretório do projeto
# ============================================
info "Criando diretório do projeto..."

PROJECT_DIR="/home/$USER/Cluster_Automotivo"

if [ -d "$PROJECT_DIR" ]; then
    warn "Diretório já existe. Deseja atualizar? [s/N]: "
    read -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        cd "$PROJECT_DIR"
        git pull origin main 2>/dev/null || warn "Não foi possível atualizar via git"
    fi
else
    # Criar diretório
    mkdir -p "$PROJECT_DIR"
    echo "Por favor, copie os arquivos do projeto para: $PROJECT_DIR"
fi

# ============================================
# Passo 4: Instalar dependências Python do projeto
# ============================================
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    info "Instalando dependências Python do projeto..."
    cd "$PROJECT_DIR"
    pip3 install -r requirements.txt
else
    warn "requirements.txt não encontrado. Instalando dependências básicas..."
    pip3 install pytest pytest-cov
fi

# ============================================
# Passo 5: Testar instalação
# ============================================
info "Testando instalação..."

cd "$PROJECT_DIR"

# Testar importações
python3 -c "from vehicle_sensors import VehicleSensorSimulator; print('✓ vehicle_sensors OK')" || error "Falha ao importar vehicle_sensors"

# Testar GUI (sem display)
python3 -c "import tkinter; print('✓ Tkinter OK')" || error "Tkinter não está instalado"

# ============================================
# Passo 6: Configurar inicialização automática (Opcional)
# ============================================
read -p "Deseja configurar inicialização automática? [s/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    info "Configurando inicialização automática..."
    
    # Criar serviço systemd
    sudo tee /etc/systemd/system/cluster.service > /dev/null << 'EOF'
[Unit]
Description=Vehicle Cluster Display
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Cluster_Automotivo
ExecStart=/usr/bin/python3 /home/pi/Cluster_Automotivo/cluster_gui.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    # Ativar serviço
    sudo systemctl daemon-reload
    sudo systemctl enable cluster
    
    info "Serviço criado. Para iniciar: sudo systemctl start cluster"
fi

# ============================================
# Conclusão
# ============================================
echo ""
echo "============================================"
echo -e "${GREEN}  ✅ Instalação Concluída!${NC}"
echo "============================================"
echo ""
echo "Para executar o cluster:"
echo "  cd $PROJECT_DIR"
echo "  python3 cluster_gui.py"
echo ""
echo "Para executar testes:"
echo "  pytest tests/test_vehicle_sensors.py -v"
echo ""