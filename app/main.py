import flet as ft
from sections.formVehicle import formVehicle
from sections.menu import menu
from database import AutomovilesDatabase

# Crear instancia de la base de datos
db = AutomovilesDatabase("automoviles.db")

# Crear tablas
db.create_tables()

userExistence = db.verify_user()

if not userExistence:
    ft.app(target=formVehicle)

else:
    ft.app(target=menu)