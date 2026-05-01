# 🚀 Guia Rápido - DietPi Cluster Automotivo

## Instalação em 3 Comandos

```bash
# 1. Tornar scripts executáveis
cd ~/Rep_Cluster/Cluster_Automotivo && chmod +x *.sh

# 2. Instalar como serviço
sudo bash setup_autostart.sh

# 3. Iniciar agora
sudo systemctl start cluster-automotivo
```

## ✅ Verificar se está funcionando

```bash
# Ver status
sudo systemctl status cluster-automotivo

# Ver logs
sudo journalctl -u cluster-automotivo -f
```

## 🌐 Acessar a Aplicação

### Descubra o IP do Raspberry:
```bash
hostname -I
```

### Abra no navegador:
```
http://<seu_ip>:5000

# Exemplo:
http://192.168.1.100:5000
```

## 📁 Arquivos Criados/Modificados

| Arquivo | Descrição |
|---------|-----------|
| `run_cluster.sh` | ✅ Melhorado com logging |
| `cluster_gui.py` | ✅ Trata erro de navegador headless |
| `cluster-automotivo.service` | ✨ Novo - Serviço systemd |
| `setup_autostart.sh` | ✨ Novo - Instalador |
| `AUTOSTART_GUIDE.md` | ✨ Novo - Guia completo |
| `DIETPI_QUICK_START.md` | ✨ Novo - Este arquivo |

## 🛠️ Comandos Principais

```bash
# Status
sudo systemctl status cluster-automotivo

# Logs em tempo real
sudo journalctl -u cluster-automotivo -f

# Parar
sudo systemctl stop cluster-automotivo

# Reiniciar
sudo systemctl restart cluster-automotivo

# Iniciar manualmente (para testes)
cd ~/Rep_Cluster/Cluster_Automotivo && ./run_cluster.sh
```

## 📍 Diferenças com Versão Anterior

| Antes | Depois |
|-------|--------|
| ❌ Sem inicialização automática | ✅ Inicia no boot automaticamente |
| ❌ Sem logs | ✅ Logs em `logs/` e journalctl |
| ❌ Quebrava se não tivesse GUI | ✅ Funciona em headless |
| ❌ Sem tratamento de erros | ✅ Mensagens de erro claras |
| ❌ Sem instalação de dependências | ✅ Instala automaticamente |

## ❓ FAQ Rápido

**P: Como paro a aplicação?**
R: `sudo systemctl stop cluster-automotivo`

**P: Como desabilito a inicialização automática?**
R: `sudo systemctl disable cluster-automotivo`

**P: Onde vejo os erros?**
R: `sudo journalctl -u cluster-automotivo -n 50`

**P: Preciso de monitor/teclado conectado?**
R: Não! Funciona 100% headless. Acesse via IP na rede.

**P: A porta 5000 está ocupada?**
R: `sudo systemctl stop cluster-automotivo && sudo systemctl start cluster-automotivo`

---

Para mais detalhes, veja: `AUTOSTART_GUIDE.md`
