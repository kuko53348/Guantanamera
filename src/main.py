import flet as ft  # type: ignore

from componets.nav_app_bar import RichText, nav_app_bar, nav_drawer_widget
from database.guantanamera_db import get_database
from pages.page_combinate import PageCombinate
from pages.page_earth import PageEarth
from pages.page_one import PageOne
from pages.page_review import ImageReview
from pages.page_sea import PageSea
from pages.page_starters import PageStarters


class page_app_view(ft.View):
    """'
    ## Create frame view
    ```python
    >>> current_view = page_app_view(
    >>>                page = self.page,
    >>>                route = self.route,
    >>>                content = ft.ElevatedButton(
    >>>                    text = 'Home',
    >>>                    on_click = lambda _: self.page.go('/'),
    >>> ))
    ```
    """

    def __init__(
        self,
        page: object = None,
        route: str = str(),
        content: object = None,
        index_page: int = None,
        show_navigation: bool = False,
    ) -> None:
        super().__init__()
        self.page = page
        self.route = route
        # self.padding = 0
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=8)

        self.content = content
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.index_pages_dict: dict = {
            0: PageStarters(page=self.page),
            1: PageEarth(page=self.page),
            2: PageSea(page=self.page),
            3: PageCombinate(page=self.page),
        }
        self.controls: list = [
            (
                self.index_pages_dict.get(index_page)
                if not index_page == None
                else content
            ),
        ]

        if show_navigation:
            # self.appbar = ft.AppBar(
            #     title=ft.Text("Bottom AppBar Demo"),
            #     center_title=True,
            #     bgcolor=ft.Colors("grey900"),
            #     automatically_imply_leading=False,
            # )

            # self.floating_action_button_location = (
            #     ft.FloatingActionButtonLocation.MINI_END_TOP
            # )
            self.drawer = nav_drawer_widget(page=self.page)
            self.floating_action_button = ft.FloatingActionButton(
                icon=ft.Icons.QR_CODE_SCANNER_OUTLINED,
                bgcolor=ft.Colors("grey900"),
                mini=True,
                foreground_color=ft.Colors.AMBER_100,
                disabled_elevation=True,
                focus_elevation=0,
                on_click=lambda _: self.open_drawer(),
            )

            self.navigation_bar = ft.NavigationBar(
                selected_index=index_page,
                bgcolor=ft.Colors("grey900"),
                # offset=(0, -0.05),
                height=60,
                on_change=lambda _: self.change_screens(index_page=_.control),
                elevation=32,
                destinations=[
                    ft.NavigationBarDestination(
                        label="Starters",
                        icon=ft.Icons.FASTFOOD_OUTLINED,
                        selected_icon=ft.Icons.FASTFOOD_ROUNDED,
                    ),
                    ft.NavigationBarDestination(
                        label="Earth",
                        icon=ft.Icons.LANDSCAPE_OUTLINED,
                        selected_icon=ft.Icons.LANDSCAPE_ROUNDED,
                    ),
                    ft.NavigationBarDestination(
                        label="Sea",
                        icon=ft.Icons.WATER_OUTLINED,
                        selected_icon=ft.Icons.WATER_ROUNDED,
                    ),
                    ft.NavigationBarDestination(
                        label="Combinate",
                        icon=ft.Icons.FOOD_BANK_OUTLINED,
                        selected_icon=ft.Icons.FOOD_BANK_ROUNDED,
                    ),
                ],
            )
            self.appbar = nav_app_bar(
                page=self.page,
                visible=True,
                bgcolor=ft.Colors("grey900"),
                icon_left="restaurant_menu_rounded",
                icon_right="table_rows_rounded",
                title="Guantanamera",
                menu_drawer=self.drawer,
            )

    def open_drawer(self, drawer: object = None):
        dlg_modal = ft.AlertDialog(
            title=ft.Text(
                value="We are in Instagram",
                size=26,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            # adaptive=True,
            modal=True,
            inset_padding=ft.padding.symmetric(vertical=8, horizontal=0),
            content=ft.Container(
                border_radius=ft.border_radius.only(
                    top_left=24,
                    top_right=24,
                    bottom_left=24,
                    bottom_right=24,
                ),
                height=280,
                image=ft.DecorationImage(
                    src="qr_code.jpeg",
                    fit=ft.ImageFit.COVER,
                    # opacity=0.02,
                ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                alignment=ft.alignment.center,
                ink_color=ft.Colors("yellow"),
                bgcolor=ft.Colors("black12"),
            ),
            actions=[
                RichText(
                    page=self.page,
                    icon="monochrome_photos_rounded",
                    text="OPEN INSTAGRAM",
                    text_link="https://www.instagram.com/guantanamera397?igsh=YzljYTk1ODg3Zg==",
                ),
                ft.Container(height=8),
                RichText(
                    page=self.page,
                    icon="cloud_download_rounded",
                    text="DOWNLOAD APK",
                    text_link="https://drive.google.com/drive/folders/1S9IjowvYYxMH6BZPTiVlEHvhspfRCT-p",
                ),
                ft.ElevatedButton(
                    text="Closet",
                    bgcolor="red",
                    on_click=lambda _: self.page.close(dlg_modal),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.open(dlg_modal)

    def change_screens(self, index_page: int = None):
        dynamic_index: int = index_page.selected_index
        self.page.session.set("current_idex", dynamic_index)

        self.controls = [
            self.index_pages_dict.get(dynamic_index),
        ]
        self.update()


class flet_box_app:

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.left = 3
        self.page.window.top = 3
        self.page.padding = 0
        self.page.spacing = 0
        # self.page.window.height = 720
        # self.page.window.width = 340
        self.page.on_route_change = lambda _: self.on_route_change(
            page=self.page,
            route="/",
        )

        self.page.session.set("current_idex", 0)
        self.page.session.set(
            "header_text",
            "Exemple",
        )
        self.page.session.set(
            "body_text",
            "with this app you can try different types of activities and choose what the most enjoyable for you",
        )

        self.page.go("/")
        # self.page.go("/first_page")
        # self.page.go("/second_page")

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == "/":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=PageOne(page=self.page),
                    show_navigation=False,
                )
            )
        if self.page.route == "/first_page":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=PageStarters(page=self.page),
                    index_page=self.page.session.get("current_idex"),
                    show_navigation=True,
                )
            )

        if self.page.route == "/second_page":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=ImageReview(page=self.page),
                )
            )

        self.page.update()


if __name__ == "__main__":
    ft.app(
        target=flet_box_app,
        assets_dir="assets",
        # name = 'Flet-Box',
        # route_url_strategy = 'assets/project_assets/',
        # use_color_emoji = True,
        # web_renderer = ft.WebRenderer.CANVAS_KIT,
        # port = 8081,
    )
