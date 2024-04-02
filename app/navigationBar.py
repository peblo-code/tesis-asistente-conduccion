import flet as ft
from sections.menu import menu

def main(page:ft.Page):
	page.update()
	def changetab(e):
	# GET INDEX TAB
		my_index = e.control.selected_index
		tab_1.visible = True if my_index == 0 else False
		tab_2.visible = True if my_index == 1 else False
		tab_3.visible = True if my_index == 2 else False
		page.update()
 
 
	page.navigation_bar = ft.NavigationBar(
        bgcolor="blue",
        on_change=changetab,
        selected_index = 0,
        destinations = [
            ft.NavigationDestination(icon="home"),
            ft.NavigationDestination(icon="explore"),
            ft.NavigationDestination(icon="settings"),
        ]
	)
 
	tab_1 = ft.Text("Tab 1",size=30,visible=True)
	tab_2 = ft.Text("Tab 2",size=30,visible=False)
	tab_3 = ft.Text("Tab 3",size=30,visible=False)

	page.add(
		ft.Container(
		margin = ft.margin.only(
		top=page.window_height/2,
		left=50

			),
			content=ft.Column([
				ft.Container(menu(page)),
				tab_2,
				tab_3
			])
		)
	)
 
ft.app(target=main)