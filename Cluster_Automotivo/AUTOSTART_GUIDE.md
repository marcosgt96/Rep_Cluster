# Guia Completo - Inicialização Automática do Cluster Automotivo no DietPi

## 📋 Resumo das Melhorias

Este guia resolve dois problemas:
1. **Inicialização automática**: O script agora funciona como serviço systemd
2. **Acesso via navegador**: A aplicação está acessível via rede e trata corretamente ambientes sem interface gráfica

---

## 🚀 Instalação Rápida (3 passos)

### Passo 1: Tornar os scripts executáveis

```bash
cd ~/Rep_Cluster/Cluster_Automotivo
chmod +x run_cluster.sh
chmod +x setup_autostart.sh
chmod +x open_cluster.sh
```

### Passo 2: Executar o instalador (como root)

```bash
sudo bash setup_autostart.sh
```

O script vai:
- ✓ Verificar o ambiente
- ✓ Criar diretório de logs
- ✓ Instalar o serviço systemd
- ✓ Ativar inicialização automática no boot

### Passo 3: Iniciar o serviço

```bash
sudo systemctl start cluster-automotivo
```

**Pronto!** A aplicação está rodando e será iniciada automaticamente no próximo boot.

---

## 🌐 Como Acessar a Aplicação

### No Raspberry Pi (localmente)
1. Abra um navegador no Raspberry Pi
2. Acesse: `http://localhost:5000`

### De outro aparelho na mesma rede
1. Abra um navegador em qualquer aparelho conectado ao WiFi
2. Descubra o IP do Raspberry Pi:
   ```bash
   # No Raspberry Pi, execute:
   hostname -I
   ```
3. Acesse: `http://<IP_DO_RASPBERRY>:5000`

### Exemplo
Se o IP do Raspberry é `192.168.1.100`:
```
http://192.168.1.100:5000
```

---

## 📊 Comandos Úteis

### Ver status do serviço
```bash
sudo systemctl status cluster-automotivo
```

### Ver logs em tempo real
```bash
sudo journalctl -u cluster-automotivo -f
```

### Ver últimos 50 logs
```bash
sudo journalctl -u cluster-automotivo -n 50
```

### Parar o serviço
```bash
sudo systemctl stop cluster-automotivo
```

### Reiniciar o serviço
```bash
sudo systemctl restart cluster-automotivo
```

### Desabilitar do boot (mas continua usando manualmente)
```bash
sudo systemctl disable cluster-automotivo
```

### Executar manualmente (para testes)
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh
```

---

## 🔧 Estrutura de Arquivos

Novos/Modificados:

```
Cluster_Automotivo/
├── run_cluster.sh                    # ✅ MELHORADO - Com logging e tratamento de erros
├── cluster_gui.py                    # ✅ MODIFICADO - Trata erro de navegador headless
├── cluster-automotivo.service        # ✨ NOVO - Configuração do serviço systemd
├── setup_autostart.sh                # ✨ NOVO - Script de instalação
├── open_cluster.sh                   # ✨ NOVO - Abre o cluster no navegador
├── logs/                             # ✨ NOVO - Diretório de logs
│   └── cluster_YYYYMMDD_HHMMSS.log   # Logs de cada execução
└── cluster_env/                      # Ambiente virtual Python
    └── .dependencies_installed        # Marcador para não reinstalar dependências
```

---

## 🐛 Solução de Problemas

### Problema: "Serviço não inicia"

**Verificar logs:**
```bash
sudo journalctl -u cluster-automotivo -n 50
```

**Verificar permissões:**
```bash
ls -la ~/Rep_Cluster/Cluster_Automotivo/run_cluster.sh
# Deve mostrar: -rwxr-xr-x (com x para executável)
```

### Problema: "Port 5000 already in use"

**Encontrar processo usando a porta:**
```bash
sudo lsof -i :5000
```

**Matar o processo:**
```bash
sudo kill -9 <PID>
```

**Ou usar porta diferente:**
Edite `cluster_gui.py` e mude `port=5000` para outra porta (ex: 8080)

### Problema: "Não consigo acessar de outro aparelho"

**Verificar se o serviço está rodando:**
```bash
sudo systemctl status cluster-automotivo
```

**Verificar se a porta está aberta:**
```bash
netstat -tuln | grep 5000
```

**Verificar firewall:**
```bash
sudo ufw allow 5000
```

**Verificar IP do Raspberry:**
```bash
hostname -I
ip route show | grep "default via"  # Para ver o gateway
```

### Problema: "Ambiente virtual não foi criado"

**Reinstalar dependências:**
```bash
rm -rf ~/Rep_Cluster/Cluster_Automotivo/cluster_env
rm ~/Rep_Cluster/Cluster_Automotivo/cluster_env/.dependencies_installed
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh
```

---

## 🔐 Segurança

### Acesso remoto seguro via SSH + Túnel

Se quiser acessar via internet (fora da rede local):

```bash
# No seu computador local, execute:
ssh -L 5000:localhost:5000 root@<IP_DO_RASPBERRY>

# Depois acesse:
http://localhost:5000
```

### Restringir acesso localmente

O serviço criado pelo `setup_autostart.sh` já usa o caminho de instalação atual da aplicação. Se quiser limitar o acesso apenas ao localhost, edite o arquivo de serviço gerado em `/etc/systemd/system/cluster-automotivo.service` e altere `ExecStart` para:

```ini
ExecStart=/bin/bash -lc 'cd /caminho/para/Cluster_Automotivo && ./run_cluster.sh'
```

ou para uma execução local:

```ini
ExecStart=/bin/bash -lc 'cd /caminho/para/Cluster_Automotivo && python3 -c "app = __import__(\"cluster_gui\").ClusterWebApp(); app.socketio.run(app.app, host=\"127.0.0.1\", port=5000)"'
```

(Isso limitaria ao localhost, sem acesso remoto)

---

## 📝 Modificações Realizadas

### 1. `run_cluster.sh` - Agora com:
- ✅ Detecção automática de erros
- ✅ Sistema de logging com timestamp
- ✅ Criação automática de ambiente virtual
- ✅ Instalação automática de dependências
- ✅ Tratamento de falhas com mensagens claras

### 2. `cluster_gui.py` - Agora com:
- ✅ Tratamento de erro ao tentar abrir navegador
- ✅ Mensagem informando o IP/porta onde acessar
- ✅ Funciona em ambientes headless (sem GUI)

### 3. `cluster-automotivo.service` - Novo:
- ✅ Inicia automaticamente no boot
- ✅ Reinicia em caso de falha
- ✅ Logs integrados com journalctl
- ✅ Segurança básica

### 4. `setup_autostart.sh` - Novo:
- ✅ Instalação simplificada em uma linha
- ✅ Verifica pré-requisitos
- ✅ Instruções de uso ao final

---

## ✨ Próximos Passos (Opcional)

### 1. Configurar DNS local (se tiver roteador)
```bash
# Acessar via nome amigável:
http://cluster-automotivo.local:5000
```

### 2. Configurar HTTPS
Adicione um proxy reverso com nginx e certificado Let's Encrypt

### 3. Painel de monitoramento
Crie um dashboard que mostra status do serviço, CPU, memória, etc.

### 4. Atualização automática
Configure um cron job para fazer pull de atualizações do GitHub

---

## 📞 Suporte

Se algo não funcionar:

1. **Verifique os logs:**
   ```bash
   sudo journalctl -u cluster-automotivo -n 100
   ```

2. **Teste manualmente:**
   ```bash
   cd ~/Rep_Cluster/Cluster_Automotivo
   ./run_cluster.sh
   ```

3. **Verifique a conectividade:**
   ```bash
   ping 192.168.1.1  # ping para seu gateway
   ```

---

## 🎉 Conclusão

Agora sua aplicação:
- ✅ Inicia automaticamente no boot do Raspberry Pi
- ✅ Funciona em ambiente headless (sem monitor/teclado)
- ✅ É acessível de qualquer aparelho na rede
- ✅ Tem logs para debug e monitoramento
- ✅ Reinicia automaticamente em caso de falha

Divirta-se com seu cluster automotivo! 🚗
