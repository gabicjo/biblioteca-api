# Sistema de Biblioteca API

API REST para gerenciamento de uma biblioteca, permitindo controle de livros, usuários e emprestimos.

## Tecnologias

- **Python 3.12+**
- **Flask** - Framework web
- **Flask-CORS** - Suporte a Cross-Origin
- **Flask-Login** - Autenticacao de usuarios
- **SQLite** - Banco de dados

## Estrutura do Projeto

```
projeto/
├── source/
│   ├── main.py              # ponto de entrada da aplicacao
│   ├── controller/         # logica de negocio
│   │   ├── books_controller.py
│   │   ├── users_controller.py
│   │   └── emprestimo_controller.py
│   ├── models/            # acesso ao banco de dados
│   │   ├── books_model.py
│   │   ├── users_model.py
│   │   └── emprestimo_model.py
│   ├── routes/            # endpoints da API
│   │   ├── books_route.py
│   │   ├── users_routes.py
│   │   └── emprestimo_routes.py
│   └── utils/            # helpers e excecoes
│       ├── errors.py
│       └── verificar_existencia.py
├── banco.db              # banco de dados SQLite
└── requirements.txt      # dependencias do projeto
```

## Endpoints

### Livros
| Metodo | Rota | Autenticado | Descricao |
|--------|------|------------|------------|
| GET | `/api/books` | Nao | Lista todos os livros |
| GET | `/api/books/<id>` | Nao | Exibe detalhes de um livro |
| POST | `/api/books/add` | Sim | Adiciona um novo livro |
| PUT | `/api/books/update/<id>` | Sim | Atualiza um livro |
| DELETE | `/api/books/delete/<id>` | Sim | Deleta um livro |

### Emprestimos
| Metodo | Rota | Autenticado | Descricao |
|--------|------|------------|------------|
| PUT | `/api/books/emprestar/<id>` | Sim | Empresta um livro |
| PUT | `/api/books/devolver/<id>` | Sim | Devolve um livro |

### Autenticacao
| Metodo | Rota | Autenticado | Descricao |
|--------|------|------------|------------|
| POST | `/api/account/login` | Nao | Login de usuario |
| POST | `/api/account/logout` | Sim | Logout de usuario |

## Instalacao

```bash
pip install -r requirements.txt
```

## Uso

```bash
cd source
python main.py
```

A API ficara disponivel em `http://localhost:5000`.

## Exemplos de Uso

### Adicionar livro
```bash
curl -X POST http://localhost:5000/api/books/add \
  -H "Content-Type: application/json" \
  -d '{
    "name": "O Senhor dos Aneis",
    "autor": "J.R.R. Tolkien",
    "publish_date": 1954,
    "page_number": 1200,
    "language": "pt",
    "genre": "Fantasia",
    "status": "disponivel"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/account/login \
  -H "Content-Type: application/json" \
  -d '{"name": "usuario", "password": "senha"}'
```

### Emprestar livro
```bash
curl -X PUT http://localhost:5000/api/books/emprestar/1
```

## Licenca

MIT