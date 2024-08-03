import flet as ft
from configs.settings import settings
from utils.Strings import strings
from controls.controls import (
    Text,
    TextField,
    SnackBar,
    clicked,
    InconButton,
    Divider
)

def home(page: ft.Page, width: int, height: int):

    view = ft.View(
        route='/',
        bgcolor=settings['bgcolor'],

        controls=[
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={'xs': 12, 'sm': 12, 'md': 5},
                        height= height * 0.35,
                        bgcolor=ft.colors.WHITE,
                        image_src='./assets/foto.png',
                        on_click=lambda e: clicked(page, e),
                        padding=ft.padding.only(
                            top=10,
                            left=8,
                            right=8,
                            bottom=8
                        ),
                        border_radius=ft.border_radius.only(
                            top_right=20,
                            bottom_left=20
                        ),

                        content=ft.Column(
                            controls=[
                                Text(
                                    value=list(strings.keys())[0].upper(),
                                    size=22,
                                    color=ft.colors.BLACK
                                ),
                                Divider(),
                                Text(
                                    value=strings[list(strings.keys())[0]],
                                    size=15,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                InconButton(
                                    icon=ft.icons.ARROW_RIGHT,
                                    tooltip='Login',
                                    size=30,
                                    on_click=lambda e: page.go('/login')
                                )
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                        
                    )
                ],
                width=width,
                height=height,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )

    return view