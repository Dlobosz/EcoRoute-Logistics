import time
import os

VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
AZUL = '\033[94m'
RESET = '\033[0m'

envios_pendientes = [
    {"id": "001", "destino": "Punta Arenas", "estado": "En Bodega", "carga": "Frigorífica", "co2_ahorro": 120},
    {"id": "002", "destino": "Puerto Montt", "estado": "En Bodega", "carga": "General", "co2_ahorro": 85}
]

alertas_clima = []

def limpiar_pantalla():
    """Limpia la consola para mejorar la interfaz de usuario"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print(f"{AZUL}\n" + "="*50)
    print(" 🚛 ECOROUTE LOGISTICS - PANEL DE DESPACHO 🚛")
    print("="*50 + f"{RESET}")
    print("1. Ver estado de flota y envíos")
    print("2. Calcular ruta ecológica (IA Simulada)")
    print("3. Reportar incidencia climática")
    print("4. Salir del sistema")
    print(f"{AZUL}" + "="*50 + f"{RESET}")
    return input(f"{AMARILLO}Seleccione una opción (1-4): {RESET}")

def ver_envios():
    limpiar_pantalla()
    print(f"{AMARILLO}📦 OBTENIENDO DATOS DE BODEGA...{RESET}")
    time.sleep(1)
    print(f"\n{AZUL}--- ESTADO DE ENVÍOS ---{RESET}")
    
    for envio in envios_pendientes:
        color_estado = VERDE if envio["estado"] == "En Ruta" else RESET
        print(f"[ID: {envio['id']}] | Destino: {envio['destino']} | Estado: {color_estado}{envio['estado']}{RESET} | Carga: {envio['carga']}")
    
    if alertas_clima:
        print(f"\n{ROJO}--- ALERTAS CLIMÁTICAS ACTIVAS ---{RESET}")
        for alerta in alertas_clima:
            print(f"⚠️ {alerta}")

    input(f"\n{AMARILLO}Presione ENTER para volver al menú...{RESET}")

def calcular_ruta():
    limpiar_pantalla()
    print(f"{VERDE}🌱 Iniciando motor de asignación IA...{RESET}")
    time.sleep(2)
    
    for envio in envios_pendientes:
        if envio["estado"] == "En Bodega":
            envio["estado"] = "En Ruta"
            print(f"\n✅ {VERDE}RUTA ÓPTIMA CALCULADA PARA ENVÍO [{envio['id']}]{RESET}")
            print(f"   -> Destino: {envio['destino']}")
            print("   -> Vehículo asignado: Camión Eléctrico #42 (Licencia validada)")
            print(f"   -> Impacto Ambiental: Ahorro estimado de {envio['co2_ahorro']} kg de CO2")
            print("   -> Viáticos calculados: $45.000 CLP (Peajes y carga eléctrica)")
            break
    else:
        print(f"\n{AMARILLO}No hay envíos en bodega pendientes de ruta.{RESET}")

    input(f"\n{AMARILLO}Presione ENTER para volver al menú...{RESET}")

def reportar_clima():
    limpiar_pantalla()
    print(f"\n{ROJO}⚠️ ALERTA METEOROLÓGICA{RESET}")
    clima = input("Ingrese la condición actual en ruta (Ej: Nieve, Lluvia intensa): ")
    
    alertas_clima.append(clima)
    print(f"\n{VERDE}Recibido. Condición '{clima}' registrada. Recalculando rutas de la zona...{RESET}")
    time.sleep(1.5)

def iniciar_sistema():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            ver_envios()
        elif opcion == '2':
            calcular_ruta()
        elif opcion == '3':
            reportar_clima()
        elif opcion == '4':
            limpiar_pantalla()
            print(f"\n{VERDE}Cerrando sistema EcoRoute de forma segura. ¡Buen viaje! 👋{RESET}\n")
            break
        else:
            print(f"\n{ROJO}❌ ERROR: Opción inválida. Por favor, ingrese un número del 1 al 4.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    iniciar_sistema()