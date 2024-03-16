import flet as ft
from sections.formVehicle import formVehicle
from sections.menu import menu
from database import AutomovilesDatabase

def main(page: ft.Page):
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
                    menu(page)
                ],
            )
        )
        if page.route == "/formVehicle":
            page.views.append(
                ft.View(
                    "/formVehicle",
                    formVehicle(page),
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