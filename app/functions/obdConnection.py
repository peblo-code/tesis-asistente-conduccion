import obd

# Función para establecer la conexión con OBD
def tryConnection():
    try:
        ports = obd.scan_serial()  # Intenta escanear los puertos seriales
        if ports:  # Verifica si se encontraron puertos
            connection = obd.OBD(ports[0])  # Conecta al primer puerto encontrado
            return connection
        else:
            print("No se encontraron puertos seriales disponibles.")
            return None
    except Exception as e:
        print("Error al conectar con OBD:", e)
        return None