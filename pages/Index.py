import flet as ft


class Index(ft.View):
    def __init__(self, page: ft.Page):
        super(Index, self).__init__(
            route="/",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.build_content()
        self.appbar = self.build_appbar()

        return

    def build_content(self):
        self.controls = [
            self.build_self_intro(),
            self.build_body(),
        ]

    def build_appbar(self) -> ft.AppBar:

        self.home_button = ft.TextButton("Home")
        self.project_button = ft.TextButton("Project")
        self.about_button = ft.TextButton("About")

        self.hire_me_button = ft.ElevatedButton(
            "Hire Me !",
            color=ft.colors.ERROR,
        )

        return ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            center_title=False,
            title=ft.Text("KYLiN"),
            actions=[
                self.home_button,
                self.project_button,
                self.about_button,
                self.hire_me_button,
            ],
        )

    def intro_text(self) -> ft.Column:
        return ft.Column(
            controls=[
                ft.Text(
                    "My Name is ",
                    theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
                ),
                ft.Text(
                    "KYLiN",
                    theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def intro_image(self) -> ft.Image:
        return ft.Image(
            src="https://avatars.githubusercontent.com/u/38067890?v=4",
            width=350,
            height=350,
            border_radius=300,
        )

    def build_self_intro(self) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    # text
                    self.intro_text(),
                    # image
                    self.intro_image(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=500,
            # bgcolor=ft.colors.ERROR,
            alignment=ft.alignment.center,
        )

    def build_body(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "I'm a Data Analysis Sciences",
                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=200,
            alignment=ft.alignment.center,
        )
