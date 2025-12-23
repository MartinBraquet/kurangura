import os
import sqlite3

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from utils.constants import DB_PATH

# Chargement des fichiers KV
Builder.load_file("ui/main_screen.kv")
Builder.load_file("ui/sell_screen.kv")
Builder.load_file("ui/buy_screen.kv")
Builder.load_file("ui/finance_screen.kv")
Builder.load_file("ui/inventaire_screen.kv")


class MainScreen(Screen):
    pass


class VenteScreen(Screen):
    pass


class AchatScreen(Screen):
    pass


class FinanceScreen(Screen):
    pass


class InventaireScreen(Screen):
    products = ListProperty([])

    def on_pre_enter(self):
        self.load_inventory()

    def load_inventory(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT name, stock
                       FROM Product
                       ORDER BY name
                       """)

        rows = cursor.fetchall()
        conn.close()

        print(rows)

        self.products = [
            {
                "name": row[0],
                "stock": row[1]
            }
            for row in rows
        ]


class GestionApp(App):
    def build(self):

        if not os.path.exists(DB_PATH):
            print("Creation de la base de donnees")
            from models import produit, transaction
            produit.create_database()
            transaction.create_database()

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(VenteScreen(name="vente"))
        sm.add_widget(AchatScreen(name="achat"))
        sm.add_widget(FinanceScreen(name="finance"))
        sm.add_widget(InventaireScreen(name="inventaire"))
        return sm


if __name__ == "__main__":
    GestionApp().run()
