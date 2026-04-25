@echo off
REM ============================================
REM Script de Deploy - Cluster Automotivo
REM Para Windows - Copia arquivos para Raspberry Pi
REM ============================================

echo ============================================
echo   🚗 Cluster Automotivo - Deploy para Raspberry
echo ============================================
echo.

REM Configurações - ALTERE ESTES VALORES
set RPI_HOST=cluster-automotivo.local
set RPI_USER=pi
set RPI_PASSWORD=cluster
set RPI_PATH=/home/cluster/Cluster_Automotivo

echo Configuracoes:
echo   Host: %RPI_HOST%
echo   Usuario: %RPI_USER%
echo   Caminho: %RPI_PATH%
echo.

REM Verificar se PSCP está disponível
where pscp >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERRO: pscp nao encontrado
    echo.
    echo Instale o Putty ou adicione ao PATH:
    echo https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
    echo.
    echo Ou use o Windows Terminal com OpenSSH:
    echo   scp -r .\* %RPI_USER%@%RPI_HOST%:%RPI_PATH%
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo PASSO 1: Conectando ao Raspberry...
echo ============================================

REM Criar diretório remoto
echo Criando diretorio remoto...
echo %RPI_PASSWORD% | pscp -batch -pw %RPI_PASSWORD% %RPI_USER%@%RPI_HOST% "mkdir -p %RPI_PATH%" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo (aviso: diretorio pode ja existir)
)

echo.
echo ============================================
echo PASSO 2: Copiando arquivos...
echo ============================================

REM Copiar todos os arquivos
echo Copiando vehicle_sensors.py...
pscp -batch -pw %RPI_PASSWORD% vehicle_sensors.py %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando cluster_gui.py...
pscp -batch -pw %RPI_PASSWORD% cluster_gui.py %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando cluster_demo.py...
pscp -batch -pw %RPI_PASSWORD% cluster_demo.py %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando cluster_quick_test.py...
pscp -batch -pw %RPI_PASSWORD% cluster_quick_test.py %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando cluster_setup.py...
pscp -batch -pw %RPI_PASSWORD% cluster_setup.py %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando requirements.txt...
pscp -batch -pw %RPI_PASSWORD% requirements.txt %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando install.sh...
pscp -batch -pw %RPI_PASSWORD% install.sh %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo Copiando pasta tests...
pscp -batch -pw %RPI_PASSWORD% -r tests %RPI_USER%@%RPI_HOST%:%RPI_PATH%/

echo.
echo ============================================
echo PASSO 3: Instalando dependências...
echo ============================================

echo Executando instalacao no Raspberry...
plink -batch -pw %RPI_PASSWORD% %RPI_USER%@%RPI_HOST% "cd %RPI_PATH% && pip3 install -r requirements.txt"

echo.
echo ============================================
echo PASSO 4: Testando...
echo ============================================

echo Verificando importacao...
plink -batch -pw %RPI_PASSWORD% %RPI_USER%@%RPI_HOST% "cd %RPI_PATH% && python3 -c 'from vehicle_sensors import VehicleSensorSimulator; print(OK)'"

echo.
echo ============================================
echo   ✅ Deploy Concluido!
echo ============================================
echo.
echo Para executar no Raspberry:
echo   ssh %RPI_USER%@%RPI_HOST%
echo   cd %RPI_PATH%
echo   python3 cluster_gui.py
echo.
pause