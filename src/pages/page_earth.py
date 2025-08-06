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
            src="pork_steak.jpeg",
            fit="cover",
            opacity=0.1,
        )
        self.content = ft.Container(
            padding=ft.padding.only(left=0, right=0, bottom=8, top=0),
            content=ft.Column(
                scroll=ft.ScrollMode.ADAPTIVE,  # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ResponsiveRow(
                        spacing=0,
                        run_spacing=8,
                        # columns=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Roasted Chicken",
                                image_src="roast_chicken.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Chicken Fajitas",
                                image_src="chicken_fajitas.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Pork Fajitas",
                                image_src="pork_fajita.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Pork Steak",
                                image_src="pork_steak.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Pork Ribs",
                                image_src="pork_costillas.jpeg",
                            ),
                        ],
                    ),
                ],
            ),
        )
