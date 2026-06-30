import time
def mostrar_menu():
    print("\n"+"="*45)
    print("ECOROUTE LOGISTISCS - PANEL DE DESPACHO")
    print("="*45)
    print("1. ver estado de la Flota y envios pendientes")
    print("2. Calcular rutas ecologica")
    print("3. Reportar incidencia climatica")
    print("4. Salir del sistema")
    print("="*45)
    return input("Seleccione una opción: ")

def ver_envios():
    print("\n OBTENIENDO DATOS DE BODEGA...")
    time.sleep(1)
    print("\n--- Envios pendientes ---")
    print("[ID: 001] | Destino: Punta Arenas | Estado: En Bodega | Carga: Frigorifica")
    print("[ID: 002] | Destino: Puerto Montt | Estado: En Bodega | Carga: General")

def calcular_ruta():
    print("\n Iniciando motor de asignacion IA para envio [001]...")
    time.sleep(2)
    print("\n RUTA OPTIMA CALCULADA:")
    print("   -> vehiculo asignado: Camion Electrico #42 (Licencia Validad)")
    print("   -> Ruta Seleccionada: Ruta 5 Sur (Desvio en tramo 4 por lluvias)")
    print("   -> Impacto Ambiental: Ahorro estimnado de 120Kg de CO2")
    print("   -> Viaticos Calculados: $45.000 CLP (Peajes y Carga Electrica)")

def reportar_clima():
    print("\n Alerta METEOROLOGICA")
    clima = input("Ingrese la condicion actual en la ruta (ej: Lluvia intensa, Nieve, Viento Fuerte): ")
    print(f"Recibido. Condicion '{clima}' registrada. Recalculando rutas alternativas...")

def iniciar_sistema():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            ver_envios()
        elif opcion == "2":
            calcular_ruta()
        elif opcion == "3":
            reportar_clima()
        elif opcion == "4":
            print("\n Cerrando sistema EcoRoute de Forma Segura... Que tengas un buen Viaje \n")
            break
        else:
            print("\n Opcion invalida. Por favor, seleccione una opcion del 1 al 4.")             

if __name__ == "__main__":
    iniciar_sistema()            