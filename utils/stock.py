import sqlite3

from utils.constants import DB_PATH


def achat(nom, quantite, prix_total):
    prix_unitaire = prix_total / quantite
    produit = get_product(nom)
    if produit is None:
        produit = update_product(None, nom, quantite)

    else:
        stock = produit["stock"] + quantite
        update_product(produit["id"], nom, stock)
    ajouter_transaction(product_id=produit["id"], quantite=quantite,
                        prix_unitaire=prix_unitaire, type="BUY")


def ajouter_transaction(product_id, quantite, prix_unitaire, type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO Transactions (product_id, quantity, unit_price, type)
                   VALUES (?, ?, ?, ?)
                   """, (product_id, quantite, prix_unitaire, type))
    conn.commit()
    conn.close()


def vente(nom, quantite, prix_total):
    prix_unitaire = prix_total / quantite
    produit = get_product(nom)
    if produit is None:
        update_product(None, nom, quantite)
    else:
        stock = produit["stock"] - quantite
        if 0 > stock:
            message = "Stock insuffisant pour la vente de {}.".format(nom)
            raise ValueError(message)

        update_product(produit["id"], nom, stock)
    ajouter_transaction(product_id=produit["id"], quantite=quantite,prix_unitaire=prix_unitaire, type="SELL")


def update_product(product_id, name, stock):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if product_id is None:
        cursor.execute("""
                       INSERT INTO Product (name, stock)
                       VALUES (?, ?)
                       """, (name, stock))
    else:
        cursor.execute("""
                       UPDATE Product
                       SET stock = ?
                       WHERE id = ?
                       """, (stock, product_id))
    product_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return {
        "id": product_id,
    }


def get_product(nom):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT id, name, purchase_price, stock
                   FROM Product
                   WHERE name = ?
                   """, (nom.lower(),))

    ligne = cursor.fetchone()
    conn.close()

    if ligne is None:
        return None

    return {
        "id": ligne[0],
        "name": ligne[1],
        "purchase_price": ligne[2],
        "stock": ligne[3]
    }


if __name__ == "__main__":
    achat("pomme", 3, 10000)
    achat("banane", 4, 2000)
    vente("pomme", 2, 10000)
