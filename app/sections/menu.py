import flet as ft
from sections.formVehicle import formVehicle
from database import AutomovilesDatabase

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
        return ft.Row(
            [
                ft.Container(
                    content=ft.Column([
                        ft.Text("Datos", 
                            theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                            text_align="CENTER"
                        ),
                        itemCard(ft.icons.ALBUM_OUTLINED, "Velocidad", "KM/H", "80"), 
                        itemCard(ft.icons.SPEED, "Revoluciones", "Revoluciones por Minuto", "2350"),
                        itemCard(ft.icons.AIR, "Temperatura", "Grados Celcius", "87"),
                        itemCard(ft.icons.WATER_DROP_OUTLINED, "Consumo", "Litros por Hora", "5.2"),
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
