import flet as ft
from configs.settings import settings
from utils.Strings import strings
from connections.usuarios import(
    db,
    ver_dados
)
from Toast import toast_flet
from controls.controls import (
    Text,
    TextField,
    clicked,
    Divider
)
user: list = []

def login(page: ft.Page, width: int, height: int):

    textfields = {
        'hint_text': ['Username', 'Password'],
        'icon': [ft.icons.PERSON, ft.icons.KEY],
        'password': [False, True],
        'autofocus': [True, False]
    }

    ft.Stack()
    view = ft.View(
        route='/login',
        bgcolor=settings[list(settings.keys())[0]],

        controls=[
            ft.Stack(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={'xs': 11, 'sm': 11, 'md': 3.5},
                                height=height * 0.48,
                                bgcolor=ft.colors.WHITE,
                                padding=ft.padding.only(
                                    top=10,
                                    left=8,
                                    right=8,
                                    bottom=8
                                ),
                                border_radius=10,

                                content=ft.Column(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                Text(
                                                    value=list(strings.keys())[2].upper(),
                                                    size=14,
                                                    color=ft.colors.BLACK,
                                                    text_align='center'
                                                ),
                                                Text(
                                                    value=strings[list(strings.keys())[2]],
                                                    size=11,
                                                    color=ft.colors.with_opacity(0.8, 'black'),
                                                    text_align='center'
                                                ),
                                            ],
                                            width=width,
                                            spacing=1,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                        ),
                                        Divider(),
                                        ft.ResponsiveRow(
                                            controls=[
                                                user_textfields := ft.Column(
                                                    controls=[
                                                        TextField(
                                                            hint_text=textfields['hint_text'][i],
                                                            prefix_icon=textfields['icon'][i],
                                                            autofocus=textfields['autofocus'][i],
                                                            password=textfields['password'][i],
                                                            size=13,
                                                            color=ft.colors.BLACK,
                                                            bgcolor=ft.colors.with_opacity(0.05, 'black'),
                                                            inputborder=ft.InputBorder.NONE
                                                        ) for i in range(len(textfields['hint_text']))
                                                    ],
                                                    col={'sm': 12},
                                                    spacing=5,
                                                ),
                                                ft.ResponsiveRow(
                                                    controls=[
                                                        ft.FloatingActionButton(
                                                            text=list(strings.keys())[2].upper(),
                                                            foreground_color=ft.colors.WHITE,
                                                            bgcolor=ft.colors.BLUE,
                                                            height=40,
                                                            elevation=0,
                                                            col={'sm': 12},
                                                            on_click=lambda e: logar(e, page, user_textfields)
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.TextButton(
                                                    text='Criar conta',
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.colors.TRANSPARENT,
                                                        color=ft.colors.BLUE
                                                    ),
                                                    tooltip='Registar',
                                                    on_click= lambda e: page.go('/register')
                                                ),
                                                ft.TextButton(
                                                    text='Esqueci senha',
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.colors.TRANSPARENT,
                                                        color=ft.colors.BLUE
                                                    )
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        )
                                    ]
                                )
                            )
                        ],
                        height=height,
                        width=width,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
            
        ]
    )

    return view

def logar(e: ft.ControlEvent, page: ft.Page, user_textfields: ft.Column):
    global user
    preenchido = False
    user_data = []

    for i, control in enumerate(user_textfields.controls):
        if control.value == '':
            toast_flet.error(page, f'{control.hint_text} não preenchido', toast_flet.position.TOP_RIGHT)
            user_data.clear()
            break

        else:
            user_data.append(control.value)

        if i == len(user_textfields.controls) - 1:
            preenchido = True
    
    if preenchido == True:
        data = ver_dados(
            condition=f'username = "{user_data[0]}" and password = "{db.encriptarValor(user_data[1])}"'
        )

        if len(data) > 0:
            user.extend([data[0][0], data[0][1]])
            page.go('/')
        
        else:
            for control in user_textfields.controls:
                control.value = ''

            toast_flet.error(page, 'Username ou password incorrectos', toast_flet.position.TOP_RIGHT)
            
            page.update()