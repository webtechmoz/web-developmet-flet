import flet as ft
from views.home import home
from views.register import register
from views.login import login

def main(page: ft.Page):
    page.title = page.route

    WIDTH: int = page.width
    HEIGHT: int = page.height

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(home(page, WIDTH, HEIGHT))
        
        elif page.route == '/register':
            page.views.append(register(page, WIDTH, HEIGHT))
        
        elif page.route == '/login':
            page.views.append(login(page, WIDTH, HEIGHT))
        
        page.title = page.route
        page.update()
        page.overlay.clear()

    
    page.on_route_change = router
    page.go('/login')

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')