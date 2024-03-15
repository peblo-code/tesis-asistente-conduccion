import obd

# Función para establecer la conexión con OBD
def tryConnection():
    try:
        # Inicializa la conexión OBD-II      
        ports = obd.scan_serial()      # return list of valid USB or RF ports          
        connection = obd.OBD(ports[1]) # connect to the first port in the list

        return connection
    except Exception as e:
        print("Error al conectar con OBD:", e)
        return None
