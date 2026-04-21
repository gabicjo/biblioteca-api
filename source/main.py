from flask import Flask
from flask_cors import CORS
from routes.books_route import books_bp
from routes.emprestimo_routes import emprestimo_bp
from flask_login import login_user, LoginManager
from routes.users_routes import login_bp
from models.users_model import User

URLPREFIX = "/api"

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave_123"
CORS(app)

login_manager.init_app(app)
login_manager.login_view = "auth.login"

app.register_blueprint(books_bp, url_prefix=URLPREFIX)
app.register_blueprint(emprestimo_bp, url_prefix=URLPREFIX)
app.register_blueprint(login_bp, url_prefix=URLPREFIX)

if __name__ == "__main__":
    app.run(debug=True)
