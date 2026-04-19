from flask import Flask, Blueprint, jsonify, request
from utils.verificar_existencia import verificar_esse_livro_existe
from controller import emprestimo_controller
from models import emprestimo_model

emprestimo_bp = Blueprint("emprestimo", __name__)


@emprestimo_bp.route("/books/emprestar/<int:book_id>", methods=["PUT"])
def emprestar_livro(book_id):
    if verificar_esse_livro_existe(book_id):
        if emprestimo_controller.verificar_pode_emprestar(book_id):
            emprestimo_model.emprestar_livro(book_id)
            return jsonify({"message": "livro emprestado"})
        
        return jsonify({"message": "livro já emprestado"}), 400

    return jsonify({"message": "livro não encontrado"}), 404

@emprestimo_bp.route("/books/devolver/<int:book_id>", methods=["PUT"])
def devolver_livro(book_id):
    if verificar_esse_livro_existe(book_id):
        if emprestimo_controller.verificar_pode_devolver(book_id):
            emprestimo_model.devolver_livro(book_id)
            return jsonify({"message": "livro devolvido"})
        
        return jsonify({"message": "livro já disponivel"}), 400

    return jsonify({"message": "livro não encontrado"}), 404