from screens.base_screen import BaseScreen
from kivy.lang import Builder

KV = """
<HomeScreen>:
    name: "home"

    MDLabel:
        text: "Bem-vindo à Tela Principal!"
        halign: "center"
"""

class HomeScreen(BaseScreen):
    pass

Builder.load_string(KV)