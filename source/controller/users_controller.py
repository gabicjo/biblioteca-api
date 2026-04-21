from models import users_model


def verificar_dados_usuario(user_name, senha_fornecida):
    dados = users_model.dados_do_usuario_name(user_name)

    if dados and dados[2] == senha_fornecida:
        return users_model.User(dados[0], dados[1], dados[2])
    return None
