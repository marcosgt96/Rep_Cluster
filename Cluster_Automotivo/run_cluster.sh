#!/bin/bash
# Script para executar o Cluster Automotivo com ambiente virtual
# Otimizado para DietPi e Raspberry Pi

# Diretório do script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/logs"
LOG_FILE="${LOG_DIR}/cluster_$(date +%Y%m%d_%H%M%S).log"

# Criar diretório de logs se não existir
mkdir -p "$LOG_DIR"

# Função para logging
log_msg() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_msg "========== Iniciando Cluster Automotivo =========="
log_msg "Diretório: $SCRIPT_DIR"

# Mudar para o diretório da aplicação
cd "$SCRIPT_DIR" || exit 1

# Verificar se Python3 está instalado
if ! command -v python3 &> /dev/null; then
    log_msg "ERRO: Python3 não encontrado. Instale com: sudo apt install python3"
    exit 1
fi

log_msg "Python3: $(python3 --version)"

# Verificar se o ambiente virtual existe
if [ ! -d "cluster_env" ]; then
    log_msg "Criando ambiente virtual..."
    python3 -m venv cluster_env
    if [ $? -ne 0 ]; then
        log_msg "ERRO: Falha ao criar ambiente virtual"
        exit 1
    fi
    log_msg "Ambiente virtual criado com sucesso"
fi

# Ativar ambiente virtual
log_msg "Ativando ambiente virtual..."
source cluster_env/bin/activate
if [ $? -ne 0 ]; then
    log_msg "ERRO: Falha ao ativar ambiente virtual"
    exit 1
fi

# Instalar dependências se necessário
if [ ! -f "cluster_env/.dependencies_installed" ]; then
    log_msg "Instalando dependências..."
    pip install --upgrade pip >> "$LOG_FILE" 2>&1
    pip install -r requirements.txt >> "$LOG_FILE" 2>&1
    if [ $? -eq 0 ]; then
        touch "cluster_env/.dependencies_installed"
        log_msg "Dependências instaladas com sucesso"
    else
        log_msg "AVISO: Falha ao instalar algumas dependências"
    fi
fi

# Executar o cluster
log_msg "Iniciando Cluster Automotivo..."
log_msg "Acesse em: http://$(hostname -I | awk '{print $1}'):5000"
python3 cluster_gui.py >> "$LOG_FILE" 2>&1

# Capturar código de saída
EXIT_CODE=$?

# Desativar ambiente virtual
deactivate

if [ $EXIT_CODE -ne 0 ]; then
    log_msg "ERRO: Cluster encerrou com erro (código: $EXIT_CODE)"
else
    log_msg "Cluster encerrado normalmente"
fi

log_msg "========== Fim da execução =========="

exit $EXIT_CODE

# Instruções:
# 1. Salve este script como run_cluster.sh no diretório do Cluster Automotivo.
# 2. Dê permissão de execução: chmod +x run_cluster.sh
# 3. Execute o script: ./run_cluster.sh
