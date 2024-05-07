from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from site_pinterest.models import Usuario

# pip install email_validator para o validador do email
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_login = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Corfirmacao de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_criar_conta = SubmitField('Criar Conta')



    def validate_email(self, email):
        # buscar um usuario pelo email
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('E-mail já cadastrado, faca login para continuar')


class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_enviar_foto = SubmitField('Enviar')
