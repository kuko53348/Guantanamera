import flet as ft


class ImageReview(ft.Container):

    def __init__(
        self,
        page: object = None,
        header: str = "Global Hotel",
        body: str = "More Than 45 Brands",
        extra: str = "More Than 45 Brands",
    ) -> None:
        super().__init__()
        self.page = page

        self.expand = True
        self.image_page = self.page.session.get("current_image")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=8, right=8, bottom=12, top=12)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.image = ft.DecorationImage(
            src=self.image_page,
            fit=ft.ImageFit.COVER,
            opacity=0.1,
        )
        # content of current widget
        self.content = ft.Container(
            blur=(16, 19),
            width=720,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        expand=True,
                        # card_music_festival
                        # width=640,
                        # height=280,
                        border_radius=ft.border_radius.only(
                            top_left=18,
                            top_right=18,
                            bottom_left=0,
                            bottom_right=0,
                        ),
                        padding=ft.padding.all(0),
                        image=ft.DecorationImage(
                            src=self.image_page,
                            fit=ft.ImageFit.COVER,
                            opacity=0.8,
                        ),
                        content=ft.Column(
                            # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                            # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    blur=(16, 12),
                                    padding=ft.padding.only(
                                        left=12, right=12, bottom=12, top=12
                                    ),
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        controls=[
                                            # Banner Title
                                            ft.Text(
                                                value=self.page.session.get(
                                                    "header_text"
                                                ),
                                                size=18,
                                                weight="bold",
                                                color=ft.Colors("white"),
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Container(
                                                        width=100,
                                                        padding=ft.padding.only(
                                                            left=8,
                                                            top=8,
                                                            right=8,
                                                            bottom=8,
                                                        ),
                                                        border_radius=ft.border_radius.all(
                                                            24
                                                        ),
                                                        expand=True,
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.START,
                                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                            run_alignment=ft.CrossAxisAlignment.CENTER,
                                                            spacing=6,
                                                            run_spacing=8,
                                                            controls=[
                                                                ft.Icon(
                                                                    name="star_rounded",
                                                                    size=12,
                                                                ),
                                                                ft.Icon(
                                                                    name="star_rounded",
                                                                    size=12,
                                                                ),
                                                                ft.Icon(
                                                                    name="star_rounded",
                                                                    size=12,
                                                                ),
                                                                ft.Icon(
                                                                    name="star_rounded",
                                                                    size=12,
                                                                ),
                                                                ft.Icon(
                                                                    name="star_rounded",
                                                                    size=12,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    ft.Container(
                                                        #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                        # tooltip = 'Container',
                                                        padding=ft.padding.only(
                                                            left=8,
                                                            right=8,
                                                            bottom=8,
                                                            top=8,
                                                        ),
                                                        border_radius=ft.border_radius.only(
                                                            top_left=32,
                                                            top_right=32,
                                                            bottom_left=32,
                                                            bottom_right=32,
                                                        ),
                                                        alignment=ft.alignment.center,
                                                        ink_color=ft.Colors("yellow"),
                                                        bgcolor=ft.Colors("white12"),
                                                        content=ft.Icon(
                                                            name="favorite"
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ],
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.END,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        # width=320,
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                        border_radius=ft.border_radius.only(
                            top_left=0,
                            top_right=0,
                            bottom_left=24,
                            bottom_right=24,
                        ),
                        blur=(16, 19),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.Colors("transparent"),
                                ft.Colors("white12"),
                            ],
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            # expand=True,
                            spacing=16,
                            run_spacing=16,
                            controls=[
                                # Banner Title
                                ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    value="Description",
                                    size=26,
                                    weight=ft.FontWeight.W_900,
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    value=self.page.session.get("description_text"),
                                    weight=ft.FontWeight.W_600,
                                    size=16,
                                    color=ft.Colors("grey600"),
                                ),
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=18,
                                        top_right=18,
                                        bottom_left=18,
                                        bottom_right=18,
                                    ),
                                    alignment=ft.alignment.center,
                                    ink_color=ft.Colors("yellow"),
                                    expand=True,
                                    # blur=(18, 18),
                                    bgcolor=ft.Colors("white12"),
                                    content=ft.Text(value="Back"),
                                    on_click=lambda _: self.page.go("/first_page"),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


class fletbox_ui(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None) -> None:
        super().__init__()
        self.page = page
        self.bgcolor = ft.Colors("transparent")
        self.expand = True
        self.alignment = ft.alignment.top_center

        # all widgets
        self.all_instances: list = [
            ImageReview(
                page=self.page,
            ),
        ]

        # content of current widget
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
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

        page.add(fletbox_ui(page=page))
        page.update()

    ft.app(
        target=main,
        assets_dir="assets",
    )
