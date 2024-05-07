from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# __name__ é o nome do arquivo que vai rodar o nosso projeto por exemplo main.py
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)



# as rotas do nosso site
from site_pinterest import routes
