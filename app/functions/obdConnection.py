import obd

# Función para establecer la conexión con OBD
def tryConnection():
    try:
        ports = obd.scan_serial()  # Intenta escanear los puertos seriales
        connection = obd.OBD(ports[1])  # Conecta al primer puerto encontrado
        if obd.OBD(connection.status() == obd.OBDStatus.ELM_CONNECTED):
            print("Conectado a ELM")
            if obd.OBD(connection.status() == obd.OBDStatus.OBD_CONNECTED):
                print("OBD conectado")
                if obd.OBD(connection.status() == obd.OBDStatus.CAR_CONNECTED):  # Verifica si se encontraron puertos
                    print("Conectado a Auto")
                    return connection
                else:
                    print("El vehiculo no se encuentra en ignicion.")
                    return None
            else:
                print("No hubo conexion a OBD")
                return None
        else:
            print("No hubo conexion a ELM")
            return None
    except Exception as e:
        print("Error al conectar con OBD:", e)
        return None
