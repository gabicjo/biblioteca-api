import sqlite3

conexão = sqlite3.connect("banco.db")
cursor = conexão.cursor()

def criar_tabela_books():
    cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    publish_date INTEGER NOT NULL,
                    page_number INTEGER NOT NULL,
                    language TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    status TEXT NOT NULL
                    )""")

criar_tabela_books()

conexão.commit()