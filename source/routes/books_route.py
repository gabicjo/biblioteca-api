from flask import Flask, Blueprint, jsonify, request
from models import books_model
from controller import books_controller
from utils.errors import DadosInvalidosError

books_bp = Blueprint("books", __name__)

@books_bp.route("/books/add", methods=["POST"])
def listar_livros():
    dados = request.get_json()
    try:
        verify = books_controller.verificar_dados_recebidos(dados)

        if verify == "error":
            return {"message": "dados insuficientes"}, 400

        return {"message": "dados adicionados com sucesso"}, 201
        
    except DadosInvalidosError:
        return {"message": "dados invalidos"}, 400

@books_bp.route("/books/delete/<int:book_id>", methods=["DELETE"])
def deletar_livro(book_id):
    req = books_controller.verificar_esse_livro_existe(book_id)
    if req:
        books_model.deletar_livro(book_id)
        return jsonify({"message": "livro deletado com sucesso"}), 200
    return jsonify({"message": "livro não encontrado"}), 404