import sqlite3

def criar_tabela_books():
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

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

def adicionar_livro_novo(dados: dict):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()
    colunas = ",".join(dados.keys())
    placeholders = ",".join([f":{k}" for k in dados.keys()])

    sql = f"INSERT INTO livros ({colunas}) VALUES ({placeholders})"

    cursor.execute(sql, dados)
    conexão.commit()

def verificar_existencia_livro(book_id):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("SELECT 1 FROM livros WHERE id = ?", (book_id,))

    return cursor.fetchone()

def deletar_livro(book_id):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (book_id,))
    conexão.commit()

def exibir_todos_livros():
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("SELECT * FROM livros")
    return cursor.fetchall()