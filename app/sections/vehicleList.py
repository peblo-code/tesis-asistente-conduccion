import flet as ft
from database import AutomovilesDatabase

def vehicleList(page: ft.Page):
    page.title = "Mis vehiculos"
    page.scroll = "adaptive"

    def card(car_name, transmision, combustible):
        texto_transmision = "Automático"
        texto_combustible = "Nafta"
        if transmision == 1:
            texto_transmision = "Manual"
        if combustible == 1:
            texto_combustible = "Diésel"
        return ft.Container(
            content=ft.Column([
                ft.Text(car_name, theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Row([
                    ft.Icon(name=ft.icons.CAR_CRASH_SHARP, color=ft.colors.PINK),
                    ft.Text(texto_transmision, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ], alignment=ft.MainAxisAlignment.START),
                ft.Row([
                    ft.Icon(name=ft.icons.OIL_BARREL, color=ft.colors.PINK),
                    ft.Text(texto_combustible, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ], alignment=ft.MainAxisAlignment.START),
            ],  horizontal_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.CENTER),
            margin=5,
            padding=30,
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
        content=ft.Column([
            ft.Text("Agregar otro vehiculo", theme_style=ft.TextThemeStyle.TITLE_LARGE),
            ft.Icon(ft.icons.ADD_BOX_OUTLINED, size=50),
        ],  alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        margin=5,
        padding=10,
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
        cards.append(card(vehiculo[2] + " " + vehiculo[1], vehiculo[3], vehiculo[4]))
    cards.append(card_add)
    
    view = ft.Container(
            content=ft.Column(cards),
            alignment = ft.alignment.center,
            width=page.width,
        )
    
    return view