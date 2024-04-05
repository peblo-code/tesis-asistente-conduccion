import flet as ft
from database import AutomovilesDatabase

def addVehicleForm(page: ft.Page):
    page.title = "Mis vehiculos"
    page.scroll = "adaptive"

    def card(text):
        display_text = None
        if text == "+":
            display_text = ft.Icon(ft.icons.ADD_BOX_OUTLINED, size=50)
        else:
            display_text = ft.Text(text, theme_style=ft.TextThemeStyle.TITLE_LARGE)
        return ft.Container(
            content=ft.Column([
                    display_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            margin=5,
            padding=10,
            alignment=ft.alignment.center,
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            bgcolor=ft.colors.SURFACE_VARIANT,
            width=(page.width)/2,
            height=250,
            border_radius=10,
            ink=True,
            on_click=lambda e: page.go("/")
        )

    
    view = ft.Container(
            content=ft.Column([
                card("Toyota Auris"),
                card("+")
            ]),
            alignment = ft.alignment.center,
            width=page.width
        )
    
    return view