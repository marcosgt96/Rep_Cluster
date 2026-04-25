# Cluster Automotivo - Script de Execução

Este script facilita a execução do Cluster Automotivo no Raspberry Pi, gerenciando automaticamente o ambiente virtual Python.

## Como usar:

1. **Tornar executável** (apenas uma vez):
   ```bash
   chmod +x run_cluster.sh
   ```

2. **Executar**:
   ```bash
   ./run_cluster.sh
   ```

## O que o script faz:

- Verifica se o ambiente virtual `cluster_env` existe
- Cria o ambiente virtual se necessário
- Ativa o ambiente virtual
- Executa `python3 cluster_gui.py`
- Desativa o ambiente virtual ao finalizar

## Execução manual:

Se preferir executar manualmente:

```bash
# Ativar ambiente virtual
source cluster_env/bin/activate

# Executar cluster
python3 cluster_gui.py

# Desativar (opcional)
deactivate
```