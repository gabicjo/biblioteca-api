import sqlite3

def emprestar_livro(book_id):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("UPDATE livros SET status = 'emprestado' WHERE id = ?", (book_id,))
    
    conexão.commit()
    conexão.close()

def verificar_status(book_id):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("SELECT status FROM livros WHERE id = ?", (book_id,))

    return cursor.fetchone()[0]
