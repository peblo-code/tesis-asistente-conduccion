import flet as ft
import obd
from sections.formVehicle import formVehicle
from database import AutomovilesDatabase
from functions.obdConnection import tryConnection

def menu(page: ft.Page):
    page.title = "Menu principal"
    page.scroll = "adaptive"

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
            ], alignment = ft.MainAxisAlignment.CENTER, spacing=0.5)
        ])

        card = ft.Container(
            content=(
                ft.Row([
                    cardInformation,
                    ft.Container(
                        content = ft.Text(
                            dataText, 
                            weight=ft.FontWeight.BOLD, 
                            theme_style=ft.TextThemeStyle.TITLE_LARGE,
                        ),
                        bgcolor=ft.colors.INDIGO_800, 
                        border_radius=10,
                        width=80,
                        height=50,
                        alignment=ft.alignment.center,
                    )
                ], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
            ),
            margin=10,
            padding=15,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.INDIGO_500,
            width=350,
            height=100,
            border_radius=10,
        )
        
        return card



    def column_with_alignment(align: ft.MainAxisAlignment):
        obdData = ["-","-","-","-"]
        if tryConnection():
            connection = tryConnection()
            speedValue = connection.query(obd.commands.SPEED).value
            rpmValue = connection.query(obd.commands.RPM).value
            coolantValue = connection.query(obd.commands.COOLANT_TEMP).value
            fuelRateValue = connection.query(obd.commands.FUEL_RATE).value
            obdData = [speedValue, rpmValue, coolantValue, fuelRateValue]
        return ft.Row(
            [
                ft.Container(
                    content=ft.Column([
                        ft.Text("Datos", 
                            theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                            text_align="CENTER"
                        ),
                        itemCard(ft.icons.ALBUM_OUTLINED, "Velocidad", "KM/H", obdData[0]), 
                        itemCard(ft.icons.SPEED, "Revoluciones", "Revoluciones por Minuto", obdData[1]),
                        itemCard(ft.icons.AIR, "Temperatura", "Grados Celcius", obdData[2]),
                        itemCard(ft.icons.WATER_DROP_OUTLINED, "Consumo", "Litros por Hora", obdData[3]),
                    ], spacing=1),
                ),
            ], alignment=align,
        )

    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")

    # Cerrar conexión
    db.close_connection()

    page.add(
        column_with_alignment(ft.MainAxisAlignment.CENTER),
    )
