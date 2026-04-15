from flask import Flask, Blueprint, jsonify, request
from models import books_model
books_bp = Blueprint("books", __name__)

@books_bp.route("/books/add", methods=["POST"])
def listar_livros():
    dados = request.get_json()
    books_model.adicionar_livro_novo(dados)

    return {"message": "dados adicionados com sucesso"}, 201