# ✅ Checklist - Cluster Automotivo DietPi

## 📋 Antes de Começar

- [ ] Conectado ao Raspberry Pi via SSH
- [ ] Estou no diretório correto: `~/Rep_Cluster/Cluster_Automotivo`
- [ ] Tenho acesso sudo (posso executar `sudo` sem senha ou com acesso)

---

## 🔧 Instalação (Execute Uma Vez)

### Passo 1: Preparar Scripts
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
chmod +x run_cluster.sh setup_autostart.sh open_cluster.sh diagnose.sh
```

- [ ] Todos os scripts estão executáveis

### Passo 2: Executar Instalador
```bash
sudo bash setup_autostart.sh
```

- [ ] Script executou sem erros
- [ ] Viu mensagem: "✓ Instalação concluída com sucesso!"
- [ ] Diretório de logs foi criado
- [ ] Serviço foi instalado

### Passo 3: Verificar Instalação
```bash
sudo systemctl status cluster-automotivo
```

- [ ] Vê "Active: active (running)" OU "Active: inactive (dead)"
- [ ] Nenhum erro de sintaxe

---

## 🚀 Iniciação (Execute Sempre que Quiser)

### Opção A: Iniciar Agora
```bash
sudo systemctl start cluster-automotivo
sudo systemctl status cluster-automotivo
```

- [ ] Status mostra "active (running)"

### Opção B: Reiniciar Raspberry (Para Testar Boot Automático)
```bash
sudo reboot
# Aguarde 2-3 minutos
sudo systemctl status cluster-automotivo
```

- [ ] Após reiniciar, o serviço inicia automaticamente

### Opção C: Executar Manualmente (Para Debug)
```bash
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh
```

- [ ] Vê mensagens de inicialização
- [ ] Vê a porta e IP de acesso
- [ ] Pressione Ctrl+C para parar

---

## 🌐 Testando Acesso

### Passo 1: Descobrir IP
```bash
hostname -I
```

- [ ] Anote o IP (ex: 192.168.1.100)

### Passo 2: Testar Localmente (No Raspberry)
```bash
curl http://localhost:5000
```

- [ ] Retorna HTML (começa com `<!DOCTYPE html>`)

### Passo 3: Testar Remotamente (De Outro Aparelho)

No navegador:
```
http://192.168.1.100:5000
```

- [ ] Página carrega corretamente
- [ ] Vê o painel do Cluster Automotivo

---

## 📊 Monitoramento

### Ver Status
```bash
sudo systemctl status cluster-automotivo
```

- [ ] Status é "active (running)"
- [ ] Nenhuma mensagem de erro

### Ver Logs em Tempo Real
```bash
sudo journalctl -u cluster-automotivo -f
```

- [ ] Logs aparecem sem erros
- [ ] Pressione Ctrl+C para sair

### Ver Últimos Erros (Se houver)
```bash
sudo journalctl -u cluster-automotivo -n 30 --no-pager
```

- [ ] Procure por linhas com "ERROR" ou "Exception"

### Ver Logs em Arquivo
```bash
ls -la ~/Rep_Cluster/Cluster_Automotivo/logs/
cat ~/Rep_Cluster/Cluster_Automotivo/logs/cluster_*.log
```

- [ ] Arquivos de log existem
- [ ] Contêm informações úteis

---

## 🔍 Diagnóstico

### Executar Script de Diagnóstico
```bash
bash ~/Rep_Cluster/Cluster_Automotivo/diagnose.sh
```

- [ ] Todos os itens mostram ✓ (verde)
- [ ] Se algum mostra ✗ (vermelho), siga as ações recomendadas

### Verificar Porta em Uso
```bash
sudo netstat -tuln | grep 5000
```

- [ ] Mostra a porta 5000 aberta em 0.0.0.0 ou 127.0.0.1

### Verificar Ambiente Virtual
```bash
ls -la ~/Rep_Cluster/Cluster_Automotivo/cluster_env/
source ~/Rep_Cluster/Cluster_Automotivo/cluster_env/bin/activate
pip list
deactivate
```

- [ ] Diretório `cluster_env` existe
- [ ] Ambiente virtual ativa corretamente
- [ ] Flask e Flask-SocketIO aparecem em `pip list`

---

## ⚠️ Problemas Comuns

### ❌ "Port 5000 already in use"

```bash
sudo systemctl restart cluster-automotivo
```

- [ ] Serviço reinicia sem erro

### ❌ "Serviço não inicia"

```bash
sudo journalctl -u cluster-automotivo -n 50
```

- [ ] Procure pela mensagem de erro
- [ ] Consulte `DIETPI_TROUBLESHOOTING.md`

### ❌ "Não consigo acessar de outro aparelho"

```bash
hostname -I
curl http://localhost:5000
sudo systemctl status cluster-automotivo
```

- [ ] IP está correto
- [ ] Serviço está rodando
- [ ] Tente novamente com o IP correto

### ❌ "Ambiente virtual não existe"

```bash
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh
```

- [ ] Script cria o ambiente virtual automaticamente
- [ ] Aguarde até ver "Iniciando Cluster Automotivo..."

---

## 🛑 Parar/Desabilitar

### Parar Agora
```bash
sudo systemctl stop cluster-automotivo
```

- [ ] `sudo systemctl status cluster-automotivo` mostra "inactive"

### Desabilitar do Boot
```bash
sudo systemctl disable cluster-automotivo
sudo systemctl stop cluster-automotivo
```

- [ ] `sudo systemctl is-enabled cluster-automotivo` mostra "disabled"

### Remover Completamente
```bash
sudo systemctl disable cluster-automotivo
sudo systemctl stop cluster-automotivo
sudo rm /etc/systemd/system/cluster-automotivo.service
sudo systemctl daemon-reload
```

- [ ] Arquivo removido
- [ ] Daemon recarregado

---

## 📱 Uso Normal

### Acessar de Outro Aparelho
1. [ ] Abra navegador
2. [ ] Digite: `http://<IP_DO_RASPBERRY>:5000`
3. [ ] Painel carrega corretamente

### Monitorar
```bash
sudo journalctl -u cluster-automotivo -f
```

- [ ] Logs aparecem em tempo real
- [ ] Sem erros de aplicação

### Reiniciar Se Precisar
```bash
sudo systemctl restart cluster-automotivo
sudo systemctl status cluster-automotivo
```

- [ ] Reinicia em menos de 5 segundos
- [ ] Status muda para "active (running)"

---

## 🎯 Verificação Final

Todos os itens abaixo marcados? Pronto! 🎉

- [ ] Scripts estão executáveis
- [ ] Serviço foi instalado
- [ ] Serviço está rodando
- [ ] Pode acessar via localhost (no Raspberry)
- [ ] Pode acessar via IP (de outro aparelho)
- [ ] Logs aparecem corretamente
- [ ] Diagnóstico mostra tudo verde
- [ ] Nenhuma mensagem de erro

---

## 📞 Próximas Ações

### Se Tudo Estiver Funcionando:
1. [ ] Reinicie o Raspberry para testar boot automático
2. [ ] Deixe rodando e acesse de outros aparelhos
3. [ ] Acompanhe os logs periodicamente

### Se Algo Não Funcionar:
1. [ ] Execute `bash diagnose.sh`
2. [ ] Consulte `DIETPI_TROUBLESHOOTING.md`
3. [ ] Verifique os logs: `sudo journalctl -u cluster-automotivo -n 100`
4. [ ] Teste manualmente: `cd ~/Rep_Cluster/Cluster_Automotivo && ./run_cluster.sh`

---

## 🆘 Suporte Rápido

**Comando mágico para resolver 90% dos problemas:**
```bash
sudo systemctl restart cluster-automotivo && sleep 2 && sudo journalctl -u cluster-automotivo -f
```

Este comando:
1. Reinicia o serviço
2. Aguarda 2 segundos
3. Mostra os logs em tempo real

Se ver algum erro, consulte a documentação ou execute o diagnóstico.

---

**Boa sorte! 🚗**
