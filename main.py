import time
import os
import json 

VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
AZUL = '\033[94m'
RESET = '\033[0m'

ARCHIVO_BD = 'base_datos.json' 

def cargar_datos():
    """Lee el archivo JSON. Si no existe, crea datos por defecto."""
    if os.path.exists(ARCHIVO_BD):
        with open(ARCHIVO_BD, 'r') as archivo:
            return json.load(archivo)
    else:
        datos_por_defecto = {
            "envios": [
                {"id": "001", "destino": "Punta Arenas", "estado": "En Bodega", "carga": "Frigorífica", "co2_ahorro": 120},
                {"id": "002", "destino": "Puerto Montt", "estado": "En Bodega", "carga": "General", "co2_ahorro": 85}
            ],
            "alertas_clima": []
        }
        guardar_datos(datos_por_defecto)
        return datos_por_defecto

def guardar_datos(datos):
    """Escribe los datos actuales en el archivo JSON."""
    with open(ARCHIVO_BD, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

bd = cargar_datos()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print(f"{AZUL}\n" + "="*50)
    print("ECOROUTE LOGISTICS - PANEL DE DESPACHO")
    print("="*50 + f"{RESET}")
    print("1. Ver estado de flota y envíos")
    print("2. Calcular ruta ecológica (IA Simulada)")
    print("3. Reportar incidencia climática")
    print("4. Restaurar base de datos a valores de fábrica") 
    print("5. Salir del sistema")
    print(f"{AZUL}" + "="*50 + f"{RESET}")
    return input(f"{AMARILLO}Seleccione una opción (1-5): {RESET}")

def ver_envios():
    limpiar_pantalla()
    print(f"{AMARILLO}LEYENDO BASE DE DATOS JSON...{RESET}")
    time.sleep(1)
    print(f"\n{AZUL}--- ESTADO DE ENVÍOS ---{RESET}")
    
    for envio in bd["envios"]:
        color_estado = VERDE if envio["estado"] == "En Ruta" else RESET
        print(f"[ID: {envio['id']}] | Destino: {envio['destino']} | Estado: {color_estado}{envio['estado']}{RESET} | Carga: {envio['carga']}")
    
    if bd["alertas_clima"]:
        print(f"\n{ROJO}--- ALERTAS CLIMÁTICAS ACTIVAS ---{RESET}")
        for alerta in bd["alertas_clima"]:
            print(f"{alerta}")

    input(f"\n{AMARILLO}Presione ENTER para volver al menú...{RESET}")

def calcular_ruta():
    limpiar_pantalla()
    print(f"{VERDE}Iniciando motor de asignación IA...{RESET}")
    time.sleep(2)
    
    for envio in bd["envios"]:
        if envio["estado"] == "En Bodega":
            envio["estado"] = "En Ruta"
            guardar_datos(bd) 
            
            print(f"\n{VERDE}RUTA ÓPTIMA CALCULADA PARA ENVÍO [{envio['id']}]{RESET}")
            print(f"   -> Destino: {envio['destino']}")
            print("   -> Vehículo asignado: Camión Eléctrico #42")
            print(f"   -> Impacto Ambiental: Ahorro estimado de {envio['co2_ahorro']} kg de CO2")
            break
    else:
        print(f"\n{AMARILLO}No hay envíos en bodega pendientes de ruta.{RESET}")

    input(f"\n{AMARILLO}Presione ENTER para volver al menú...{RESET}")

def reportar_clima():
    limpiar_pantalla()
    print(f"\n{ROJO}ALERTA METEOROLÓGICA{RESET}")
    clima = input("Ingrese la condición actual en ruta (Ej: Nieve, Lluvia intensa): ")
    
    bd["alertas_clima"].append(clima)
    guardar_datos(bd) 
    
    print(f"\n{VERDE}Condición '{clima}' registrada en la base de datos.{RESET}")
    time.sleep(1.5)

def limpiar_bd():
    """Función de utilidad para el profesor para reiniciar el prototipo"""
    limpiar_pantalla()
    if os.path.exists(ARCHIVO_BD):
        os.remove(ARCHIVO_BD)
    global bd
    bd = cargar_datos()
    print(f"\n{VERDE}Base de datos restaurada correctamente.{RESET}")
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
            limpiar_bd()
        elif opcion == '5':
            limpiar_pantalla()
            print(f"\n{VERDE}Cerrando sistema EcoRoute. ¡Buen viaje!{RESET}\n")
            break
        else:
            print(f"\n{ROJO}ERROR: Opción inválida.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    iniciar_sistema()