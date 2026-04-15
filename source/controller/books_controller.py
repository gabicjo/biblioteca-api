from models import books_model

def __verificar_colunas_faltantes(dados: dict, requeridos: list):
    faltando = []

    for item in requeridos:
        if item not in dados or dados[item] in [None, "", []]:
            faltando.append(item)

    return faltando

def verificar_dados_recebidos(dados):
    faltando = __verificar_colunas_faltantes(dados, ["name", "autor", "publish_date", "page_number", "genre"])

    if faltando:
        return "error"

    books_model.adicionar_livro_novo(dados)
    return "ok"