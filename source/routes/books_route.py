from flask import Flask, Blueprint, jsonify

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["GET"])
def listar_livros():
    return jsonify([
        {"nome": "livro1"}, 
        {"name": "livro2"}
        ])