import flet as ft
import obd
import threading
import time
from database import AutomovilesDatabase
from functions.obdConnection import tryConnection
from functions.shift import checkShift
from functions.checkDriving import checkDriving

def dashboard(page: ft.Page):
    page.title = "Menu principal"
    page.scroll = "adaptive"

    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")

    transmision = db.obtener_transmision_por_id_vehiculo()

    # Cerrar conexión
    db.close_connection()

    # Variable global para almacenar los datos OBD
    obdData = ["-", "-", "-", "-", "-", "Desconectado", ft.colors.BLACK]
    tempDisplayTiming = 0
    lastIdMsg = ""

    connection = None


    # Intenta obtener la conexión OBD
    loading_view = ft.View("/dashboard",
        [ft.Column(
            [ft.ProgressRing(), ft.Text("Estableciendo conexion con OBD2...")],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

    page.views.append(loading_view)
    page.update()
    connection = tryConnection()

    def update_data():
        nonlocal obdData
        nonlocal tempDisplayTiming
        nonlocal lastIdMsg
        
        if connection:
            # Obtiene los valores de OBD
            speedValue = connection.query(obd.commands.SPEED).value.magnitude 
            rpmValue = connection.query(obd.commands.RPM).value.magnitude
            coolantValue = connection.query(obd.commands.COOLANT_TEMP).value.magnitude
            throttle = connection.query(obd.commands.THROTTLE_POS).value.magnitude
            engineLoad = connection.query(obd.commands.ENGINE_LOAD).value.magnitude
            elmVoltage = connection.query(obd.commands.ELM_VOLTAGE).value.magnitude
            def shiftValue():
                if speedValue:
                    return checkShift(speedValue, rpmValue, throttle, engineLoad)
                return "-"
            drivingValue = checkDriving(coolantValue, rpmValue, speedValue, throttle, tempDisplayTiming, lastIdMsg)
            tempDisplayTiming = drivingValue[1]
            lastIdMsg = drivingValue[3]

            obdData[:] = [speedValue, rpmValue, coolantValue, elmVoltage, shiftValue(), drivingValue[0], drivingValue[2]]

        # Programa la próxima actualización después de 0.5 segundos
        threading.Timer(1, update_data).start()

    # Llama a la función update_data para la primera actualización
    update_data()

    def infoCard(dataText, color):
        
        cardInformation = ft.Row([
            ft.Icon(name=ft.icons.INFO, ),
            ft.Column([
                ft.Text("Informacion", 
                    theme_style=ft.TextThemeStyle.TITLE_LARGE,
                    weight=ft.FontWeight.BOLD,
                    
                ),

            ], spacing=0.5)
        ])

        card = ft.Container(
            content=(
                ft.Column([
                    cardInformation,
                    ft.Container(
                        content=ft.Text(
                            dataText, 
                            weight=ft.FontWeight.BOLD,
                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                            color=ft.colors.BLACK,
                        ),
                        bgcolor=ft.colors.WHITE70, 
                        border_radius=10,
                        width=300,
                        padding=10,
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
            ),
            margin=10,
            padding=15,
            bgcolor=color,
            width=350,
            border_radius=10,
        )

        return card
        

    def itemCard(icon, titleText, subtitleText, dataText):
        cardInformation = ft.Row([
            ft.Icon(icon),
            ft.Column([
                ft.Text(titleText, 
                    theme_style=ft.TextThemeStyle.TITLE_LARGE,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(subtitleText, 
                    theme_style=ft.TextThemeStyle.LABEL_LARGE,
                    color=ft.colors.INDIGO_200
                ),
            ], spacing=0.5)
        ])

        card = ft.Container(
            content=(
                ft.Row([
                    cardInformation,
                    ft.Container(
                        content=ft.Text(
                            dataText, 
                            weight=ft.FontWeight.BOLD,
                            text_align="CENTER",
                            theme_style=ft.TextThemeStyle.TITLE_LARGE,
                        ),
                        bgcolor=ft.colors.INDIGO_800, 
                        border_radius=10,
                        width=80,
                        height=50,
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ),
            margin=10,
            padding=15,
            bgcolor=ft.colors.INDIGO_500,
            width=350,
            height=100,
            border_radius=10,
        )
        
        return card


    def create_and_update_cards():
        while True:
            print(obdData)
            # Actualizar los datos OBD
            listaItemCard = [
                infoCard(obdData[5], obdData[6]),
                itemCard(ft.icons.ALBUM_OUTLINED, "Velocidad", "KM/H", obdData[0]), 
                itemCard(ft.icons.SPEED, "Revoluciones", "Revoluciones por Minuto", obdData[1]),
                itemCard(ft.icons.AIR, "Temperatura", "Grados Celcius", obdData[2]),
                itemCard(ft.icons.WATER_DROP_OUTLINED, "Batería", "Voltaje de Batería", obdData[3]),
            ]
            if transmision == "1":
                listaItemCard.append(itemCard(ft.icons.ALBUM_OUTLINED, "Marcha", "Subir/Bajar", obdData[4]))

            # Crear una nueva vista con las tarjetas actualizadas
            new_view = ft.View("/dashboard", [
                ft.Container(
                    content=ft.Column([
                         ft.Container(
                            content=ft.Icon(name=ft.icons.ARROW_BACK, size=50),
                            on_click=lambda e: page.go("/")
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Datos", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, text_align=ft.TextAlign.CENTER),
                                *listaItemCard
                            ], spacing=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            alignment=ft.alignment.center
                        )
                    ],)
                ),
            ], scroll=ft.ScrollMode.ALWAYS,)

            # Actualizar la vista en la página
            page.views.clear()
            page.views.append(new_view)
            page.update()

            if connection is None:
                break

            # Esperar 0.5 segundos antes de la próxima actualización
            time.sleep(.5)

    # Iniciar el hilo para crear y actualizar las tarjetas
    threading.Thread(target=create_and_update_cards, daemon=True).start()

    # Devolver una vista vacía inicialmente
    return ft.View("/dashboard")
