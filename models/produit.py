import sqlite3

from utils.constants import DB_PATH


def create_database(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Product
                   (
                       id             INTEGER PRIMARY KEY AUTOINCREMENT,
                       name           TEXT    NOT NULL,
                       purchase_price REAL,
                       stock          INTEGER NOT NULL CHECK (stock >= 0)
                   )
                   """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
