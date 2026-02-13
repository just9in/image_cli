import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "database.db")

def get_connection():
    return sqlite3.connect(DB_NAME)  
# its connected to database.db for data storage and servers as open connection to read/write

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS images(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL, 
        path TEXT NOT NULL,
        hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        )
    conn.commit()
    conn.close()


def insert_image(name, path, hash_value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO images (name, path, hash) VALUES (?, ?, ?)",
        (name, path, hash_value)
    )

    conn.commit()
    conn.close()


def get_all_images():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, path, hash FROM images")
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_image(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM images WHERE name = ?", (name,))
    conn.commit()

    affected = cursor.rowcount
    conn.close()

    return affected
