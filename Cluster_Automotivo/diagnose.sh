#!/bin/bash
# Script de diagnóstico - Cluster Automotivo DietPi
# Use: bash diagnose.sh

echo "╔════════════════════════════════════════════════════╗"
echo "║  DIAGNÓSTICO - CLUSTER AUTOMOTIVO DIETPI          ║"
echo "║  $(date '+%Y-%m-%d %H:%M:%S')                           ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $1"
    else
        echo -e "${RED}✗${NC} $1"
    fi
}

check_command() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}✓${NC} $1 instalado"
    else
        echo -e "${RED}✗${NC} $1 NÃO instalado"
    fi
}

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣  REQUISITOS DO SISTEMA"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "Python 3:"
python3 --version 2>/dev/null
check "Python3 disponível"
echo ""

echo "pip:"
python3 -m pip --version 2>/dev/null
check "pip disponível"
echo ""

echo "venv:"
python3 -c "import venv" 2>/dev/null
check "venv disponível"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2️⃣  DIRETÓRIOS E ARQUIVOS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

APP_DIR="$HOME/Rep_Cluster/Cluster_Automotivo"

if [ -d "$APP_DIR" ]; then
    echo -e "${GREEN}✓${NC} Diretório encontrado: $APP_DIR"
else
    echo -e "${RED}✗${NC} Diretório NÃO encontrado: $APP_DIR"
    exit 1
fi
echo ""

# Verificar arquivos
for file in "cluster_gui.py" "run_cluster.sh" "requirements.txt" "cluster-automotivo.service"; do
    if [ -f "$APP_DIR/$file" ]; then
        echo -e "${GREEN}✓${NC} $file existe"
    else
        echo -e "${RED}✗${NC} $file FALTA"
    fi
done
echo ""

# Verificar permissões do script
if [ -x "$APP_DIR/run_cluster.sh" ]; then
    echo -e "${GREEN}✓${NC} run_cluster.sh é executável"
else
    echo -e "${YELLOW}⚠${NC} run_cluster.sh NÃO é executável"
    echo "   Execute: chmod +x $APP_DIR/run_cluster.sh"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  AMBIENTE VIRTUAL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -d "$APP_DIR/cluster_env" ]; then
    echo -e "${GREEN}✓${NC} Ambiente virtual existe"
    
    if [ -f "$APP_DIR/cluster_env/bin/activate" ]; then
        echo -e "${GREEN}✓${NC} Ambiente virtual é válido"
        
        # Testar ativação
        source "$APP_DIR/cluster_env/bin/activate" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓${NC} Ambiente virtual ativa corretamente"
            
            # Verificar dependências
            echo ""
            echo "Pacotes instalados:"
            pip list 2>/dev/null | grep -E "Flask|SocketIO"
            
            deactivate
        else
            echo -e "${RED}✗${NC} Erro ao ativar ambiente virtual"
        fi
    else
        echo -e "${RED}✗${NC} Ambiente virtual está corrompido"
    fi
else
    echo -e "${YELLOW}⚠${NC} Ambiente virtual NÃO existe"
    echo "   Será criado na primeira execução"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  SERVIÇO SYSTEMD"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -f "/etc/systemd/system/cluster-automotivo.service" ]; then
    echo -e "${GREEN}✓${NC} Arquivo de serviço instalado"
else
    echo -e "${YELLOW}⚠${NC} Arquivo de serviço NÃO encontrado"
    echo "   Execute: sudo bash $APP_DIR/setup_autostart.sh"
fi
echo ""

# Verificar status do serviço (requer sudo)
if sudo systemctl is-enabled cluster-automotivo &> /dev/null; then
    echo -e "${GREEN}✓${NC} Serviço habilitado no boot"
else
    echo -e "${YELLOW}⚠${NC} Serviço NÃO está habilitado no boot"
fi

if sudo systemctl is-active cluster-automotivo &> /dev/null; then
    echo -e "${GREEN}✓${NC} Serviço está rodando"
else
    echo -e "${YELLOW}⚠${NC} Serviço NÃO está rodando"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  REDE E PORTAS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "IP do Raspberry:"
IPS=$(hostname -I)
echo "$IPS"
echo ""

# Verificar conexão
if ping -c 1 8.8.8.8 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Conexão com internet OK"
else
    echo -e "${YELLOW}⚠${NC} Sem conexão com internet (pode ser normal)"
fi
echo ""

echo "Porta 5000:"
if sudo netstat -tuln 2>/dev/null | grep -q 5000; then
    echo -e "${GREEN}✓${NC} Porta 5000 está em uso"
    sudo netstat -tuln | grep 5000
else
    echo -e "${YELLOW}⚠${NC} Porta 5000 não está em uso"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6️⃣  LOGS E DIAGNÓSTICO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Diretório de logs
if [ -d "$APP_DIR/logs" ]; then
    echo -e "${GREEN}✓${NC} Diretório de logs existe"
    LOG_COUNT=$(ls "$APP_DIR/logs" 2>/dev/null | wc -l)
    echo "   Logs armazenados: $LOG_COUNT"
else
    echo -e "${YELLOW}⚠${NC} Diretório de logs não existe"
fi
echo ""

# Últimas linhas dos logs do systemd
echo "Últimas linhas dos logs do systemd (se houver):"
if sudo journalctl -u cluster-automotivo -n 5 --no-pager 2>/dev/null | grep -q "cluster"; then
    sudo journalctl -u cluster-automotivo -n 5 --no-pager | sed 's/^/   /'
else
    echo "   (sem logs ainda)"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "7️⃣  RESUMO E AÇÕES RECOMENDADAS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

ACTIONS=""

if [ ! -x "$APP_DIR/run_cluster.sh" ]; then
    ACTIONS="${ACTIONS}   1. chmod +x $APP_DIR/run_cluster.sh\n"
fi

if [ ! -f "/etc/systemd/system/cluster-automotivo.service" ]; then
    ACTIONS="${ACTIONS}   2. sudo bash $APP_DIR/setup_autostart.sh\n"
fi

if [ ! -d "$APP_DIR/cluster_env" ]; then
    ACTIONS="${ACTIONS}   3. cd $APP_DIR && ./run_cluster.sh (para criar ambiente virtual)\n"
fi

if [ -z "$ACTIONS" ]; then
    echo -e "${GREEN}✓ TUDO PARECE ESTAR OK!${NC}"
    echo ""
    echo "Próximos passos:"
    echo "   • Reinicie o Raspberry para ativar a inicialização automática"
    echo "   • Ou inicie manualmente: sudo systemctl start cluster-automotivo"
    echo "   • Acesse: http://<seu_ip>:5000"
else
    echo -e "${YELLOW}⚠ AÇÕES RECOMENDADAS:${NC}"
    echo ""
    echo -e "$ACTIONS"
    echo ""
    echo "Depois execute este script novamente para verificar."
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "FIM DO DIAGNÓSTICO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
