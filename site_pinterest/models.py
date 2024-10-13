from site_pinterest import database, login_manager
from datetime import datetime, timezone
# UserMixin é quem diz qual é a classe que vai gerenciar a estrutura de login
from flask_login import UserMixin

# login_manager precisa de uma funcao que vai receber id de uma usuario e vai retornar quem é esse usuario
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    """
    Essa linha de código está dizendo ao Python que cada usuário pode ter várias fotos associadas a ele.
    backref='usuario': Este é um recurso bacana que diz ao Python para criar uma forma de acessar o usuário relacionado a cada foto. Então, quando tivermos uma foto, poderemos facilmente descobrir qual usuário a postou fazendo foto.usuario.
    lazy=True: Isso significa que o Python só vai buscar essas informações quando realmente precisarmos delas, o que ajuda a tornar o programa mais eficiente."""
     # fotos é a relacao da tabela usuario para fotos para depois quando eu fizer usuario.fotos, eu possa acessar os fotos do usuario
    fotos = database.relationship('Foto', backref='usuario', lazy=True)




class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now(timezone.utc))
    # id_usuario é o campo que relaciona as fotos com o usuario
    """
    Essa coluna "id_usuario" serve para armazenar o identificador único de um usuário na tabela do banco de dados. Ela está vinculada à tabela "usuario" através da chave estrangeira (ForeignKey), o que significa que ela guarda um número que corresponde ao ID de um usuário específico na outra tabela. Isso é útil para estabelecer relações entre diferentes tabelas de um banco de dados, permitindo, por exemplo, associar informações de um usuário a outros dados armazenados em outras tabelas."""
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)