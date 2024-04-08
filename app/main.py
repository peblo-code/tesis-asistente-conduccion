import flet as ft
from sections.formVehicle import formVehicle
from sections.dashboard import dashboard
from sections.vehicleList import vehicleList
from home import home
from database import AutomovilesDatabase

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Crear instancia de la base de datos
    db = AutomovilesDatabase("automoviles.db")

    # Crear tablas
    db.create_tables()

    userExistence = db.verify_user()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Text("Inicio", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),
                    home(page),
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        if page.route == "/formVehicle":
            page.views.append(
                ft.View(
                    "/formVehicle",
                    formVehicle(page)
                )
            )
        if page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        dashboard(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        if page.route == "/vehicleList":
            page.views.append(
                ft.View(
                    "/vehicleList",
                    [
                        vehicleList(page)
                    ],
                scroll=ft.ScrollMode.ALWAYS
                )
            )
        page.update()

    if not userExistence:
        page.go("/formVehicle")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.FLET_APP)