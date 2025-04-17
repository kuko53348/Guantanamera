from componets.card_componets import CarStarter
import flet as ft


class PageStarters(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("transparent")
        self.ink_color = ft.Colors("yellow")
        self.image = ft.DecorationImage(
            src="login.jpg",
            fit="cover",
            opacity=0.1,
        )
        self.content = ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.ADAPTIVE,  # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ResponsiveRow(
                        # columns=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Consume",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Bannana Chips",
                                image_src="chips.png",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Sauteed vegetables",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Boiled food",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Cold salad",
                                image_src="coldsalad.png",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Garlic shrimp",
                                image_src="shrimp.png",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Perlan fish",
                                image_src="perlan.png",
                            ),
                        ],
                    ),
                ],
            ),
        )
        # self.page.
