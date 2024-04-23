import flet as ft
from dotenv import load_dotenv
from control import requests


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    # requests.identify_plant2('assets/images/rose.jpg')
    # requests.trefle_identification()
    requests.get_wikipedia_info('https://en.wikipedia.org/wiki/Rosa_chinensis')

def configure():
    """
    Loads environment variables from a .env file into the system's environment.

    This function utilizes the `load_dotenv` method from the `dotenv` package to read a .env file
    located in the same directory as the script, or the project's root directory, and load the
    variables it contains into the environment. This allows these variables to be accessed
    using `os.getenv` throughout the application.

    No parameters are needed and the function does not return any values.
    """
    load_dotenv()

if __name__ == '__main__':
    configure()
    ft.app(main)
