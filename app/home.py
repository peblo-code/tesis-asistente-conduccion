import flet as ft

def home(page: ft.Page):
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def card(card_text, icon_name):
        return ft.Container(
            content=ft.Column([
                ft.Text(card_text, theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Icon(name=icon_name, color=ft.colors.GREY_400, size=100),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=5,
            padding=10,
            alignment=ft.alignment.center,
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            bgcolor=ft.colors.SURFACE_VARIANT,
            width=(page.width/2)-25,
            height=page.height/3,
            border_radius=10,
            ink=True,
            on_click=lambda e: page.go("/dashboard"),
        )
    
    view = ft.Container(
            content = ft.Column([
                ft.Row([
                    card("Conducir", ft.icons.PLAY_ARROW),
                    card("Logs", ft.icons.NOTES)
                ]),
                ft.Row([
                    card("Vehiculos", ft.icons.DRIVE_ETA),
                    card("Ajustes", ft.icons.SETTINGS)
                ])
            ]),
            alignment = ft.alignment.center,
            width=page.width
        )

    return view
