import flet as ft


class TopAppBar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.center_title = False
        self.title = ft.Text("KYLiN")

        self.build_button()

        self.actions = [
            self.home_button,
            self.project_button,
            self.about_button,
            self.hire_me_button,
        ]

    def build_button(self):
        self.home_button = ft.TextButton("Home")
        self.project_button = ft.TextButton("Project")
        self.about_button = ft.TextButton("About")

        self.hire_me_button = ft.ElevatedButton(
            "Hire Me !",
            color=ft.colors.ERROR,
        )
