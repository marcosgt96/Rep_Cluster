"""
Script de demonstração do Cluster Automotivo
Simula cenários de condução
"""

from vehicle_sensors import VehicleSensorSimulator, VehicleData
import time
import sys


def print_separator(title=""):
    """Imprime uma linha separadora"""
    if title:
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}\n")
    else:
        print("=" * 60)


def format_data(data: VehicleData) -> str:
    """Formata dados para exibição"""
    return (
        f"  Velocidade:      {data.speed_kmh:>6.1f} km/h\n"
        f"  RPM:             {data.rpm:>6.0f} rpm\n"
        f"  Combustível:     {data.fuel_level:>6.1f} %\n"
        f"  Temp. Ar.:       {data.coolant_temp:>6.1f} °C\n"
        f"  Pressão Óleo:    {data.oil_pressure:>6.2f} bar\n"
        f"  Temp. Trans.:    {data.transmission_oil_temp:>6.1f} °C"
    )


def scenario_startup():
    """Simula partida do veículo"""
    print_separator("CENÁRIO 1: PARTIDA DO MOTOR")
    sensor = VehicleSensorSimulator()
    
    print("Iniciando motor...")
    sensor.start_engine()
    
    for i in range(3):
        data = sensor.get_current_data()
        print(f"\nTempo {i}s:")
        print(format_data(data))
        time.sleep(1)


def scenario_acceleration():
    """Simula aceleração progressiva"""
    print_separator("CENÁRIO 2: ACELERAÇÃO PROGRESSIVA")
    sensor = VehicleSensorSimulator()
    sensor.start_engine()
    
    print("Acelerando de 0 a ~100 km/h...")
    
    for step in range(5):
        sensor.accelerate(200)
        sensor.consume_fuel(0.5)
        data = sensor.get_current_data()
        print(f"\nPasso {step + 1}:")
        print(format_data(data))
        time.sleep(0.5)


def scenario_driving():
    """Simula condução normal"""
    print_separator("CENÁRIO 3: CONDUÇÃO NORMAL")
    sensor = VehicleSensorSimulator()
    sensor.start_engine()
    
    print("Simulando condução normal por 10 segundos...")
    
    acelerando = True
    for i in range(10):
        if acelerando and sensor.rpm < 3000:
            sensor.accelerate(150)
        elif sensor.rpm > 2000:
            sensor.decelerate(100)
        
        sensor.consume_fuel(0.2)
        data = sensor.get_current_data()
        
        print(f"\nSegundo {i + 1}:")
        print(format_data(data))
        time.sleep(1)


def scenario_high_speed():
    """Simula velocidade alta"""
    print_separator("CENÁRIO 4: VELOCIDADE ALTA")
    sensor = VehicleSensorSimulator()
    sensor.start_engine()
    
    print("Acelerando até ~200 km/h...")
    
    # Acelerar rapidamente
    for _ in range(15):
        sensor.accelerate(300)
        sensor.consume_fuel(1.0)
    
    data = sensor.get_current_data()
    print(f"\nVelocidade máxima atingida:")
    print(format_data(data))
    
    # Manter velocidade
    print("\n\nMantendo velocidade por 5 segundos...")
    for i in range(5):
        sensor.consume_fuel(0.5)
        data = sensor.get_current_data()
        print(f"\nSegundo {i + 1}:")
        print(format_data(data))
        time.sleep(1)


def scenario_cooldown():
    """Simula resfriamento do motor"""
    print_separator("CENÁRIO 5: DESLIGAMENTO E RESFRIAMENTO")
    sensor = VehicleSensorSimulator()
    sensor.start_engine()
    
    # Aquecer
    print("Aquecendo o motor...")
    for _ in range(10):
        sensor.accelerate(200)
    
    print("\nMotor aquecido! Desligando...")
    sensor.stop_engine()
    
    data = sensor.get_current_data()
    print(f"\nMomentaneamente após desligamento:")
    print(format_data(data))


def scenario_with_warnings():
    """Simula condições que acionam avisos"""
    print_separator("CENÁRIO 6: CONDIÇÕES DE ALERTA")
    sensor = VehicleSensorSimulator()
    sensor.start_engine()
    
    # Simular combustível baixo
    sensor.fuel = 5.0
    print("Combustível baixo!")
    
    # Simulation de superaquecimento
    print("Forçando superaquecimento...")
    sensor.coolant_temp = 120.0
    sensor.oil_pressure = 0.5
    
    data = sensor.get_current_data()
    print(f"\nEstado critico detectado:")
    print(format_data(data))
    
    print("\n⚠️  ALERTAS:")
    if data.fuel_level < 10:
        print("  • COMBUSTÍVEL CRITICO - Abasteça imediatamente!")
    if data.coolant_temp > 110:
        print("  • TEMPERATURA DO MOTOR CRITICA - Parar motor agora!")
    if data.oil_pressure < 1.0:
        print("  • PRESSÃO DE ÓLEO BAIXA - Problema no motor!")


def main():
    """Executa todos os cenários"""
    print("\n" + "=" * 60)
    print("  DEMONSTRAÇÃO DO CLUSTER AUTOMOTIVO")
    print("=" * 60)
    
    try:
        scenario_startup()
        time.sleep(1)
        
        scenario_acceleration()
        time.sleep(1)
        
        scenario_driving()
        time.sleep(1)
        
        scenario_high_speed()
        time.sleep(1)
        
        scenario_cooldown()
        time.sleep(1)
        
        scenario_with_warnings()
        
        print_separator("DEMONSTRAÇÃO CONCLUÍDA")
        print("✓ Todos os cenários foram executados com sucesso!")
        
    except KeyboardInterrupt:
        print("\n\n❌ Demonstração interrompida pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
