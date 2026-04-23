# Atualização do Cluster Automotivo no Raspberry Pi

Este guia explica como atualizar o projeto quando você fizer alterações no código.

---

## 🔄 Método 1: Deploy Automático (Recomendado)

### Do Windows
```cmd
deploy.bat
```

### Do macOS/Linux
```bash
./deploy.sh
```

Os scripts copiam todos os arquivos e instalam dependências automaticamente.

---

## 🔄 Método 2: Manual via SSH

### Conectar ao Raspberry
```bash
ssh pi@cluster-automotivo.local
# ou
ssh pi@192.168.1.100  # seu IP
```

### Atualizar arquivos

**Opção A: Via Git (se o projeto estiver no GitHub)**
```bash
cd ~/Cluster_Automotivo
git pull
pip3 install -r requirements.txt --upgrade
```

**Opção B: Copiar manualmente do seu computador**

No SEU computador:
```bash
# Linux/macOS
scp -r ./* pi@cluster-automotivo.local:~/Cluster_Automotivo/

# Windows (PowerShell)
scp -r .\* pi@cluster-automotivo.local:~/Cluster_Automotivo/
```

### Reiniciar o serviço (se usar systemd)
```bash
sudo systemctl restart cluster
```

---

## 🔄 Método 3: Atualização Seletiva

Para atualizar apenas um arquivo específico:

```bash
# No seu computador
scp vehicle_sensors.py pi@cluster-automotivo.local:~/Cluster_Automotivo/

# No Raspberry (se o cluster estiver rodando como serviço)
sudo systemctl restart cluster
```

---

## 📋 Checklist de Atualização

| Passo | Comando | Quando |
|-------|---------|--------|
| 1. Conectar | `ssh pi@IP` | Sempre |
| 2. Copiar arquivos | `git pull` ou `scp` | Após alterações |
| 3. Atualizar dependências | `pip3 install -r requirements.txt --upgrade` | Se requirements.txt mudou |
| 4. Testar | `python3 cluster_gui.py` | Após atualização |
| 5. Reiniciar serviço | `sudo systemctl restart cluster` | Se usando inicialização automática |

---

## ⚠️ Notas Importantes

1. **Faça backup** antes de grandes alterações
2. **Teste localmente** antes de enviar para o Raspberry
3. **Verifique erros**: `python3 -c "from vehicle_sensors import *"`
4. **Logs**: Se usar systemd: `sudo journalctl -u cluster -f`

---

## 🔧 Atualização Rápida (Copy-Paste)

```bash
# No seu computador (pasta do projeto):
scp -r ./* pi@192.168.1.100:~/Cluster_Automotivo/

# No Raspberry:
cd ~/Cluster_Automotivo
python3 -c "from vehicle_sensors import VehicleSensorSimulator; print('OK')"
sudo systemctl restart cluster
```

Substitua `192.168.1.100` pelo IP do seu Raspberry (veja no roteador).