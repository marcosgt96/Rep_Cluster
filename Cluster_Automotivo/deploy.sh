#!/bin/bash
# ============================================
# Script de Deploy - Cluster Automotivo
# Para macOS/Linux - Copia arquivos para Raspberry Pi
# ============================================

set -e

echo "============================================"
echo "  🚗 Cluster Automotivo - Deploy para Raspberry"
echo "============================================"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info() { echo -e "${GREEN}[INFO]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# ============================================
# Configurações - ALTERE ESTES VALORES
# ============================================
RPI_HOST="${RPI_HOST:-cluster-automotivo.local}"
RPI_USER="${RPI_USER:-pi}"
RPI_PASSWORD="${RPI_PASSWORD:-cluster123}"
RPI_PATH="/home/pi/Cluster_Automotivo"

echo "Configurações:"
echo "  Host: $RPI_HOST"
echo "  Usuário: $RPI_USER"
echo "  Caminho: $RPI_PATH"
echo

# Verificar se SSH está disponível
if ! command -v scp &> /dev/null; then
    error "SCP não encontrado. Instale OpenSSH."
    exit 1
fi

# ============================================
# PASSO 1: Criar diretório remoto
# ============================================
info "Criando diretório remoto..."

# Usar sshpass se disponível, caso contrário usar expect
if command -v sshpass &> /dev/null; then
    sshpass -p "$RPI_PASSWORD" ssh -o StrictHostKeyChecking=no \
        "$RPI_USER@$RPI_HOST" "mkdir -p $RPI_PATH"
else
    # Tentativa sem sshpass (pode pedir senha)
    echo "sshpass não encontrado. Tentando sem senha..."
    echo "Você precisará inserir a senha quando solicitado."
    ssh -o StrictHostKeyChecking=no "$RPI_USER@$RPI_HOST" "mkdir -p $RPI_PATH" || {
        error "Falha ao conectar. Instale sshpass: brew install sshpass (macOS) ou apt install sshpass (Linux)"
        exit 1
    }
fi

# ============================================
# PASSO 2: Copiar arquivos
# ============================================
info "Copiando arquivos..."

COPY_CMD="sshpass -p '$RPI_PASSWORD' scp -o StrictHostKeyChecking=no"
if ! command -v sshpass &> /dev/null; then
    COPY_CMD="scp -o StrictHostKeyChecking=no"
fi

# Arquivos principais
$COPY_CMD vehicle_sensors.py "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD cluster_gui.py "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD cluster_demo.py "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD cluster_quick_test.py "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD cluster_setup.py "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD requirements.txt "$RPI_USER@$RPI_HOST:$RPI_PATH/"
$COPY_CMD install.sh "$RPI_USER@$RPI_HOST:$RPI_PATH/"

# Pasta tests
$COPY_CMD -r tests "$RPI_USER@$RPI_HOST:$RPI_PATH/"

info "Arquivos copiados com sucesso!"

# ============================================
# PASSO 3: Instalar dependências
# ============================================
info "Instalando dependências..."

RUN_CMD="sshpass -p '$RPI_PASSWORD' ssh -o StrictHostKeyChecking=no"
if ! command -v sshpass &> /dev/null; then
    RUN_CMD="ssh -o StrictHostKeyChecking=no"
fi

$RUN_CMD "$RPI_USER@$RPI_HOST" "cd $RPI_PATH && pip3 install -r requirements.txt"

# ============================================
# PASSO 4: Testar
# ============================================
info "Testando instalação..."

$RUN_CMD "$RPI_USER@$RPI_HOST" "cd $RPI_PATH && python3 -c 'from vehicle_sensors import VehicleSensorSimulator; print(OK)'"

echo ""
echo "============================================"
echo -e "${GREEN}  ✅ Deploy Concluído!${NC}"
echo "============================================"
echo ""
echo "Para executar no Raspberry:"
echo "  ssh $RPI_USER@$RPI_HOST"
echo "  cd $RPI_PATH"
echo "  python3 cluster_gui.py"
echo ""