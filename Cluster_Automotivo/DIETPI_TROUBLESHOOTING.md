# 🔧 Troubleshooting - DietPi Cluster Automotivo

## Problema: Serviço não inicia no boot

### Verificação 1: Serviço está habilitado?
```bash
systemctl is-enabled cluster-automotivo
# Deve retornar: enabled
```

**Se retornar "disabled":**
```bash
sudo systemctl enable cluster-automotivo
```

### Verificação 2: Arquivo de serviço está correto?
```bash
sudo cat /etc/systemd/system/cluster-automotivo.service
# Procure por: ExecStart=/root/Rep_Cluster/Cluster_Automotivo/run_cluster.sh
```

### Verificação 3: Ver logs de boot
```bash
sudo journalctl -b -u cluster-automotivo
```

### Verificação 4: Teste manual
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh

# Deve mostrar:
# [TIMESTAMP] ========== Iniciando Cluster Automotivo ==========
# [TIMESTAMP] Iniciando Cluster Automotivo...
# [TIMESTAMP] Acesse em: http://192.168.X.X:5000
```

---

## Problema: "Port 5000 already in use"

### Encontrar o processo:
```bash
sudo lsof -i :5000
# ou
sudo netstat -tuln | grep 5000
# ou
sudo ss -tlnp | grep 5000
```

### Matar o processo:
```bash
sudo kill -9 <PID>
```

### Ou reiniciar o serviço:
```bash
sudo systemctl restart cluster-automotivo
```

### Usar porta diferente (alternativa):
Edite `cluster_gui.py`:
```python
# Encontre esta linha:
self.socketio.run(self.app, host='0.0.0.0', port=5000, debug=False)

# Mude para:
self.socketio.run(self.app, host='0.0.0.0', port=8080, debug=False)
```

---

## Problema: Não consigo acessar de outro aparelho

### 1️⃣ Verificar se está rodando:
```bash
sudo systemctl status cluster-automotivo

# Deve mostrar:
# Active: active (running)
```

### 2️⃣ Verificar IP do Raspberry:
```bash
hostname -I
# Deve retornar algo como: 192.168.1.100 192.168.1.101
```

### 3️⃣ Testar conexão localmente:
```bash
curl http://localhost:5000
# Deve retornar HTML da página
```

### 4️⃣ Testar de outro aparelho na rede:
```bash
# De outro aparelho (Linux/Mac):
curl http://192.168.1.100:5000

# De outro aparelho (Windows PowerShell):
Invoke-WebRequest http://192.168.1.100:5000
```

### 5️⃣ Verificar Firewall:
```bash
# Ver regras UFW
sudo ufw status

# Permitir porta 5000
sudo ufw allow 5000

# Se UFW não está rodando:
sudo ufw enable
```

### 6️⃣ Verificar conectividade WiFi:
```bash
# Verfiar IP do gateway
ip route show

# Testar conexão ao gateway
ping 192.168.1.1

# Ver redes WiFi disponíveis
sudo nmcli device wifi list

# Ver conexões ativas
nmcli device
```

---

## Problema: Nenhuma saída nos logs

### Verificar logs em tempo real:
```bash
sudo journalctl -u cluster-automotivo -f
```

### Verificar logs históricos:
```bash
sudo journalctl -u cluster-automotivo -n 100
```

### Se não houver nada:
1. Certifique-se que o serviço iniciou:
   ```bash
   sudo systemctl start cluster-automotivo
   sudo systemctl status cluster-automotivo
   ```

2. Verifique permissões:
   ```bash
   ls -la ~/Rep_Cluster/Cluster_Automotivo/run_cluster.sh
   # Deve ter: -rwxr-xr-x (com x = executável)
   ```

---

## Problema: Erro ao instalar dependências

### Atualizar pip:
```bash
python3 -m pip install --upgrade pip
```

### Instalar Flask e SocketIO:
```bash
pip install Flask>=2.0.0 Flask-SocketIO>=5.0.0
```

### Se ainda tiver problema:
```bash
# Limpar cache de pip
pip cache purge

# Tentar novamente
pip install -r requirements.txt -v
```

---

## Problema: Aplicação fecha inesperadamente

### Ver razão da saída:
```bash
# Últimas 20 linhas dos logs
sudo journalctl -u cluster-automotivo -n 20

# Ou com mais contexto
sudo journalctl -u cluster-automotivo --no-pager
```

### Habilitar mais detalhes nos logs:
Edite `/etc/systemd/system/cluster-automotivo.service`:
```ini
# Mude de:
StandardOutput=journal
StandardError=journal

# Para (para ver em tempo real):
StandardOutput=inherit
StandardError=inherit
```

Depois recarregue:
```bash
sudo systemctl daemon-reload
sudo systemctl restart cluster-automotivo
```

---

## Problema: Ambiente virtual não está sendo criado

### Verificar se venv existe:
```bash
ls -la ~/Rep_Cluster/Cluster_Automotivo/cluster_env/
```

### Se não existe, criar manualmente:
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
python3 -m venv cluster_env
source cluster_env/bin/activate
pip install -r requirements.txt
deactivate
```

### Reinstalar do zero:
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
rm -rf cluster_env
rm -f cluster_env/.dependencies_installed
./run_cluster.sh
```

---

## Problema: Python3 não encontrado

```bash
# Verificar se Python3 está instalado
python3 --version

# Se não estiver:
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verificar novamente
python3 --version
```

---

## Problema: Permissão negada ao executar o script

```bash
# Tornar executável
chmod +x ~/Rep_Cluster/Cluster_Automotivo/run_cluster.sh
chmod +x ~/Rep_Cluster/Cluster_Automotivo/setup_autostart.sh

# Verificar
ls -la ~/Rep_Cluster/Cluster_Automotivo/*.sh
# Devem ter: -rwxr-xr-x
```

---

## Problema: Serviço inicia mas app fecha logo depois

### Razões comuns:

1. **Dependências não instaladas:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Arquivo de configuração corrompido:**
   ```bash
   cat ~/Rep_Cluster/Cluster_Automotivo/cluster_gui.py | head -20
   ```

3. **Porta já em uso:**
   ```bash
   sudo systemctl status cluster-automotivo | grep "Port"
   ```

### Debug completo:
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
source cluster_env/bin/activate
python3 cluster_gui.py -v

# Deve mostrar:
# * Running on http://0.0.0.0:5000
```

---

## Verificação Completa do Sistema

Execute este script para diagnosticar:

```bash
#!/bin/bash
echo "=== DIAGNÓSTICO CLUSTER AUTOMOTIVO ==="
echo ""
echo "1. Python3:"
python3 --version
echo ""
echo "2. Serviço habilitado:"
systemctl is-enabled cluster-automotivo
echo ""
echo "3. Serviço rodando:"
sudo systemctl is-active cluster-automotivo
echo ""
echo "4. IP do Raspberry:"
hostname -I
echo ""
echo "5. Porta 5000 em uso:"
sudo netstat -tuln | grep 5000
echo ""
echo "6. Últimos erros:"
sudo journalctl -u cluster-automotivo -n 10 --no-pager
echo ""
echo "7. Ambiente virtual existe:"
ls -d ~/Rep_Cluster/Cluster_Automotivo/cluster_env 2>/dev/null && echo "SIM" || echo "NÃO"
echo ""
echo "=== FIM DIAGNÓSTICO ==="
```

Salve como `diagnose.sh`, execute com `bash diagnose.sh` e compartilhe o output se precisar de ajuda.

---

## Links Úteis

- [systemd Documentation](https://man7.org/linux/man-pages/man1/systemctl.1.html)
- [journalctl Documentation](https://man7.org/linux/man-pages/man1/journalctl.1.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [DietPi Official](https://dietpi.com/)

---

## Ainda com problema?

Se nada funcionar:

1. Copie os logs completos:
   ```bash
   sudo journalctl -u cluster-automotivo --no-pager > ~/logs.txt
   sudo journalctl -b --no-pager >> ~/logs.txt
   cat ~/Rep_Cluster/Cluster_Automotivo/logs/* >> ~/logs.txt
   ```

2. Execute o diagnóstico acima

3. Compartilhe os outputs
