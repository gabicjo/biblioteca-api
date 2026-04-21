from flask import Flask, Blueprint, jsonify, request
from models import books_model
from controller import books_controller
from utils.errors import DadosInvalidosError
from utils.verificar_existencia import verificar_esse_livro_existe
from flask_login import login_required

books_bp = Blueprint("books", __name__)


@books_bp.route("/books/add", methods=["POST"])
@login_required
def adicionar_livros():
    dados = request.get_json()
    try:
        verify = books_controller.verificar_dados_recebidos(dados)

        if verify == "error":
            return {"message": "dados insuficientes"}, 400

        return {"message": "dados adicionados com sucesso"}, 201
        
    except DadosInvalidosError:
        return {"message": "dados invalidos"}, 400


@books_bp.route("/books/delete/<int:book_id>", methods=["DELETE"])
@login_required
def deletar_livro(book_id):
    req = verificar_esse_livro_existe(book_id)

    if req:
        books_model.deletar_livro(book_id)
        return jsonify({"message": "livro deletado com sucesso"}), 200
    return jsonify({"message": "livro não encontrado"}), 404


@books_bp.route("/books", methods=["GET"])
def exibir_livros():
    return jsonify(books_model.exibir_todos_livros()), 200


@books_bp.route("/books/<int:book_id>", methods=["GET"])
def exibir_detalhes_livro(book_id):
    if verificar_esse_livro_existe(book_id):
        return jsonify(books_model.exibir_detalhes_livro(book_id)), 200
    return jsonify({"message": "livro não encontrado"}), 404


@books_bp.route("/books/update/<int:book_id>", methods=["PUT"])
@login_required
def atualizar_informações_livro(book_id):
    if verificar_esse_livro_existe(book_id):
        response = request.json

        books_model.atualizar_informações(book_id, response)
        return jsonify({"message": "livro atualizado com sucesso"}), 200
    return jsonify({"message": "livro não encontrado"}), 404