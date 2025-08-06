from componets.card_componets import CardEarth
import flet as ft


class PageSea(ft.Container):

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
            src="lobster.jpeg",
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
                        spacing=0,
                        run_spacing=8,
                        # columns=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Fish fillet",
                                image_src="fish_fillet.jpeg",
                            ),
                            ft.Row(
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Wheels Fish",
                                        image_src="fish_weel.jpeg",
                                    ),
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Fish on plate",
                                        image_src="fish_on_plate.jpeg",
                                    ),
                                ],
                            ),
                            ft.Row(
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Paella\n",
                                        image_src="paella.jpeg",
                                    ),
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Garlic shrimp",
                                        image_src="garlic_shrimp.jpeg",
                                    ),
                                ],
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Grilled lobster small size",
                                image_src="lobster.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Grilled lobster big size",
                                image_src="grillet_lobster.jpeg",
                            ),
                        ],
                    ),
                ],
            ),
        )
