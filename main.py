import flet as ft
from app.sections.formVehicle import formVehicle
from app.sections.dashboard import dashboard
from app.sections.vehicleList import vehicleList
from app.home import home
from app.database import AutomovilesDatabase
import time

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
                    [
                        formVehicle(page)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        if page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        dashboard(page)
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
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