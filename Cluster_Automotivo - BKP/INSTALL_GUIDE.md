# ============================================
# Raspberry Pi Imager - Cluster Automotivo
# ============================================
# Este documento fornece instruções para criar
# um cartão SD pronto com o Cluster Automotivo
# ============================================

## 🎯 Opções de Instalação

### Opção 1: Instalação em Raspberry Pi existente
→ Use o script `install.sh` no Raspberry Pi

### Opção 2: Criar imagem ready-to-use (este guia)
→ Cria um cartão SD com tudo pronto

---

## 📦 Materiais Necessários

| Item | Descrição |
|------|------------|
| Computador | Windows, macOS ou Linux |
| Leitor de cartão SD | USB ou integrado |
| Cartão SD | 8GB+ (recomendado 16GB) |
| Raspberry Pi | 3B+ ou superior |
| Raspberry Pi Imager | [Baixar](https://www.raspberrypi.com/software/) |

---

## 🔧 Criando a Imagem - Passo a Passo

### Passo 1: Baixar Raspberry Pi Imager

**Windows/macOS/Linux:**
- Acesse: https://www.raspberrypi.com/software/
- Baixe e instale a versão para seu sistema

### Passo 2: Preparar o Cartão SD

1. Conecte o cartão SD ao computador
2. Abra o Raspberry Pi Imager
3. Selecione:
   - **Operating System**: Raspberry Pi OS (32-bit) ou (64-bit)
   - **Storage**: Seu cartão SD

### Passo 3: Configurações Avançadas (⚙️)

Clique em ⚙️ (engrenagem) e configure:

| Configuração | Valor |
|--------------|-------|
| **Hostname** | `cluster-automotivo` |
| **Enable SSH** | ✅ Ativado |
| **Username** | `cluster` |
| **Password** | `cluster` (ou sua preferência) |
| **WiFi** | Sua rede WiFi |
| **Set locale settings** | ✅ Brasil |

### Passo 4: Gravar a Imagem

1. Clique em **Write**
2. Aguarde a conclusão (5-10 minutos)
3. Remova o cartão com segurança

### Passo 5: Primeira Inicialização

1. Insira o cartão no Raspberry Pi
2. Conecte a tela (HDMI)
3. Conecte a fonte de alimentação
4. Aguarde 1-2 minutos para inicializar

### Passo 6: Acessar via SSH

**No computador, abra o terminal:**

```bash
# Windows (PowerShell)
ssh cluster@cluster-automotivo.local
# ou
ssh cluster@192.168.1.100  # Verifique o IP no roteador

# macOS/Linux
ssh pi@cluster-automotivo.local
```

**Senha:** `cluster` (ou a que você configurou)

### Passo 7: Baixar e Instalar o Cluster

```bash
# No Raspberry Pi (via SSH):

# Criar diretório
mkdir -p ~/Cluster_Automotivo
cd ~/Cluster_Automotivo

# Baixar do GitHub (substitua pela sua URL)
git clone https://github.com/marcosgt96/Cluster_Automotivo.git .

# Ou criar manualmente os arquivos
# Copie os arquivos do seu computador via SCP:
# scp -r ./Cluster_Automotivo/* cluster@cluster-automotivo.local:~/Cluster_Automotivo/

# Instalar dependências
pip3 install -r requirements.txt

# Testar
python3 cluster_gui.py
```

---

## 🎯 Criar Imagem Pré-Instalada (Avançado)

Para criar uma imagem já com o cluster instalado:

### No Raspberry Pi (após Passo 7):

```bash
# No Raspberry Pi:
sudo apt install -y git

# Clonar ou copiar projeto
cd ~
git clone https://github.com/seu-usuario/Cluster_Automotivo.git

# Instalar dependências
cd Cluster_Automotivo
pip3 install -r requirements.txt

# Criar script de inicialização automática
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/cluster.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=Cluster Automotivo
Exec=python3 /home/pi/Cluster_Automotivo/cluster_gui.py
EOF
```

### Criar Backup da Imagem:

```bash
# No computador com cartão inserido:
# Windows (PowerShell como Admin):
win32diskimager.exe

# macOS:
sudo dd if=/dev/rdiskN of=cluster-automotivo.img bs=1M

# Linux:
sudo dd if=/dev/mmcblk0 of=cluster-automotivo.img bs=1M
```

Substitua `N` pelo número do disco (verifique com `diskutil list` no macOS ou `lsblk` no Linux)

---

## 📋 Configuração Recomendada

### Para Tela de 7" Touchscreen:

```bash
# No Raspberry Pi:
sudo raspi-config
```

Navegue até:
- **Display Options** → **Resolution** → `800x480`
- **Display Options** → **Screen Blanking** → `No`

### Para Tela HDMI (TV/Vídeo):

```bash
# Forçar resolução HDMI
echo "hdmi_force_hotplug=1" | sudo tee -a /boot/config.txt
echo "hdmi_group=2" | sudo tee -a /boot/config.txt
echo "hdmi_mode=82" | sudo tee -a /boot/config.txt  # 1920x1080 60Hz
```

---

## 🔄 Atualizações Futuras

```bash
# Acessar Raspberry
ssh pi@cluster-automotivo.local

# Atualizar
cd ~/Cluster_Automotivo
git pull
pip3 install -r requirements.txt --upgrade

# Reiniciar
sudo reboot
```

---

## 📞 Suporte

Se tiver problemas:

1. **Sem conexão SSH**: Verifique IP no roteador
2. **Tela preta**: Pressione Alt+F2 para ver terminal
3. **GUI não inicia**: Verifique com `python3 -c "import tkinter"`

---

## 📝 Notas

- **Segurança**: Altere a senha padrão após primeira inicialização
- **Backup**: Faça imagem do cartão após configuração completa
- **Rede**: Anote o IP do Raspberry para acesso futuro