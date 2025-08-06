import flet as ft
from flet import Offset, Tab, Alignment, BorderSide

from database.guantanamera_db import get_database


# widget class
class fletbox_ui_0(ft.Container):
    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.Colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.jpeg',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.Colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=36, top=8, right=36, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                opacity=1.0,
                shadow=[],
                visible=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    opacity=1.0,
                    spacing=5,
                    visible=True,
                    controls=[
                        ft.Text(
                            color=ft.Colors("grey200"),
                            enable_interactive_selection=True,
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=36,
                            value="Guantanamera",
                            visible=True,
                            weight=ft.FontWeight.W_900,
                        ),
                        ft.Text(
                            color=ft.Colors("grey400"),
                            enable_interactive_selection=True,
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=28,
                            value="Restaurant",
                            visible=True,
                            weight=ft.FontWeight.W_900,
                        ),
                        ft.Text(
                            text_align=ft.TextAlign.LEFT,
                            color=ft.Colors("grey600"),
                            enable_interactive_selection=True,
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=13,
                            weight=ft.FontWeight.W_600,
                            value=get_database("Guantanamera restorant"),
                            visible=True,
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_1(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.Colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.jpeg',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.Colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                opacity=1.0,
                padding=ft.Padding(left=4, top=4, right=14, bottom=4),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                on_click=lambda _: self.page.go("/first_page"),
                visible=True,
                width=220,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    expand=True,
                    opacity=1.0,
                    run_spacing=8,
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    visible=True,
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment(x=0, y=0),
                            bgcolor=ft.Colors("transparent"),
                            border_radius=ft.BorderRadius(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            ink_color=ft.Colors("yellow"),
                            opacity=1.0,
                            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                            shadow=[],
                            visible=True,
                            content=ft.Icon(
                                name="navigate_next_rounded",
                                opacity=1.0,
                                visible=True,
                            ),
                        ),
                        ft.Text(
                            color=ft.Colors("grey"),
                            enable_interactive_selection=True,
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=14,
                            value="Get Started",
                            visible=True,
                            weight="bold",
                        ),
                        ft.Icon(
                            name="double_arrow_rounded",
                            opacity=1.0,
                            visible=True,
                        ),
                    ],
                ),
            ),
        )


class PageOne(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None) -> None:
        super().__init__()
        self.image = ft.DecorationImage(
            src="guantanamera.jpeg", fit=ft.ImageFit.COVER, opacity=0.15
        )
        self.padding = ft.padding.only(left=0, right=0, bottom=64, top=64)

        self.page = page
        self.bgcolor = ft.Colors("transparent")
        self.expand = True
        self.alignment = ft.alignment.top_center

        # all widgets
        self.all_instances: list = [
            fletbox_ui_0(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_1(
                page=self.page,
                expand=False,
            ),
        ]

        # content of current widget
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
            run_spacing=0,
            controls=self.all_instances,
        )


if __name__ == "__main__":
    # Just testing MainApp

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.DARK
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window.left = 3
        page.window.top = 3
        page.padding = 0
        page.spacing = 0
        page.window.height = 720
        page.window.width = 320

        page.add(PageOne(page=page))
        page.update()

    ft.app(
        target=main,
        assets_dir="assets",
    )
