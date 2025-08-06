import flet as ft

from database.guantanamera_db import get_database


#  widget edit tag name
class CarStarter(ft.Container):

    def __init__(
        self,
        page: object = None,
        show_message: bool = False,
        header: str = "35% OFF",
        body: str = "Get Best offer now",
        image_src: str = "none.gif",
        text_size: int = 16,
        body_size: int = 22,
        card_size: int = 180,
    ) -> None:
        super().__init__()
        self.page = page

        self.expand = True
        self.bgcolor = ft.Colors("transparent")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.col = {"sm": 6, "md": 4, "xl": 2}

        self.on_click = lambda _: self.change_image_second_page(
            image_change=image_src, header=body
        )

        # content of current widget
        self.content = ft.Container(
            expand=True,
            margin=ft.margin.only(left=0, top=0, right=0, bottom=0),
            padding=ft.padding.only(left=8, top=0, right=8, bottom=0),
            border_radius=ft.border_radius.all(24),
            # width=340,
            height=card_size,
            bgcolor=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors("white")),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src=image_src,
                fit="cover",
                opacity=0.35,
            ),
            content=ft.Container(
                padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                content=ft.Column(
                    # padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                    # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                    # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        # Banner Title
                        ft.Text(
                            value=header,
                            size=text_size,
                            weight="bold",
                            color=ft.Colors("grey500"),
                        ),
                        # Description
                        ft.Container(
                            # expand=True,
                            margin=ft.margin.only(left=0, top=0, right=0, bottom=0),
                            # padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                            # border_radius=ft.border_radius.all(18),
                            ink_color=ft.Colors("yellow"),
                            alignment=ft.alignment.center_left,
                            # width=100,
                            # height=20,
                            # bgcolor=ft.Colors("white54"),
                            content=ft.Text(
                                value=body,
                                size=body_size,
                                weight=ft.FontWeight.W_900,
                                color=ft.Colors("grey300"),
                            ),
                        ),
                        ft.Container(
                            visible=True if show_message else False,
                            expand=True,
                            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                            border_radius=ft.border_radius.all(18),
                            ink_color=ft.Colors("yellow"),
                            alignment=ft.alignment.center,
                            width=100,
                            bgcolor=ft.Colors("white54"),
                            content=ft.Text(
                                value="Details",
                                size=16,
                                weight="bold",
                                color=ft.Colors("grey900"),
                            ),
                        ),
                    ],
                ),
            ),
        )

    def change_image_second_page(self, image_change: str = "", header: str = ""):
        self.page.session.set("header_text", header)
        self.page.session.set("description_text", get_database(index=header))
        self.page.session.set("current_image", image_change)
        self.page.go("/second_page")


#  widget edit tag name
class CardEarth(ft.Container):

    def __init__(
        self,
        page: object = None,
        header: str = "World Famous Brands",
        body: str = "More Than 45 Brands",
        image_src: str = "none.gif",
        text_size: int = 16,
        body_size: int = 22,
        card_size: int = 150,
    ) -> None:
        super().__init__()
        self.page = page

        self.expand = True
        self.bgcolor = ft.Colors("transparent")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.col = {"sm": 6, "md": 4, "xl": 2}

        self.on_click = lambda _: self.change_image_second_page(
            image_change=image_src, header=body
        )

        # content of current widget
        self.content = ft.Container(
            # padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            margin=ft.margin.only(left=4, top=0, right=4, bottom=0),
            content=ft.Container(
                width=340,
                height=card_size,
                border_radius=ft.border_radius.all(32),
                padding=ft.padding.all(20),
                bgcolor=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors("white")),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black"),
                    offset=ft.Offset(0, 5),
                ),
                image=ft.DecorationImage(
                    src=image_src,
                    fit="cover",
                    opacity=0.3,
                ),
                content=ft.Column(
                    # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                    # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                    spacing=4,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        # Brand Name
                        ft.Text(
                            value=header,
                            size=16,
                            weight="bold",
                            color=ft.Colors("grey400"),
                        ),
                        # Description
                        ft.Text(
                            value=body,
                            size=24,
                            weight=ft.FontWeight.W_900,
                            color=ft.Colors("grey200"),
                        ),
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                            border_radius=ft.border_radius.all(18),
                            ink_color=ft.Colors("yellow"),
                            alignment=ft.alignment.center,
                            width=100,
                            bgcolor=ft.Colors("white54"),
                            content=ft.Text(
                                value="Details",
                                size=16,
                                weight="bold",
                                color=ft.Colors("grey900"),
                            ),
                        ),
                    ],
                ),
            ),
        )

    def change_image_second_page(self, image_change: str = "", header: str = ""):
        self.page.session.set("header_text", header)
        self.page.session.set("description_text", get_database(index=header))
        self.page.session.set("current_image", image_change)
        self.page.go("/second_page")


#  widget edit tag name
class CardCombinade(ft.Container):

    def __init__(
        self,
        page: object = None,
        header: str = "Global Hotel",
        body: str = "More Than 45 Brands",
        extra: str = "More Than 45 Brands",
        image_src: str = "none.gif",
    ) -> None:
        super().__init__()
        # self.expand = True
        self.bgcolor = ft.Colors("transparent")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.col = {"sm": 6, "md": 4, "xl": 2}
        self.width = 340

        self.on_click = lambda _: self.change_image_second_page(
            image_change=image_src, header=header
        )

        # content of current widget
        self.content = ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.only(left=12, top=0, right=12, bottom=0),
            border_radius=ft.border_radius.all(32),
            width=340,
            # height=150,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src=image_src,
                fit=ft.ImageFit.FILL,
                opacity=0.1,
            ),
            content=ft.Row(
                width=320,
                # expand=True,
                controls=[
                    ft.Image(
                        src=image_src,
                        width=140,
                        height=140,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        # horizontal_alignment=ft.CrossAxisAlignment.START,
                        # run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                            ft.Column(
                                spacing=8,
                                run_spacing=8,
                                # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        value=header,
                                        size=18,
                                        weight=ft.FontWeight.W_900,
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Text(
                                        value=body,
                                        size=11,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                            ),
                            ft.Container(
                                width=240,
                                padding=ft.padding.only(
                                    left=8, top=8, right=8, bottom=8
                                ),
                                margin=ft.margin.only(left=8, top=8, right=8, bottom=8),
                                border_radius=ft.border_radius.all(18),
                                ink_color=ft.Colors("yellow"),
                                alignment=ft.alignment.center,
                                # width=100,
                                bgcolor=ft.Colors.with_opacity(
                                    opacity=0.2, color=ft.Colors("white")
                                ),
                                content=ft.Text(
                                    value=extra,
                                    size=16,
                                    weight=ft.FontWeight.W_900,
                                    color=ft.Colors("grey200"),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

    def change_image_second_page(self, image_change: str = "", header: str = ""):
        self.page.session.set("header_text", header)
        self.page.session.set("description_text", get_database(index=header))
        self.page.session.set("current_image", image_change)
        self.page.go("/second_page")
