import flet as ft

from components import ContentButton, DisplaySvg


class Index(ft.View):
    def __init__(self, page: ft.Page):
        super(Index, self).__init__(
            route="/",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page = page

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

        launch_url = lambda url: (lambda _: self.page.launch_url(url))

        self.fb_button = ContentButton(
            src=DisplaySvg.FACEBOOK,
            tooltip="Facebook",
            on_click=launch_url(
                url="https://www.facebook.com/profile.php?id=100009109213789&mibextid=2JQ9oc"
            ),
        )

        self.instagram_button = ContentButton(
            src=DisplaySvg.INSTAGRAM,
            tooltip="Instagram",
            on_click=launch_url(
                url="https://www.instagram.com/lin.keith.24?igsh=MXR3b2dwcXVoZHd5dA=="
            ),
        )

        self.linkedin_button = ContentButton(
            src=DisplaySvg.LINKEDIN,
            tooltip="LinkedIn",
            on_click=launch_url(
                url="https://www.linkedin.com/in/keith-lin-23a423293?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
            ),
        )

        self.github_button = ContentButton(
            src=DisplaySvg.GITHUB,
            tooltip="Github",
            on_click=launch_url(url="https://github.com/KeithLin724"),
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
