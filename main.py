from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Chargement des fichiers KV
Builder.load_file("ui/main_screen.kv")
Builder.load_file("ui/sell_screen.kv")
Builder.load_file("ui/buy_screen.kv")
Builder.load_file("ui/stats_screen.kv")


class MainScreen(Screen):
    pass


class VenteScreen(Screen):
    pass


class AchatScreen(Screen):
    pass


class StatScreen(Screen):
    pass


class GestionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(VenteScreen(name="vente"))
        sm.add_widget(AchatScreen(name="achat"))
        sm.add_widget(StatScreen(name="stat"))
        return sm


if __name__ == "__main__":
    GestionApp().run()