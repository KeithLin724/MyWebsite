import flet as ft


class Project(ft.View):
    def __init__(self, page: ft.Page):
        super(Project, self).__init__(
            route="/project",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page = page
        self.build_content()
        return

    def build_content(self):
        self.controls = []
