import flet as ft


class TopAppBar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.center_title = False
        self.title = ft.Text("KYLiN")
        self.page = page
        self.build_button()

        self.actions = [
            self.home_button,
            self.project_button,
            self.about_button,
            self.hire_me_button,
        ]

    def build_button(self):
        self.home_button = ft.TextButton(
            "Home",
            on_click=lambda _: self.page.go("/"),
        )
        self.project_button = ft.TextButton(
            "Project",
            on_click=lambda _: self.page.go("/project"),
        )
        self.about_button = ft.TextButton(
            "About",
            on_click=lambda _: self.page.go("/about"),
        )

        self.hire_me_button = ft.ElevatedButton(
            "Hire Me !",
            color=ft.colors.ERROR,
        )
