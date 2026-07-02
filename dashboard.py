import streamlit as st
import json
import time

ARCHIVO_BD = 'base_datos.json'

def cargar_datos():
    with open(ARCHIVO_BD, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_datos(datos):
    with open(ARCHIVO_BD, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

st.set_page_config(page_title="EcoRoute Panel", page_icon="🚛", layout="wide")

st.title("🚛 EcoRoute Logistics - Centro de Control Inteligente")
st.markdown("Monitor de flota y asignación de rutas mediante IA simulada.")
st.markdown("---")

bd = cargar_datos()

col1, col2 = st.columns(2)

with col1:
    st.header("📦 Envíos Registrados")
    for envio in bd["envios"]:
        if envio["estado"] == "En Bodega":
            st.warning(f"**ID: {envio['id']}** | Destino: {envio['destino']} | Estado: {envio['estado']} | ♻️ Ahorro: {envio['co2_ahorro']}kg CO2")
        else:
            st.success(f"**ID: {envio['id']}** | Destino: {envio['destino']} | Estado: {envio['estado']} | ♻️ Ahorro: {envio['co2_ahorro']}kg CO2")

with col2:
    st.header("🚚 Flota de Vehículos")
    for camion in bd["camiones"]:
        if camion["estado"] == "Disponible":
            st.info(f"**{camion['modelo']}** | Patente: {camion['patente']} | Estado: {camion['estado']}")
        elif camion["estado"] == "En Ruta":
            st.success(f"**{camion['modelo']}** | Patente: {camion['patente']} | Estado: {camion['estado']}")
        else:
            st.error(f"**{camion['modelo']}** | Patente: {camion['patente']} | Estado: {camion['estado']}")

st.markdown("---")
st.header("🧠 Motor de Asignación Automatizada")

# Botón interactivo web
if st.button("Calcular Ruta Óptima y Asignar Flota", type="primary", use_container_width=True):
    asignacion_exitosa = False
    
    for envio in bd["envios"]:
        if envio["estado"] == "En Bodega":
            camion_asignado = None
            for camion in bd["camiones"]:
                if camion["estado"] == "Disponible":
                    camion_asignado = camion
                    break
            
            if camion_asignado:
                envio["estado"] = "En Ruta"
                camion_asignado["estado"] = "En Ruta"
                guardar_datos(bd) 
                
                st.success(f"✅ ÉXITO: El envío {envio['id']} con destino a {envio['destino']} ha sido asignado al {camion_asignado['modelo']} ({camion_asignado['patente']}).")
                asignacion_exitosa = True
                time.sleep(2) 
                st.rerun() 
                break 
            else:
                st.error(f"❌ ALERTA LOGÍSTICA: No hay camiones 'Disponibles' para el envío {envio['id']}.")
                asignacion_exitosa = True
                break

    if not asignacion_exitosa:
        st.info("Todos los envíos actuales ya se encuentran en ruta.")