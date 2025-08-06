from componets.card_componets import CarStarter
import flet as ft


class PageStarters(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(left=8, right=8, bottom=0, top=0)
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("transparent")
        self.ink_color = ft.Colors("yellow")
        self.image = ft.DecorationImage(
            src="camarones.jpeg",
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
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                # show_message=True,
                                header="Get Best offer now",
                                body="Cuban Tamals",
                                image_src="tamales.jpeg",
                                text_size=24,
                                card_size=140,
                                body_size=50,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Cold Salad",
                                image_src="cold_salad_coctail.jpeg",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Shrimp Cocktail",
                                image_src="cold_salad.jpeg",
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Tuna Cocktail",
                                image_src="atun_cold_salad.jpeg",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Chicken Cocktail",
                                image_src="chiken_salad.jpeg",
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Fried Potatoes",
                                image_src="fried_potatoes.jpeg",
                                text_size=12,
                                body_size=16,
                                card_size=125,
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Perlan",
                                image_src="perlan.jpeg",
                                text_size=12,
                                body_size=16,
                                card_size=125,
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Banana Chips",
                                image_src="banana_chips.jpeg",
                                text_size=12,
                                body_size=16,
                                card_size=125,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Garlic Shrimp",
                                image_src="camarones.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Shrimp coctail ",
                                image_src="cocktel_camarones.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Tostones",
                                image_src="tostones.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Tuna Tostones ",
                                image_src="tostones_atun.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Vegetable Salad",
                                image_src="ensalada_vegetales.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Fruit Salad",
                                image_src="ensalada_frutas.jpeg",
                                body_size=18,
                                card_size=125,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                show_message=True,
                                header="Get Best offer now",
                                body="Pork Fajita",
                                image_src="pork_fajita_picadera.jpeg",
                                text_size=24,
                                card_size=140,
                                body_size=50,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Croquettes on Plate",
                                image_src="croquetas.jpeg",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Boiled Food",
                                image_src="salted_salad.jpeg",
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Hamburger with Cheese",
                                image_src="hamburger.jpeg",
                            ),
                            CarStarter(
                                page=self.page,
                                header="Get Best offer now",
                                body="Ham slices",
                                image_src="jam.jpeg",
                            ),
                        ],
                    ),
                ],
            ),
        )
