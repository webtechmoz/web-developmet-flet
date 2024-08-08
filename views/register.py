import flet as ft
from configs.settings import settings
from utils.Strings import strings
from Toast import toast_flet
from connections.usuarios import (
    db,
    inserir_dados
)
from controls.controls import (
    Text,
    TextField,
    clicked,
    Divider
)

def register(page: ft.Page, width: int, height: int):

    textfields = {
        'hint_text': ['Nome', 'Username', 'Email', 'Password', 'Confirmar password'],
        'icon': [ft.icons.PERSON, ft.icons.PERSON, ft.icons.EMAIL, ft.icons.KEY, ft.icons.KEY],
        'password': [False, False, False, True, True],
        'autofocus': [True, False, False, False, False]
    }

    view = ft.View(
        route='/register',
        bgcolor=settings[list(settings.keys())[0]],

        controls=[
            ft.Stack(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={'xs': 11, 'sm': 11, 'md': 3.5},
                                height=height * 0.67,
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
                                                    value=list(strings.keys())[1].upper(),
                                                    size=14,
                                                    color=ft.colors.BLACK,
                                                    text_align='center'
                                                ),
                                                Text(
                                                    value=strings[list(strings.keys())[1]],
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
                                                            text=list(strings.keys())[1].upper(),
                                                            foreground_color=ft.colors.WHITE,
                                                            bgcolor=ft.colors.BLUE,
                                                            height=40,
                                                            elevation=0,
                                                            col={'sm': 12},
                                                            on_click=lambda e: registar(e, page, user_textfields)
                                                        )
                                                    ]
                                                )
                                            ]
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

def registar(e: ft.ControlEvent, page: ft.Page, user_textfields: ft.Column):
    user_data = []
    preenchido = False
    
    for i, control in enumerate(user_textfields.controls):
        if control.value == '':
            toast_flet.error(page, f'{control.hint_text} não preenchido', 'top_right')
            user_data.clear()
            page.update()
            break
        
        else:
            if control.hint_text == user_textfields.controls[-1].hint_text:
                if control.value == user_textfields.controls[i - 1].value:
                    user_data.append(db.encriptarValor(control.value))
                
                else:
                    control.value = ''
                    user_textfields.controls[i - 1].value = ''
                    user_data.clear()
                    toast_flet.error(page, f'Senha e confirmar senha diferentes', 'top_right')
                    break
            
            elif control == user_textfields.controls[-2]:
                pass

            else:
                user_data.append(control.value)
        
        if i == len(user_textfields.controls) - 1:
            user_data.append('True')
            preenchido = True
    
    if preenchido == True:
        inserir_dados(
            dados=user_data
        )
        user_data.clear()
        for i in range(len(user_textfields.controls)):
            user_textfields.controls[i].value = ''
        
        toast_flet.sucess(page, 'Usuário criado com sucesso', 'top_right')
        page.go('/login')
