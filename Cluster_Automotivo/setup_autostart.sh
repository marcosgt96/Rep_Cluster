#!/bin/bash
# Script para instalar o Cluster Automotivo como serviço automático no DietPi
# Execute com: sudo bash setup_autostart.sh

echo "======================================"
echo "Instalação - Cluster Automotivo"
echo "======================================"
echo ""

# Verificar se está rodando como root
if [ "$EUID" -ne 0 ]; then
   echo "ERRO: Este script precisa ser executado como root (use: sudo bash setup_autostart.sh)"
   exit 1
fi

# Definir variáveis
APP_DIR="/root/Rep_Cluster/Cluster_Automotivo"
SERVICE_FILE="/etc/systemd/system/cluster-automotivo.service"
SERVICE_TEMPLATE="$APP_DIR/cluster-automotivo.service"

echo "Verificando se o diretório da aplicação existe..."
if [ ! -d "$APP_DIR" ]; then
    echo "ERRO: Diretório não encontrado: $APP_DIR"
    echo "Ajuste o caminho no início do script se necessário."
    exit 1
fi

echo "✓ Diretório encontrado: $APP_DIR"
echo ""

# Tornar o script run_cluster.sh executável
echo "Tornando o script de execução executável..."
chmod +x "$APP_DIR/run_cluster.sh"
echo "✓ run_cluster.sh é executável"
echo ""

# Criar diretório de logs
echo "Criando diretório de logs..."
mkdir -p "$APP_DIR/logs"
chmod 755 "$APP_DIR/logs"
echo "✓ Diretório de logs criado"
echo ""

# Verificar se o arquivo de serviço template existe
if [ ! -f "$SERVICE_TEMPLATE" ]; then
    echo "ERRO: Arquivo de serviço não encontrado: $SERVICE_TEMPLATE"
    exit 1
fi

# Copiar o arquivo de serviço
echo "Instalando serviço systemd..."
cp "$SERVICE_TEMPLATE" "$SERVICE_FILE"

if [ ! -f "$SERVICE_FILE" ]; then
    echo "ERRO: Falha ao copiar arquivo de serviço"
    exit 1
fi

echo "✓ Serviço instalado: $SERVICE_FILE"
echo ""

# Recarregar configuração do systemd
echo "Recarregando configuração do systemd..."
systemctl daemon-reload
echo "✓ Systemd recarregado"
echo ""

# Ativar serviço para iniciar no boot
echo "Ativando serviço para iniciar automaticamente no boot..."
systemctl enable cluster-automotivo.service
echo "✓ Serviço habilitado no boot"
echo ""

echo "======================================"
echo "✓ Instalação concluída com sucesso!"
echo "======================================"
echo ""
echo "Comandos úteis:"
echo ""
echo "Iniciar agora:"
echo "  sudo systemctl start cluster-automotivo"
echo ""
echo "Ver status:"
echo "  sudo systemctl status cluster-automotivo"
echo ""
echo "Ver logs em tempo real:"
echo "  sudo journalctl -u cluster-automotivo -f"
echo ""
echo "Ver logs da última inicialização:"
echo "  sudo journalctl -u cluster-automotivo -n 50"
echo ""
echo "Parar o serviço:"
echo "  sudo systemctl stop cluster-automotivo"
echo ""
echo "Desabilitar do boot:"
echo "  sudo systemctl disable cluster-automotivo"
echo ""
echo "Acessar a aplicação:"
echo "  http://$(hostname -I | awk '{print $1}'):5000"
echo ""
