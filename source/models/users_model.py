import sqlite3
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    @staticmethod
    def get(user_id):
        conexão = sqlite3.connect("banco.db")
        cursor = conexão.cursor()
        cursor.execute("SELECT id, name, password FROM users WHERE id = ?", (user_id,))
        user_data = cursor.fetchone()
        conexão.close()
        if user_data:
            return User(*user_data)
        return None


def dados_do_usuario_name(user_name):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("SELECT id, name, password FROM users WHERE name = ?", (user_name,))
    user_data = cursor.fetchone()
    conexão.close()
    return user_data


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


def dados_do_usuario_by_id(user_id):
    conexão = sqlite3.connect("banco.db")
    cursor = conexão.cursor()

    cursor.execute("SELECT * FROM users WHERE name = ?", (user_id,))
    return cursor.fetchone()
