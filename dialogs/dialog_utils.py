from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

def show_dialog(app, title, text):
    dialog = MDDialog(
        title=title,
        text=text,
        buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())],
    )
    dialog.open()