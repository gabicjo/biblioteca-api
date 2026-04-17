from models import books_model

def verificar_esse_livro_existe(book_id):
    req = books_model.verificar_existencia_livro(book_id=book_id)
    if req is not None:
        return True
    return False