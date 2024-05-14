import flet as ft


class Index(ft.View):
    def __init__(self, page: ft.Page):
        super(Index, self).__init__(
            route="/",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.build_content()
        self.appbar = self.build_appbar()
        self.scroll = ft.ScrollMode.AUTO
        return

    def build_content(self):
        self.controls = [
            self.build_self_intro(),
            self.build_body(),
            self.build_content_me_button(),
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
            # leading=ft.Icon(ft.icons.PALETTE),
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

    def build_content_me_button(self) -> ft.Container:

        content_icon_size = 50

        self.fb_button = ft.Image(
            src="assets/bxl-facebook-circle.svg",
            width=content_icon_size,
            height=content_icon_size,
        )

        self.instagram_button = ft.Image(
            src="assets/bxl-instagram-alt.svg",
            width=content_icon_size,
            height=content_icon_size,
        )

        self.linkedin_button = ft.Image(
            src="assets/bxl-linkedin-square.svg",
            width=content_icon_size,
            height=content_icon_size,
        )

        self.github_button = ft.Image(
            src="assets/bxl-github.svg",
            width=content_icon_size,
            height=content_icon_size,
        )

        return ft.Container(
            content=ft.Row(
                controls=[
                    self.fb_button,
                    self.instagram_button,
                    self.linkedin_button,
                    self.github_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=200,
            alignment=ft.alignment.center,
        )
