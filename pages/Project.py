import flet as ft
from components import TopAppBar


class Project(ft.View):
    def __init__(self, page: ft.Page):
        super(Project, self).__init__(
            route="/project",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page = page
        self.build_content()
        self.appbar = TopAppBar(self.page)
        return

    def build_content(self):
        self.controls = []
