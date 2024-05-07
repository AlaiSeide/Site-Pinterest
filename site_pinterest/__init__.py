from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# __name__ é o nome do arquivo que vai rodar o nosso projeto por exemplo main.py
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
"""Estamos definindo uma configuração específica, chamada "SECRET_KEY". Essa chave secreta é usada para proteger os dados da sessão e outras informações sensíveis na aplicação.
Ela é usada para criptografar e descriptografar dados sensíveis, como cookies de sessão e tokens de autenticação."""

app.config['SECRET_KEY'] = 'f2e005d0713826c596b29c5f5f7ddf35'
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# quando o usuario tentar acessar uma pagina sem fazer login, seria redirecionado para a pagina de login que é 'homepage'
login_manager.login_view = 'homepage'


# as rotas do nosso site
from site_pinterest import routes
