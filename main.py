import flet as ft
import pages as pg

page_dict = {
    "/": pg.Index,
}


def main(page: ft.Page):
    page.title = "My Website"

    def router(router) -> None:
        page.views.clear()
        page.views.append(page_dict[page.route](page))
        page.update()

    page.on_route_change = router
    page.go("/")

    return


if __name__ == "__main__":
    ft.app(target=main, assets_dir="./assets")
