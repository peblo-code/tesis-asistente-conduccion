import flet as ft

def home(page: ft.Page):
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def card(card_text):
        return ft.Container(
            content=ft.Text(card_text),
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
            on_click=lambda e: print("Clickable with Ink clicked!"),
        )

    page.add(
        ft.Container(
            content = ft.Column([
                ft.Row([
                    card("Conducir"),
                    card("Logs")
                ]),
                ft.Row([
                    card("Vehiculos"),
                    card("Ajustes")
                ])
            ]),
            alignment = ft.alignment.center,
            width=page.width
        ),
        
    )



ft.app(target=home)