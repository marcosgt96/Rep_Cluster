# 🔧 Solução: Erro ao fazer `git pull`

## 📌 O Problema

```
error: Your local changes to the following files would be overwritten by merge:
        Cluster_Automotivo/run_cluster.sh
Please commit your changes or stash them before you merge.
Aborting
```

Este erro ocorre quando você tem mudanças locais no Raspberry Pi que conflitam com as mudanças no repositório remoto.

---

## ✅ Solução Recomendada (Opção 1)

Use `stash` para guardar as mudanças locais e depois atualizar:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo

# 1. Guardar as mudanças locais
git stash

# 2. Atualizar do repositório remoto
git pull

# 3. Aplicar as mudanças locais (se quiser manter)
git stash pop
```

**Se houver conflito após `git stash pop`:**
```bash
# Editar os arquivos com conflito manualmente
git add .
git commit -m "Resolvido conflito após git stash pop"
```

---

## ✅ Solução Alternativa (Opção 2)

Se você quer descartar as mudanças locais e usar a versão remota:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo

# 1. Descartar mudanças locais
git checkout -- Cluster_Automotivo/run_cluster.sh

# 2. Atualizar
git pull
```

---

## ✅ Solução Alternativa (Opção 3)

Commit das mudanças locais:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo

# 1. Adicionar mudanças
git add run_cluster.sh

# 2. Fazer commit
git commit -m "Mudanças locais no run_cluster.sh"

# 3. Atualizar
git pull

# 4. Se houver conflito, resolver manualmente:
# Editar o arquivo e remover os marcadores de conflito
# Depois fazer novo commit
```

---

## 🚀 Após Resolver o Conflito

Reinicie o serviço:

```bash
sudo systemctl restart cluster-automotivo
sudo systemctl status cluster-automotivo
```

Verifique os logs:

```bash
sudo journalctl -u cluster-automotivo -f
```

---

## 🛡️ Como Evitar Este Problema no Futuro

### 1. Não modificar `run_cluster.sh` localmente
O script é gerenciado pelo repositório. Se precisar personalizar:

**Opção A: Editar apenas o necessário**
```bash
# Ao invés de editar o arquivo, use variáveis de ambiente:
export CLUSTER_PORT=8080  # antes de executar
./run_cluster.sh
```

**Opção B: Criar um script wrapper**
```bash
# Criar: ~/run_cluster_custom.sh
#!/bin/bash
cd ~/Rep_Cluster/Cluster_Automotivo
./run_cluster.sh
```

### 2. Antes de cada `git pull`, parar o serviço
```bash
sudo systemctl stop cluster-automotivo
git pull
sudo systemctl start cluster-automotivo
```

### 3. Usar `.gitignore` para arquivos locais
Adicionar ao `.gitignore`:
```
# Arquivos de configuração local
local_config.sh
*.local
```

### 4. Criar branch local se precisar personalizar
```bash
git checkout -b meu-branch-customizado
# Fazer mudanças
git add .
git commit -m "Customizações locais"

# Depois para atualizar do main:
git fetch origin
git rebase origin/main
```

---

## 📊 Resumo das Soluções

| Opção | Comando | Efeito | Usar Quando |
|-------|---------|--------|------------|
| 1 - Stash | `git stash && git pull && git stash pop` | Mantém mudanças locais | Quer manter customizações |
| 2 - Checkout | `git checkout -- Cluster_Automotivo/run_cluster.sh && git pull` | Descarta mudanças | Quer usar versão remota |
| 3 - Commit | `git add . && git commit -m "msg" && git pull` | Cria histórico | Quer documentar mudanças |

---

## ❓ Próximas Perguntas

**P: Qual solução devo usar?**
R: Use a Opção 1 (Stash) se fez customizações locais. Use Opção 2 se quer sempre a versão do repositório.

**P: Posso committar em um repositório público?**
R: Sim, mas considere criar um fork ou branch separado para suas customizações.

**P: Como verifico quais mudanças foram feitas?**
R: Use `git diff Cluster_Automotivo/run_cluster.sh`

**P: Posso voltar a uma versão anterior?**
R: Sim, com `git revert <commit-hash>` ou `git reset --hard <commit-hash>`

---

**Suporte:** Veja `DIETPI_TROUBLESHOOTING.md` para mais problemas comuns com Git.
