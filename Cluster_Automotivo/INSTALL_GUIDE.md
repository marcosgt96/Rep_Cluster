# 🚀 Cluster Automotivo - Guia Completo de Instalação

## ✅ O Que Este Guia Resolve

Você terá uma aplicação que:
- ✅ **Inicia automaticamente** no boot do Raspberry Pi
- ✅ **Funciona remotamente** de qualquer aparelho na rede
- ✅ **Tem logs completos** para debug e monitoramento
- ✅ **Reinicia sozinha** em caso de falha
- ✅ **Funciona headless** (sem monitor/teclado conectado)

---

## 🎯 Opções de Instalação

### Opção 1: Instalação Rápida (Recomendada)
→ Para Raspberry Pi já configurado com DietPi
→ Usa inicialização automática via systemd

### Opção 2: Criar Imagem do Zero
→ Para cartão SD novo com tudo pronto
→ Inclui configuração completa do sistema

---

## 🚀 Instalação Rápida (DietPi Existente)

### Pré-requisitos
- Raspberry Pi com DietPi instalado
- Acesso SSH ao Raspberry Pi
- Conexão com internet

### 3 Passos para Instalar

#### 1️⃣ Preparar Scripts
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
chmod +x *.sh
```

#### 2️⃣ Instalar Serviço Automático
```bash
sudo bash setup_autostart.sh
```

#### 3️⃣ Iniciar Aplicação
```bash
sudo systemctl start cluster-automotivo
```

**✅ Pronto! A aplicação está rodando automaticamente.**

---

## 🌐 Como Acessar a Aplicação

### Localmente (no Raspberry Pi)
```
http://localhost:5000
```

### De outro aparelho na rede
```
http://<IP_DO_RASPBERRY>:5000
```

**Descubra o IP do Raspberry:**
```bash
hostname -I
```

---

## 📚 Documentação Criada

Para suporte completo, criamos 6 documentos:

1. **`CHECKLIST.md`** ← **COMECE AQUI!**
   - Verificação passo a passo
   - Testes de funcionamento

2. **`DIETPI_QUICK_START.md`**
   - Início rápido em 3 passos
   - Comandos principais

3. **`AUTOSTART_GUIDE.md`**
   - Guia completo e detalhado
   - Segurança e configurações

4. **`DIETPI_TROUBLESHOOTING.md`**
   - +20 problemas e soluções
   - Muito útil se algo não funcionar

5. **`SOLUTION_SUMMARY.md`**
   - Resumo de tudo que foi feito
   - Estrutura de arquivos
   - Fluxograma de inicialização

6. **`diagnose.sh`**
   - Script para diagnosticar problemas
   - Execute: `bash diagnose.sh`

---

## 🎮 Comandos Essenciais

```bash
# Status da aplicação
sudo systemctl status cluster-automotivo

# Ver logs em tempo real
sudo journalctl -u cluster-automotivo -f

# Reiniciar aplicação
sudo systemctl restart cluster-automotivo

# Parar aplicação
sudo systemctl stop cluster-automotivo

# Diagnosticar problemas
bash ~/Rep_Cluster/Cluster_Automotivo/diagnose.sh

# Executar manualmente (para testes)
cd ~/Rep_Cluster/Cluster_Automotivo && ./run_cluster.sh
```

---

## 📁 Arquivos Criados/Modificados

### ✅ Arquivos MODIFICADOS
- `run_cluster.sh` - Logging completo + tratamento de erros
- `cluster_gui.py` - Funciona em ambientes headless

### ✨ Novos SCRIPTS
- `setup_autostart.sh` - Instalador automático do serviço
- `cluster-automotivo.service` - Configuração systemd
- `open_cluster.sh` - Abre cluster no navegador
- `diagnose.sh` - Diagnóstico automático

### ✨ Nova DOCUMENTAÇÃO
- `CHECKLIST.md` - Verificação passo a passo
- `DIETPI_QUICK_START.md` - Início rápido
- `AUTOSTART_GUIDE.md` - Guia detalhado
- `DIETPI_TROUBLESHOOTING.md` - Solução de problemas
- `SOLUTION_SUMMARY.md` - Resumo técnico

---

## 🐍 Ambiente Virtual Python

**Importante:** Sempre use ambiente virtual para evitar conflitos:

```bash
# Criar ambiente virtual (feito automaticamente pelo script)
python3 -m venv cluster_env

# Ativar ambiente virtual (sempre antes de usar Python/pip)
source cluster_env/bin/activate

# Agora pode usar pip normalmente
pip install -r requirements.txt

# Executar aplicação
python3 cluster_gui.py

# Desativar (opcional)
deactivate
```

**Nota:** O script `run_cluster.sh` gerencia isso automaticamente!

---

## 🔄 Atualizações Futuras (Via Git)

Com as mudanças para inicialização automática, as atualizações são mais simples:

### 1. Acessar Raspberry Pi
```bash
ssh root@<IP_DO_RASPBERRY>
# ou
ssh pi@<IP_DO_RASPBERRY>
```

### 2. Parar o Serviço
```bash
sudo systemctl stop cluster-automotivo
```

### 3. Atualizar Código
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
git pull
```

### 4. Verificar se há mudanças nos scripts (opcional)
```bash
# Se houve mudanças em setup_autostart.sh ou cluster-automotivo.service:
chmod +x *.sh
sudo bash setup_autostart.sh  # Reinstala o serviço se necessário
```

### 5. Atualizar Dependências (geralmente automático)
```bash
# O script run_cluster.sh instala dependências automaticamente na primeira execução
# Só é necessário atualizar manualmente se houver mudanças específicas:
source cluster_env/bin/activate
pip install -r requirements.txt --upgrade
deactivate
```

### 6. Reiniciar Serviço
```bash
sudo systemctl start cluster-automotivo
sudo systemctl status cluster-automotivo
```

### 7. Verificar Logs
```bash
sudo journalctl -u cluster-automotivo -f
```

**✅ Atualização concluída!**

**Nota:** Na maioria dos casos, apenas os passos 1, 2, 3, 6 e 7 são necessários.

---

## 📦 Opção 2: Criar Imagem do Zero

Para criar um cartão SD completamente novo com tudo pronto:

### Materiais Necessários
| Item | Descrição |
|------|------------|
| Computador | Windows, macOS ou Linux |
| Leitor de cartão SD | USB ou integrado |
| Cartão SD | 8GB+ (recomendado 16GB) |
| Raspberry Pi | 3B+ ou superior |
| Raspberry Pi Imager | [Baixar](https://www.raspberrypi.com/software/) |

### Passo a Passo

#### 1. Baixar Raspberry Pi Imager
**Windows/macOS/Linux:**
- Acesse: https://www.raspberrypi.com/software/
- Baixe e instale a versão para seu sistema

#### 2. Preparar Cartão SD
1. Conecte o cartão SD ao computador
2. Abra o Raspberry Pi Imager
3. Selecione:
   - **Operating System**: DietPi (recomendado) ou Raspberry Pi OS
   - **Storage**: Seu cartão SD

#### 3. Configurações Avançadas (⚙️)
Clique em ⚙️ (engrenagem) e configure:

| Configuração | Valor |
|--------------|-------|
| **Hostname** | `cluster-automotivo` |
| **Enable SSH** | ✅ Ativado |
| **Username** | `root` (para DietPi) ou `pi` |
| **Password** | `dietpi` ou `raspberry` |
| **WiFi** | Sua rede WiFi |
| **Set locale settings** | ✅ Brasil |

#### 4. Gravar Imagem
1. Clique em **Write**
2. Aguarde a conclusão (5-10 minutos)
3. Remova o cartão com segurança

#### 5. Primeira Inicialização
1. Insira o cartão no Raspberry Pi
2. Conecte a fonte de alimentação
3. Aguarde 2-3 minutos para inicializar

#### 6. Acessar via SSH
```bash
# Windows (PowerShell)
ssh root@cluster-automotivo.local
# ou
ssh root@192.168.1.100

# macOS/Linux
ssh root@cluster-automotivo.local
```

#### 7. Instalar Cluster Automotivo
```bash
# No Raspberry Pi:

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y git python3 python3-pip python3-venv

# Baixar projeto
cd ~
git clone https://github.com/seu-usuario/Rep_Cluster.git
cd Rep_Cluster/Cluster_Automotivo

# Instalar aplicação
chmod +x *.sh
sudo bash setup_autostart.sh
sudo systemctl start cluster-automotivo

# Verificar
sudo systemctl status cluster-automotivo
```

**✅ Imagem pronta!**

---

## 🖥️ Configurações de Tela (Opcional)

### Para Tela Touchscreen 7"
```bash
# No Raspberry Pi:
sudo raspi-config
```

Navegue até:
- **Display Options** → **Resolution** → `800x480`
- **Display Options** → **Screen Blanking** → `No`

### Para Tela HDMI (TV/Monitor)
```bash
# Forçar resolução HDMI
echo "hdmi_force_hotplug=1" | sudo tee -a /boot/config.txt
echo "hdmi_group=2" | sudo tee -a /boot/config.txt
echo "hdmi_mode=82" | sudo tee -a /boot/config.txt  # 1920x1080 60Hz
```

---

## 📞 Suporte e Troubleshooting

### Problemas Comuns

1. **Serviço não inicia:**
   ```bash
   sudo journalctl -u cluster-automotivo -n 50
   ```

2. **Porta 5000 ocupada:**
   ```bash
   sudo systemctl restart cluster-automotivo
   ```

3. **Não acessa remotamente:**
   ```bash
   hostname -I  # Verificar IP
   curl http://localhost:5000  # Testar localmente
   ```

4. **Ambiente virtual com problemas:**
   ```bash
   rm -rf ~/Rep_Cluster/Cluster_Automotivo/cluster_env
   ./run_cluster.sh  # Recria automaticamente
   ```

### Script de Diagnóstico
```bash
bash ~/Rep_Cluster/Cluster_Automotivo/diagnose.sh
```

### Documentação de Suporte
- **`DIETPI_TROUBLESHOOTING.md`** - +20 soluções de problemas
- **`AUTOSTART_GUIDE.md`** - Guia técnico detalhado

---

## 📝 Notas Importantes

- **Segurança**: Altere a senha padrão após primeira configuração
- **Backup**: Faça backup da imagem do cartão SD após configurar tudo
- **Rede**: Anote o IP do Raspberry para acesso futuro
- **Ambiente Virtual**: O script gerencia automaticamente
- **Atualizações**: Use `git pull` + reinicie o serviço
- **Logs**: Sempre verifique logs em caso de problemas

---

## 🎯 Verificação Final

Após instalação, verifique se tudo funciona:

```bash
# 1. Serviço ativo
sudo systemctl status cluster-automotivo

# 2. Porta aberta
sudo netstat -tuln | grep 5000

# 3. Acesso local
curl http://localhost:5000

# 4. Descobrir IP
hostname -I

# 5. Testar acesso remoto (de outro aparelho)
# Abra navegador: http://<IP>:5000
```

**✅ Tudo funcionando? Parabéns! 🚗**

---

## 📖 Leitura Recomendada

- **Rápido (2 min):** Este arquivo
- **Passo a passo (5 min):** `CHECKLIST.md`
- **Detalhado (15 min):** `AUTOSTART_GUIDE.md`
- **Problemas:** `DIETPI_TROUBLESHOOTING.md`

---

**Última atualização:** 2025-01-05
**Sistema:** DietPi/Raspberry Pi OS
**Versão:** v1.0 com inicialização automática
**Compatível:** Raspberry Pi 3B+ ou superior