import flet as ft
import sqlite3
from database import AutomovilesDatabase

def main(page: ft.Page):
    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")
    
    # Crear tablas
    db.create_tables()

    class Auto:
        def __init__(self, marca, modelo, transmision, combustible):
            self.marca = marca
            self.modelo = modelo
            self.transmision = transmision
            self.combustible = combustible
        
    def button_clicked(e):
        automovil = Auto(marca_dropdown.value, modelo_dropdown.value, transmision_dropdown.value, combustible_dropdown.value)
        output_text.value = f"La marca es: {automovil.marca}\nEl modelo es: {automovil.modelo}\nLa transmision es: {automovil.transmision}\nEl combustible es: {automovil.combustible}"
        page.update()
    
    # Función para cargar los modelos según la marca seleccionada
    def cargar_modelos(e):
        marca_seleccionada = marca_dropdown.value
        modelos = db.get_modelos_por_marca(marca_seleccionada)
        modelo_dropdown.options = [ft.dropdown.Option(modelo) for modelo in modelos]
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Guardar", on_click=button_clicked)
    marca_dropdown = ft.Dropdown(
        on_change=cargar_modelos,
        width="100%",
        label="Marca",
        options=[ft.dropdown.Option(marca) for marca in db.get_marcas()],
    )
    modelo_dropdown = ft.Dropdown(
        width="100%",
        label="Modelo",
        options=[],
    )

    transmision_dropdown = ft.Dropdown(
        width="100%",
        label="Transmision",
        options=[
            ft.dropdown.Option("Automatico"),
            ft.dropdown.Option("Manual"),
        ],
    )
    combustible_dropdown = ft.Dropdown(
        width="100%",
        label="Combustible",
        options=[
            ft.dropdown.Option("Nafta"),
            ft.dropdown.Option("Diesel"),
        ],
    )
    
    # Cerrar conexión
    db.close_connection()
    page.add(marca_dropdown, modelo_dropdown, transmision_dropdown, combustible_dropdown, submit_btn, output_text)

ft.app(target=main)