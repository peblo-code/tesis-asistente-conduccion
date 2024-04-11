import sqlite3

class AutomovilesDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Marca (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT NOT NULL
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Modelo (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT NOT NULL,
                                marca_id INTEGER,
                                FOREIGN KEY (marca_id) REFERENCES Marca(id)
                            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Vehiculos (
                                id INTEGER PRIMARY KEY,
                                modelo_id INTEGER,
                                transmision TEXT,
                                combustible TEXT,
                                FOREIGN KEY (modelo_id) REFERENCES Modelo(id)
                            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT NOT NULL,
                                vehiculo_id INTEGER,
                                FOREIGN KEY (vehiculo_id) REFERENCES Vehiculos(id)
                            )''')


        self.connection.commit()

        # Verificar si las tablas están vacías
        self.cursor.execute("SELECT COUNT(*) FROM Marca")
        count = self.cursor.fetchone()[0]
        if count == 0:
            # Insertar marcas y obtener sus IDs
            marcas = ["Toyota", "Nissan", "Mitsubishi"]
            marcas_ids = {}
            for marca in marcas:
                marcas_ids[marca] = self.insert_marca(marca)

            # Insertar modelos vinculados a las marcas
            modelos = {
                "Toyota": ["Corolla", "Premio", "Allion"],
                "Nissan": ["Tida", "Sunny", "Patrol"],
                "Mitsubishi": ["L200", "Lancer", "Mirage"]
            }
            for marca, modelos_list in modelos.items():
                for modelo in modelos_list:
                    self.insert_modelo(modelo, marcas_ids[marca])

    def verify_user(self):
        # Verificar si las tablas están vacías
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM Usuarios")
        count = cursor.fetchone()[0]

        cursor.close()
        connection.close()
        
        if count > 0:
            return True
        return False
    
    def insert_marca(self, nombre):
        self.cursor.execute("INSERT INTO Marca (nombre) VALUES (?)", (nombre,))
        self.connection.commit()
        return self.cursor.lastrowid  # Devolver el ID de la marca insertada

    def insert_modelo(self, nombre, marca_id):
        self.cursor.execute("INSERT INTO Modelo (nombre, marca_id) VALUES (?, ?)", (nombre, marca_id))
        self.connection.commit()

    def insert_vehiculo(self, modelo_id, transmision, combustible):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Vehiculos (modelo_id, transmision, combustible) VALUES (?, ?, ?)", (modelo_id, transmision, combustible))
        connection.commit()

        cursor.close()
        connection.close()
        return cursor.lastrowid  # Devolver el ID de la marca insertada
    
    def editar_vehiculo_por_id(self, vehiculo_id, modelo_id, transmision, combustible):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE Vehiculos SET modelo_id = ?, transmision = ?, combustible = ? WHERE id = ?", (modelo_id, transmision, combustible, vehiculo_id))
        connection.commit()

        cursor.close()
        connection.close()


    def insert_usuario(self, nombre, vehiculo_id):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Usuarios (nombre, vehiculo_id) VALUES (?, ?)", (nombre, vehiculo_id))
        connection.commit()

        cursor.close()
        connection.close()

    def get_marcas(self):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        self.cursor.execute("SELECT id, nombre FROM Marca")
    
        cursor.close()
        connection.close()
        return self.cursor.fetchall()

    def get_modelos_por_marca(self, marca_id):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("SELECT id, nombre FROM Modelo WHERE marca_id = ?", (marca_id,))
        modelos = cursor.fetchall()

        cursor.close()
        connection.close()

        return modelos
    
    def obtener_transmision_por_id_vehiculo(self, vehiculo_id):
        self.cursor.execute("SELECT transmision FROM Vehiculos WHERE id = ?", (vehiculo_id,))
        transmision = self.cursor.fetchone()
        if transmision:
            return transmision[0]
        else:
            return None
    
    def obtener_vehiculo_por_id(self, vehiculo_id):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Vehiculos WHERE id = ?", (vehiculo_id,))
        vehiculo = cursor.fetchone()

        cursor.close()
        connection.close()

        return vehiculo
        
    def obtener_vehiculos_registrados(self):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        # Consulta para obtener todos los vehículos
        cursor.execute("SELECT Vehiculos.id, Modelo.nombre, Marca.nombre, Vehiculos.transmision, Vehiculos.combustible FROM Vehiculos INNER JOIN Modelo ON Vehiculos.modelo_id = Modelo.id INNER JOIN Marca ON Modelo.marca_id = Marca.id")

        vehiculos = cursor.fetchall()

        cursor.close()
        connection.close()

        return vehiculos



    def close_connection(self):
        self.connection.close()
