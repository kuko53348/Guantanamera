from componets.card_componets import CardCombinade
import flet as ft


class PageCombinate(ft.Container):

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
            src="paella.png",
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
                            CardCombinade(
                                page=self.page,
                                header="Cuban paella",
                                body="All in one plate: Lobster,Mushroom,Calamar,Octupus",
                                extra="All in one plate",
                                image_src="paella_one.png",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Cuban mixed",
                                body="This combo have a special mixed and flavors",
                                extra="Chiken / Pork",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Sea and land Chiken",
                                body="This combo have a special mixed and flavors",
                                extra="Fish / Chiken",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Sea and land Pork",
                                body="This combo have a special mixed and flavors",
                                extra="Fish / Pork",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Sea mixed",
                                body="This combo have a special mixed and flavors",
                                extra="Lobster / Fish",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Guantanamera",
                                body="This combo have a special mixed and flavors",
                                extra="Lobster / Chiken / Pork",
                            ),
                            CardCombinade(
                                page=self.page,
                                header="Special combo",
                                body="This combo have a special mixed and flavors",
                                extra="Lobster / Shrimp / Pork",
                                image_src="lobstershrimp.png",
                            ),
                        ],
                    ),
                ],
            ),
        )
