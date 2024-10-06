from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

KV = """
<LoginScreen>:
    name: "login"

    MDTextField:
        id: username
        hint_text: "Usuário"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.8

    MDTextField:
        id: password
        hint_text: "Senha"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.8

    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.login(username.text, password.text)
"""

class LoginScreen(Screen):
    pass

Builder.load_string(KV)