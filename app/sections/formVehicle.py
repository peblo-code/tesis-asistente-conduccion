import flet as ft
from app.database import AutomovilesDatabase

def formVehicle(page: ft.Page):
    page.title = "Formulario del Usuario"
    page.scroll = "adaptive"
    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")
    isFirstUser = db.verify_user()

    class Auto:
        def __init__(self, marca, modelo, transmision, combustible):
            self.marca = marca
            self.modelo = modelo
            self.transmision = transmision
            self.combustible = combustible
        
    def button_clicked(e):
        automovil = Auto(marca_dropdown.value, modelo_dropdown.value, transmision_dropdown.value, combustible_dropdown.value)
        id_vehiculo = db.insert_vehiculo(automovil.modelo, automovil.transmision, automovil.combustible)
        if(not isFirstUser):
            db.insert_usuario(username.value, id_vehiculo)
            #output_text.value = f"El nombre de usuario es: {usuario}\nLa marca es: {automovil.marca}\nEl modelo es: {automovil.modelo}\nLa transmision es: {automovil.transmision}\nEl combustible es: {automovil.combustible}"
            page.go("/")
            page.update()
        else:
            page.go("/vehicleList")
            page.update()
    
    # Función para cargar los modelos según la marca seleccionada
    def cargar_modelos(e):
        marca_seleccionada = marca_dropdown.value
        modelos = db.get_modelos_por_marca(marca_seleccionada)
        modelo_dropdown.options = [ft.dropdown.Option(key=id_modelo, text=modelo) for id_modelo, modelo in modelos]
        page.update()

    #output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Guardar", on_click=button_clicked)

    username = ft.TextField(
        label="Nombre y Apellido",
        width="100%",
        visible=not isFirstUser
    )
    marca_dropdown = ft.Dropdown(
        on_change=cargar_modelos,
        width="100%",
        label="Marca",
        options=[ft.dropdown.Option(text=marca, key=id_marca) for id_marca, marca in db.get_marcas()],
    )
    modelo_dropdown = ft.Dropdown(
        width="100%",
        label="Modelo",
        options=[],
    )

    transmision_dropdown = ft.Dropdown(
        width="100%",
        label="Transmisión",
        options=[
            ft.dropdown.Option(key=0, text="Automática"),
            ft.dropdown.Option(key=1, text="Manual"),
        ],
    )
    combustible_dropdown = ft.Dropdown(
        width="100%",
        label="Combustible",
        options=[
            ft.dropdown.Option(key=0, text="Nafta"),
            ft.dropdown.Option(key=1, text="Diesel"),
        ],
    )
    
    # Cerrar conexión
    db.close_connection()
    view = ft.SafeArea(
        ft.Column([
            ft.Container(
                content=ft.Icon(name=ft.icons.ARROW_BACK, size=50),
                on_click=lambda e: page.go("/vehicleList"),
                visible=isFirstUser
            ),
            ft.Text("Datos del Vehiculo", 
                theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                text_align="CENTER",
            ),
            username,
            marca_dropdown, 
            modelo_dropdown, 
            transmision_dropdown, 
            combustible_dropdown, 
            submit_btn
            #output_text
        ])
    )

    return view
