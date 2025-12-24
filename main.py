import os
import sqlite3

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from utils.constants import DB_PATH
from utils.stock import vente, achat

# Chargement des fichiers KV
Builder.load_file("ui/main_screen.kv")
Builder.load_file("ui/sell_screen.kv")
Builder.load_file("ui/buy_screen.kv")
Builder.load_file("ui/finance_screen.kv")
Builder.load_file("ui/inventaire_screen.kv")


class CustomScreen(Screen):
    def decimal_filter(self, value, from_undo):
        if value == "." and "." not in self.ids.prix.text:
            return value
        if value.isdigit():
            return value
        return ""

    def show_error(self, message, duration=10):
        label = self.ids.error_label
        label.text = message
        Clock.unschedule(self.clear_error)
        Clock.schedule_once(self.clear_error, duration)

    def clear_error(self, *args):
        self.ids.error_label.text = ""

    def reset_text(self):
        self.ids.nom_produit.text = ""
        self.ids.quantite.text = ""
        self.ids.prix.text = ""


class VenteScreen(CustomScreen):
    def vente(self, nom, quantite, prix_total):
        try:
            prix_total = float(prix_total)
        except ValueError:
            self.show_error("Prix invalide")
            return
        try:
            quantite = int(quantite)
        except ValueError:
            self.show_error("quantite invalide")
            return
        try:
            vente(nom, quantite, prix_total)
        except ValueError as e:
            print(e)
            self.show_error(str(e))
            return

        self.reset_text()
        print(
            f"Vente de {quantite} {nom} pour {prix_total} euros."
        )


class AchatScreen(CustomScreen):
    def achat(self, nom, quantite, prix_total):
        try:
            prix_total = float(prix_total)
        except ValueError:
            self.show_error("Prix invalide")
            return
        try:
            quantite = int(quantite)
        except ValueError:
            self.show_error("quantite invalide")
            return
        try:
            achat(nom, quantite, prix_total)
        except ValueError as e:
            print(e)
            self.show_error(str(e))
            return

        self.reset_text()
        print(
            f"achat de {quantite} {nom} pour {prix_total} euros. "
        )


class FinanceScreen(CustomScreen):
    pass


class InventaireScreen(CustomScreen):
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


class MainScreen(CustomScreen):
    pass


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
