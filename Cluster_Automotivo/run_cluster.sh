#!/bin/bash
# Script para executar o Cluster Automotivo com ambiente virtual

cd "$(dirname "$0")"

# Verificar se o ambiente virtual existe
if [ ! -d "cluster_env" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv cluster_env
fi

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source cluster_env/bin/activate

# Executar o cluster
echo "Iniciando Cluster Automotivo..."
python3 cluster_gui.py

# Desativar ambiente virtual
deactivate