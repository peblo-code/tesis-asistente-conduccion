import flet as ft
from sections.formVehicle import formVehicle
from database import AutomovilesDatabase

def menu(page: ft.Page):
    page.title = "Menu principal"
    page.scroll = "adaptive"

    card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")

    # Cerrar conexión
    db.close_connection()

    page.add(
        ft.Text("MENU", 
            theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            text_align="CENTER",
        ),
        card
    )
