from componets.card_componets import CardEarth
import flet as ft


class PageEarth(ft.Container):

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
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Roasted chicken",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Chicken fajitas",
                                image_src="chiken.png",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Pork fajitas",
                                image_src="chiken.png",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Pork steak",
                                image_src="steak.png",
                            ),
                        ],
                    ),
                ],
            ),
        )
