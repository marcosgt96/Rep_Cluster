#!/usr/bin/env python3
"""
Script de Configuração e Execução do Cluster Automotivo
Facilita a instalação e uso no Raspberry Pi
"""

import os
import sys
import subprocess
import platform


def print_header(title):
    """Imprime cabeçalho formatado"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def check_python_version():
    """Verifica versão do Python"""
    print_header("Verificando Versão Python")
    
    version = sys.version_info
    py_version = f"{version.major}.{version.minor}.{version.micro}"
    
    print(f"✓ Python {py_version}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ é necessário!")
        sys.exit(1)
    
    return py_version


def check_tkinter():
    """Verifica se tkinter está instalado"""
    print_header("Verificando Tkinter")
    
    try:
        import tkinter
        print("✓ Tkinter já está instalado")
        return True
    except ImportError:
        print("❌ Tkinter não encontrado!")
        
        if platform.system() == "Linux":
            print("\nPara instalar Tkinter:")
            print("  Debian/Ubuntu/Raspberry Pi OS:")
            print("    sudo apt install python3-tk")
            print("  Fedora/RHEL:")
            print("    sudo dnf install python3-tkinter")
        
        return False


def install_requirements():
    """Instala dependências do requirements.txt"""
    print_header("Instalando Dependências Python")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✓ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Erro ao instalar dependências")
        return False


def run_demo():
    """Executa demonstração"""
    print_header("Executando Demonstração")
    
    try:
        exec(open("cluster_demo.py").read())
    except FileNotFoundError:
        print("❌ cluster_demo.py não encontrado")
    except Exception as e:
        print(f"❌ Erro: {e}")


def run_tests():
    """Executa testes"""
    print_header("Executando Testes")
    
    try:
        subprocess.call([sys.executable, "-m", "pytest", "tests/test_vehicle_sensors.py", "-v"])
    except FileNotFoundError:
        print("❌ pytest não encontrado")


def run_gui(fullscreen=False):
    """Executa GUI do cluster"""
    print_header("Iniciando Interface Gráfica do Cluster")
    
    print(f"Fullscreen: {'Sim' if fullscreen else 'Não'}")
    print("\nDicas:")
    print("  • Pressione ESC para sair (modo fullscreen)")
    print("  • Use os botões para controlar a simulação")
    print("  • Pressione ALT+F4 para fechar (modo janelado)")
    
    try:
        if fullscreen:
            # Modificar temporariamente o arquivo
            with open("cluster_gui.py", "r") as f:
                content = f.read()
            
            content_mod = content.replace("fullscreen=False", "fullscreen=True")
            
            # Executar modificado
            exec(content_mod)
        else:
            exec(open("cluster_gui.py").read())
    except FileNotFoundError:
        print("❌ cluster_gui.py não encontrado")
    except Exception as e:
        print(f"❌ Erro: {e}")


def show_menu():
    """Exibe menu principal"""
    while True:
        print_header("CLUSTER AUTOMOTIVO - Menu Principal")
        
        print("1. Executar Demonstração (CLI)")
        print("2. Executar Testes")
        print("3. Executar GUI (Modo Janelado)")
        print("4. Executar GUI (Fullscreen)")
        print("5. Verificar Dependências")
        print("6. Instalar Dependências")
        print("0. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            run_demo()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            run_gui(fullscreen=False)
            break
        elif choice == "4":
            run_gui(fullscreen=True)
            break
        elif choice == "5":
            check_python_version()
            check_tkinter()
            print("\n✓ Verificação completa")
        elif choice == "6":
            install_requirements()
        elif choice == "0":
            print("\n👋 Até logo!")
            break
        else:
            print("\n❌ Opção inválida!")


def main():
    """Função principal"""
    print_header("CLUSTER AUTOMOTIVO - Configuração Inicial")
    
    # Verificações iniciais
    py_version = check_python_version()
    tkinter_ok = check_tkinter()
    
    if not tkinter_ok:
        install_choice = input("\nTentar instalar Tkinter? (s/n): ").strip().lower()
        if install_choice == "s":
            if platform.system() == "Linux":
                print("\nExecutando: sudo apt install python3-tk")
                os.system("sudo apt install -y python3-tk")
        else:
            print("\n⚠️  Aviso: Tkinter é necessário para a GUI")
    
    # Menu
    show_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrompido pelo usuário")
        sys.exit(0)
