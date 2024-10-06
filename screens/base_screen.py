from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder

KV = """
<BaseScreen>
    MDBoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Meu Aplicativo"
            left_action_items: [['menu', lambda x: nav_drawer.set_state("toggle")]]

        MDNavigationLayout:
            ScreenManager:
                id: screen_manager
                HomeScreen:
                OtherScreen:  # Adicione mais telas aqui conforme necessário

            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
"""

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Exemplo de itens de menu
        self.add_widget(OneLineIconListItem(text="Home", on_release=self.change_screen))
        self.add_widget(OneLineIconListItem(text="Outra Tela", on_release=self.change_screen))

    def change_screen(self, instance):
        # Altera para a tela selecionada
        self.screen_manager.current = instance.text.lower()
        self.nav_drawer.set_state("close")

class BaseScreen(Screen):
    pass

Builder.load_string(KV)