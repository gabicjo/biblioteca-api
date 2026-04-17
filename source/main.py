from flask import Flask
from flask_cors import CORS
from routes.books_route import books_bp
from routes.emprestimo_routes import emprestimo_bp

URLPREFIX = "/api"

app = Flask(__name__)
CORS(app)

app.register_blueprint(books_bp, url_prefix=URLPREFIX)
app.register_blueprint(emprestimo_bp, url_prefix=URLPREFIX)

if __name__ == "__main__":
    app.run(debug=True)