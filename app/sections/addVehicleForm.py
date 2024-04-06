import flet as ft
from database import AutomovilesDatabase

def addVehicleForm(page: ft.Page):
    page.title = "Mis vehiculos"
    page.scroll = "adaptive"

    def card(text):
        return ft.Container(
            content=ft.Text(text, theme_style=ft.TextThemeStyle.TITLE_LARGE),

            margin=5,
            padding=10,
            alignment=ft.alignment.center,
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            bgcolor=ft.colors.SURFACE_VARIANT,
            width=(page.width)/2,
            height=(page.height)/4,
            border_radius=10,
            ink=True,
            on_click=lambda e: page.go("/")
        )
    
    card_add = ft.Container(
        content=ft.Icon(ft.icons.ADD_BOX_OUTLINED, size=50),
        margin=5,
        padding=10,
        alignment=ft.alignment.center,
        theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
        theme_mode=ft.ThemeMode.DARK,
        bgcolor=ft.colors.SURFACE_VARIANT,
        width=(page.width)/2,
        height=(page.height)/4,
        border_radius=10,
        ink=True,
        on_click=lambda e: page.go("/")
    )

    vehiculos = AutomovilesDatabase.obtener_vehiculos_registrados()
    cards=[]
    for vehiculo in vehiculos:
        cards.append(card(vehiculo[2] + " " + vehiculo[1]))
    cards.append(card_add)
    
    view = ft.Container(
            content=ft.Column(cards),
            alignment = ft.alignment.center,
            width=page.width,
        )
    
    return view