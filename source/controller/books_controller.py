from models import books_model
from utils.errors import DadosInvalidosError


def __verificar_colunas_faltantes(dados: dict, requeridos: list) -> list:
    faltando = []

    for item in requeridos:
        if item not in dados or dados[item] in [None, "", []]:
            faltando.append(item)

    return faltando


def __corrigir_dados_vazios(dados: dict) -> dict:
    if "autor" not in dados or dados["autor"] == "":
        dados["autor"] = "Desconhecido"

    if "language" not in dados or dados["language"] == "":
        dados["language"] = "english"

    if "status" not in dados or dados["status"] == "":
        dados["status"] = "disponivel"

    return dados


def __corrigir_dados_invalidos(dados: dict) -> dict:
    if dados["status"] not in ["disponivel", "emprestado"]:
        dados["status"] = "disponivel"

    if len(str(dados["publish_date"])) > 4:
        raise DadosInvalidosError("Dados invalidos")

    if dados["page_number"] < 30:
        raise DadosInvalidosError("Dados invalidos")

    return dados


def verificar_dados_recebidos(dados: dict) -> str:
    faltando = __verificar_colunas_faltantes(dados, ["name", "publish_date", "page_number", "genre"])

    if faltando:
        return "error"

    dados = __corrigir_dados_vazios(dados)
    dados = __corrigir_dados_invalidos(dados)

    books_model.adicionar_livro_novo(dados)
    return "ok"

def verificar_esse_livro_existe(book_id):
    req = books_model.verificar_existencia_livro(book_id=book_id)
    if req is not None:
        return True
    return False