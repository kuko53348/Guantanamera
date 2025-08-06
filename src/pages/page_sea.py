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
                        # columns=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Fish Fillet",
                                image_src="fish_fillet.jpeg",
                            ),
                            ft.Row(
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Fish Wheels",
                                        image_src="fish_weel.jpeg",
                                    ),
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Fish on Plate",
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
                                        body="Cuban Paella",
                                        image_src="paella.jpeg",
                                    ),
                                    CardEarth(
                                        page=self.page,
                                        header="Get Best offer now",
                                        body="Garlic Shrimp",
                                        image_src="garlic_shrimp.jpeg",
                                    ),
                                ],
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Grilled Lobster (Medium Size)",
                                image_src="lobster.jpeg",
                            ),
                            CardEarth(
                                page=self.page,
                                header="Get Best offer now",
                                body="Grilled Lobster (Big Size)",
                                image_src="grillet_lobster.jpeg",
                            ),
                        ],
                    ),
                ],
            ),
        )
