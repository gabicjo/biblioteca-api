from flask import Flask, Blueprint, jsonify, request
from models import books_model
from controller import books_controller

books_bp = Blueprint("books", __name__)

@books_bp.route("/books/add", methods=["POST"])
def listar_livros():
    dados = request.get_json()
    verify = books_controller.verificar_dados_recebidos(dados)

    if verify == "error":
        return {"message": "dados insuficientes"}, 400

    return {"message": "dados adicionados com sucesso"}, 201