import flet as ft

def Text(
    value: str,
    size: str,
    color: ft.colors,
    weight: ft.FontWeight = 'bold',
    text_align: ft.TextAlign = ft.TextAlign.LEFT,
    selectable: bool = True
):
    text = ft.Text(
        value=value,
        size=size,
        color=ft.colors.with_opacity(0.8, color),
        weight=weight,
        text_align=text_align,
        selectable=selectable
    )

    return text

def Divider(
    height: int = 1,
    thickness: int = 2,
    visible: bool = True
):
    divider = ft.Divider(
        height=height,
        visible=visible,
        thickness=thickness
    )

    return divider

def SnackBar(
    page: ft.Page,
    icon: ft.icons,
    value: str,
    color: ft.colors,
    bgcolor: ft.colors = None
):
    snackbar = ft.SnackBar(
        bgcolor=bgcolor,
        content=ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=25,
                    color=color
                ),
                Text(
                    value=value,
                    size=13,
                    color=color,
                )
            ]
        )
    )

    page.overlay.append(snackbar)
    snackbar.open = True
    page.update()

    return snackbar

def TextField(
    hint_text: str,
    prefix_icon: ft.icons,
    size: int,
    color: ft.colors,
    bgcolor: ft.colors = None,
    inputborder: ft.InputBorder = ft.InputBorder.UNDERLINE,
    on_change: ft.ControlEvent = None,
    text_vertical_align: float = -0.50,
    col: dict = None,
    width: int = None,
    height: int = 45,
    password: bool = False,
    autofocus: bool = False,
    weight: ft.FontWeight = 'bold'
):
    textfield = ft.TextField(
        hint_text=hint_text,
        hint_style=ft.TextStyle(
            size=size,
            color=ft.colors.with_opacity(0.6, color),
            weight=weight
        ),
        text_style=ft.TextStyle(
            size=size,
            color=ft.colors.with_opacity(0.6, color),
            weight=weight
        ),
        prefix_icon=prefix_icon,
        password=password,
        height=height,
        width=width,
        col=col,
        bgcolor=bgcolor,
        border=inputborder,
        on_change=on_change,
        autofocus=autofocus,
        text_vertical_align=text_vertical_align
    )

    return textfield

def InconButton(
    icon: ft.icons,
    size: int = 25,
    tooltip: str = None,
    color: ft.colors = ft.colors.BLUE,
    on_click: ft.ControlEvent = None
):
    inconbutton = ft.IconButton(
        icon=icon,
        icon_size=size,
        icon_color=color,
        on_click=on_click,
        tooltip=tooltip
    )

    return inconbutton

def clicked(page: ft.Page, e: ft.ControlEvent):
    SnackBar(
        page=page,
        icon=ft.icons.MENU_BOOK,
        value=e.control,
        color=ft.colors.BLUE
    )
    
    page.update()