#!/bin/bash
# Script para abrir o cluster no navegador
# Use em outro aparelho conectado na mesma rede

echo "Detectando IP do Cluster Automotivo..."

# Tentar obter o IP
CLUSTER_IP=$(hostname -I | awk '{print $1}')

if [ -z "$CLUSTER_IP" ]; then
    echo "ERRO: Não foi possível detectar o IP do Raspberry Pi"
    echo ""
    echo "Use manualmente:"
    echo "  - Verifique o IP do Raspberry Pi no seu roteador ou execute: hostname -I"
    echo "  - Abra no navegador: http://<IP_DO_RASPBERRY>:5000"
    exit 1
fi

CLUSTER_URL="http://$CLUSTER_IP:5000"

echo "✓ Cluster encontrado em: $CLUSTER_URL"
echo ""

# Tentar abrir no navegador padrão
if command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open "$CLUSTER_URL"
elif command -v open &> /dev/null; then
    # macOS
    open "$CLUSTER_URL"
elif command -v start &> /dev/null; then
    # Windows
    start "$CLUSTER_URL"
else
    echo "Abra manualmente no seu navegador:"
    echo "  $CLUSTER_URL"
fi
