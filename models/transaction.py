import sqlite3

from utils.constants import DB_PATH


def create_database(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Transactions
                   (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       date       TEXT DEFAULT (datetime('now', 'localtime')),
                       unit_price REAL    NOT NULL,
                       quantity   INTEGER NOT NULL CHECK (quantity > 0),
                       product_id INTEGER NOT NULL,
                       type       TEXT    NOT NULL CHECK (type IN ('BUY', 'SELL'))
                   )
                   """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
