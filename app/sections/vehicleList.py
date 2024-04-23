import flet as ft
from database import AutomovilesDatabase

def vehicleList(page: ft.Page):
    page.title = "Mis vehiculos"
    page.scroll = "adaptive"

    db = AutomovilesDatabase("automoviles.db")
    vehicle_selected = db.get_vehicle_selected()

    def card(car_id, car_name, transmision, combustible):
        texto_transmision = "Automático"
        texto_combustible = "Nafta"
        if transmision == "1":
            texto_transmision = "Manual"
        if combustible == "1":
            texto_combustible = "Diésel"

        car_selected = db.obtener_vehiculo_por_id(car_id)

        def edit_clicked(e,display_view, display_edit):
            if(display_view.visible):
                display_view.visible = False
                display_edit.visible = True
            else:
                button_clicked(e)
                display_view.visible = True
                display_edit.visible = False
            page.update()

        def update_vehicle_selected(e, vehiculo_id):
            db.set_vehicle_selected(str(vehiculo_id))
            page.go("/")
        
        def button_clicked(e):
            db.editar_vehiculo_por_id(car_id, modelo_dropdown.value, transmision_dropdown.value, combustible_dropdown.value)
            cargar_vehiculos()
            page.update()

        car_name_text = car_name
        if car_id == vehicle_selected:
            car_name_text += " (seleccionado)"
        display_view = ft.Row([
            ft.Column([
                ft.Text(car_name_text, theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Row([
                    ft.Icon(name=ft.icons.CAR_CRASH_SHARP, color=ft.colors.PINK),
                    ft.Text(texto_transmision, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ], alignment=ft.MainAxisAlignment.START),
                ft.Row([
                    ft.Icon(name=ft.icons.OIL_BARREL, color=ft.colors.PINK),
                    ft.Text(texto_combustible, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ], alignment=ft.MainAxisAlignment.START),

            ],  horizontal_alignment=ft.CrossAxisAlignment.START, alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.Container(
                    content=ft.Icon(name=ft.icons.EDIT),
                    bgcolor=ft.colors.DEEP_PURPLE_ACCENT_700,
                    width=50,
                    height=50,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: edit_clicked(e, display_view, display_edit)
                ),
                ft.Container(
                    content=ft.Icon(name=ft.icons.CHECK_BOX),
                    bgcolor=ft.colors.DEEP_PURPLE_ACCENT_700,
                    width=50,
                    height=50,
                    border_radius=10,
                    ink=True,
                    visible=not (car_id == vehicle_selected),
                    on_click=lambda e: update_vehicle_selected(e, car_id)
                )
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        def cargar_modelos(e):
            marca_seleccionada = marca_dropdown.value
            modelos = db.get_modelos_por_marca(marca_seleccionada)
            modelo_dropdown.options = [ft.dropdown.Option(key=id_modelo, text=modelo) for id_modelo, modelo in modelos]
            page.update()

        marca_dropdown = ft.Dropdown(
            on_change=cargar_modelos,
            on_focus=cargar_modelos,
            width="100%",
            label="Marca",
            autofocus=True,
            options=[ft.dropdown.Option(text=marca, key=id_marca) for id_marca, marca in db.get_marcas()],
            value=car_selected[4]
        )
        modelo_dropdown = ft.Dropdown(
            width="100%",
            label="Modelo",
            options=[],
            value=car_selected[1]
        )

        transmision_dropdown = ft.Dropdown(
            width="100%",
            label="Transmisión",
            options=[
                ft.dropdown.Option(key=0, text="Automático"),
                ft.dropdown.Option(key=1, text="Manual"),
            ],
            value=int(car_selected[2])
        )
        combustible_dropdown = ft.Dropdown(
            width="100%",
            label="Combustible",
            options=[
                ft.dropdown.Option(key=0, text="Nafta"),
                ft.dropdown.Option(key=1, text="Diesel"),
            ],
            value=int(car_selected[3])
        )
        display_edit = ft.Row([
            ft.Column([
                marca_dropdown, 
                modelo_dropdown, 
                transmision_dropdown, 
                combustible_dropdown,
            ]),

            ft.Container(
                content=ft.Icon(name=ft.icons.CHECK),
                bgcolor=ft.colors.DEEP_ORANGE_900,
                width=50,
                height=50,
                border_radius=10,
                ink=True,
                on_click=lambda e: edit_clicked(e,display_view, display_edit)
            )
        ], visible=False, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        return ft.Container(
            content=ft.Column(controls=[display_view, display_edit]),
            margin=5,
            padding=30,
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            bgcolor=ft.colors.SURFACE_VARIANT,
            width=(page.width)/2,
            border_radius=10,
            alignment=ft.alignment.center
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
        on_click=lambda e: page.go("/formVehicle")
    )

    cards=[]

    def cargar_vehiculos():
        cards.clear()
        vehiculos = db.obtener_vehiculos_registrados()
        for vehiculo in vehiculos:
            cards.append(card(vehiculo[0], vehiculo[2] + " " + vehiculo[1], vehiculo[3], vehiculo[4]))
        cards.append(card_add)
    cargar_vehiculos()
    
    view = ft.Column([
            ft.Container(
                content=ft.Icon(name=ft.icons.ARROW_BACK, size=50),
                on_click=lambda e: page.go("/home")
            ),
            ft.Container(
                content=ft.Column(cards),
                alignment = ft.alignment.center,
                width=page.width,
            )
        ])
    
    return view