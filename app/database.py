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

    def insert_usuario(self, nombre, vehiculo_id):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Usuarios (nombre, vehiculo_id) VALUES (?, ?)", (nombre, vehiculo_id))
        connection.commit()

        cursor.close()
        connection.close()

    def get_marcas(self):
        self.cursor.execute("SELECT id, nombre FROM Marca")
        return self.cursor.fetchall()

    def get_modelos_por_marca(self, marca_id):
        connection = sqlite3.connect("automoviles.db")
        cursor = connection.cursor()

        cursor.execute("SELECT id, nombre FROM Modelo WHERE marca_id = ?", (marca_id,))
        modelos = cursor.fetchall()

        cursor.close()
        connection.close()

        return modelos

    def close_connection(self):
        self.connection.close()
