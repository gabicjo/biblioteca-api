from flask import Flask, Blueprint, jsonify, request
from controller import users_controller
from flask_login import login_user

login_bp = Blueprint("auth", __name__)


@login_bp.route("/account/login", methods=["POST"])
def login():
    data = request.json
    user = users_controller.verificar_dados_usuario(data["name"], data["password"])
    if user:
        login_user(user)
        return jsonify({"message": "usuario logado com sucesso"}), 200

    return jsonify({"message": "informações incorretas"}), 401
