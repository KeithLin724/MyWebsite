import flet as ft


class Index(ft.View):
    def __init__(self, page: ft.Page):
        super(Index, self).__init__(
            route="/",
            
        )
        self.controls = [
            ft.Text("Hello world"),
        ]
        return
