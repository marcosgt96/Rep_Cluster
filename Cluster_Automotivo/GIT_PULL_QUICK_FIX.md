# 🚀 Solução Rápida: Erro `git pull`

## 📋 O Seu Erro

```
error: Your local changes to the following files would be overwritten by merge:
        Cluster_Automotivo/run_cluster.sh
Please commit your changes or stash them before you merge.
Aborting
```

---

## ✅ 3 Soluções (Use UMA)

### Solução 1️⃣ (RECOMENDADA) - Stash

Executa no Raspberry Pi:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo
git stash
git pull
git stash pop
```

✅ **Mantém** suas customizações locais

---

### Solução 2️⃣ - Descartar Mudanças

Executa no Raspberry Pi:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo
git checkout -- run_cluster.sh
git pull
```

❌ **Descarta** customizações locais

---

### Solução 3️⃣ - Forçar (Último Recurso)

Executa no Raspberry Pi:

```bash
cd ~/Rep_Cluster/Cluster_Automotivo
git fetch origin
git reset --hard origin/main
```

⚠️ **Cuidado:** Perde todas as mudanças locais

---

## ✅ Após Resolver

```bash
# Reiniciar serviço
sudo systemctl restart cluster-automotivo

# Verificar status
sudo systemctl status cluster-automotivo

# Ver logs
sudo journalctl -u cluster-automotivo -f
```

---

## 📖 Mais Informações

Para compreender melhor o problema e evitar no futuro, veja:
**`GIT_SYNC_GUIDE.md`** - Guia completo com 3 opções detalhadas

---

**Pronto! Seu `git pull` funcionará agora.** 🎉
