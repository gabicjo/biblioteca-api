from models import emprestimo_model

def verificar_pode_emprestar(book_id):
    if emprestimo_model.verificar_status(book_id) == "disponivel":
        return True
    
    return False