from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
import requests

from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from screens.base_screen import BaseScreen
from dialogs.dialog_utils import show_dialog

class MyApp(MDApp):
    def build(self):
        self.store = JsonStore("user_data.json")  # Armazenar dados do usuário
        Builder.load_file('kv/layout.kv')
        
        sm = self.root  # Obter o ScreenManager do layout .kv

        # Verificar se já está logado
        if self.store.exists("user"):
            token = self.store.get("user").get("token")
            if token:
                # Ir para a tela principal se o token existir
                sm.current = "home"

        return sm

    def login(self, username, password):
        url = "https://francsilva.com.br/api/token/"  # URL da sua API de login
        data = {"username": username, "password": password}

        try:
            # Enviando requisição de login
            response = requests.post(url, json=data)

            if response.status_code == 200:
                # Login bem-sucedido
                token = response.json().get("token")
                if token:
                    # Salvando o token no armazenamento local
                    self.store.put("user", token=token)
                    self.root.current = "home"
                else:
                    show_dialog("Erro", "Token não encontrado na resposta.")
            else:
                # Falha no login
                show_dialog("Erro", "Usuário ou senha inválidos.")
        except requests.RequestException as e:
            # Erro de conexão ou outro problema com a requisição
            show_dialog("Erro", f"Erro ao conectar: {e}")

if __name__ == "__main__":
    MyApp().run()