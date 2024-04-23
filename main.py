import flet as ft
from control import request

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    request.identify_plant2('assets/images/rose.jpg')


if __name__ == '__main__':
    ft.app(main)