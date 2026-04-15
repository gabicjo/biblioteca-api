from models import books_model


def __verificar_colunas_faltantes(dados: dict, requeridos: list) -> list:
    faltando = []

    for item in requeridos:
        if item not in dados or dados[item] in [None, "", []]:
            faltando.append(item)

    return faltando


def __corrigir_dados_vazios(dados: dict) -> dict:
    if "autor" not in dados or dados['autor'] == "":
        dados["autor"] = "Desconhecido"

    if "language" not in dados or dados['language'] == "":
        dados["language"] = "english"
    
    if "status" not in dados or dados['status'] == "":
        dados["status"] = "disponivel"

    return dados


def verificar_dados_recebidos(dados: dict) -> str:
    faltando = __verificar_colunas_faltantes(dados, ["name", "publish_date", "page_number", "genre"])

    if faltando:
        return "error"

    dados = __corrigir_dados_vazios(dados)

    books_model.adicionar_livro_novo(dados)
    return "ok"