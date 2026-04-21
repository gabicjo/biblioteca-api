from flask import Flask, Blueprint, jsonify, request

login_bp = Blueprint("auth", __name__)

@login_bp.route("/accont/login", methods=["POST"])
def login():
    return {"message": "testando"}