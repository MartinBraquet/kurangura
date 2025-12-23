import sqlite3

from models import DB_PATH


def achat(nom,quantite,prix_total):
    prix_unitaire = prix_total / quantite
    produit=get_product(nom)
    if produit is None:
        update_product(None, nom, prix_unitaire, quantite)
    else:
        stock = produit["stock"] + quantite
        update_product(produit["id"], nom, prix_unitaire, stock)


def vente(nom,quantite,prix_total):
    prix_unitaire=prix_total/quantite


def update_product(product_id, name, purchase_price, stock):
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

    conn.commit()
    conn.close()


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




