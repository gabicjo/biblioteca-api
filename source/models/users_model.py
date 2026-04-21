import sqlite3

def criar_tabela_users():
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                    )""")
    
    conexão.commit()
    conexão.close()