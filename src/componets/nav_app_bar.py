import flet as ft


class nav_drawer_widget(ft.NavigationDrawer):

    __slots__ = [
        "shadow_color",
        "elevation",
        "bgcolor",
        "surface_tint_color",
        "indicator_color",
    ]

    def __init__(self, page: object = None):
        super().__init__()
        self.page = page
        self.shadow_color = "black"
        self.elevation = 24
        self.bgcolor = ("surface,0.96",)
        self.surface_tint_color = "black,0.4"
        self.indicator_color = "grey,0.25"

    def build(self):
        self.controls = [
            ft.Container(
                padding=ft.padding.all(0),
                margin=ft.margin.all(0),
                # expand        = True,
                alignment=ft.alignment.center,
                height=340,
                border_radius=ft.border_radius.only(
                    top_left=16, top_right=18, bottom_left=48, bottom_right=100
                ),
                border=ft.border.all(4, ft.Colors.SURFACE),
                content=ft.Image(
                    src="guantanamera_door.png",
                    fit=ft.ImageFit.COVER,
                    opacity=0.80,
                    expand=True,
                    scale=1.2,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=22,
                    color=ft.Colors.BLACK,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                ),
            ),
            ft.Divider(thickness=0.1),
            ft.Container(
                expand=True,
                ink=False,
                bgcolor="TRANSPARENT",
                padding=ft.padding.all(8),
                margin=ft.margin.all(8),
                alignment=ft.alignment.center,
                content=ft.Text(
                    value="Guantanamera restaurant",
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                    # italic            = True,
                    size=18,
                    font_family="Consolas",  # "Consolas ,RobotoSlab
                ),
            ),
            ft.Divider(thickness=0.1),
            ft.NavigationDrawerDestination(
                label="Gallery",
                icon=ft.Icon(ft.Icons.CAMERA_OUTLINED),
                selected_icon=ft.Icons.CAMERA,
            ),
            ft.NavigationDrawerDestination(
                label="Documentation",
                icon=ft.Icons.AUTO_STORIES_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.AUTO_STORIES),
            ),
            ft.NavigationDrawerDestination(
                label="Developer",
                icon=ft.Icon(ft.Icons.CLEAN_HANDS_OUTLINED),
                selected_icon=ft.Icons.CLEAN_HANDS,
            ),
            ft.NavigationDrawerDestination(
                label="App version",
                icon=ft.Icon(ft.Icons.LOCAL_MALL_OUTLINED),
                selected_icon=ft.Icons.LOCAL_MALL,
            ),
        ]
        self.on_change = lambda e: self.handle_change(index_data=e)

    def handle_change(self, index_data):
        # MODEL OF DATA SELECTED
        # self.all_index_database = "my_doc"
        # self.tmp_index_data = index_data.data
        # self.model_data = self.dict_documentation.get(self.tmp_index_data)

        dlg_modal = ft.AlertDialog(
            # title=ft.Text(self.model_data),
            # adaptive=True,
            modal=True,
            inset_padding=ft.padding.symmetric(vertical=12, horizontal=8),
            content=ft.Column(
                scroll="HIDDEN",
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Text(
                        size=12,
                        # value=self.all_index_database(arg=self.model_data),
                        text_align=ft.TextAlign.LEFT,
                    ),
                ],
            ),
            actions=[
                ft.ElevatedButton(
                    text="Closet",
                    bgcolor="red",
                    on_click=lambda _: self.page.close(dlg_modal),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.open(dlg_modal)


class nav_app_bar(ft.AppBar):

    def __init__(
        self,
        main_page: object = object(),
        visible: bool = False,
    ):
        super().__init__()
        self.page = main_page
        self.visible = visible
        self.title = ft.Text(
            value="Restauración",
        )
        self.leading = ft.Icon(
            name=ft.Icons.COFFEE_ROUNDED,
        )
        self.center_title = False
        self.actions = [
            ft.IconButton(
                icon=ft.Icons.TABLE_ROWS_ROUNDED,
                on_click=lambda e: self.check_menu_bar(main_page=self.page),
            ),
        ]
        self.bgcolor = "TRANSPARENT"
        self.page.update()

    def check_menu_bar(self, main_page):
        main_page.open(main_page.views[0].drawer)
        main_page.update()
