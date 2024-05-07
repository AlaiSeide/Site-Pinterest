from site_pinterest import app, database, bcrypt
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from site_pinterest.forms import FormLogin, FormCriarConta, FormFoto
from site_pinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()

    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)



@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(formcriarconta.senha.data)

        usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):  # Define uma função chamada 'perfil' que recebe um parâmetro 'id_usuario'.
    if int(id_usuario) == int(current_user.id):  # Verifica se o 'id_usuario' é igual ao ID do usuário atualmente logado.
        # Se for verdade, significa que o usuário está visualizando seu próprio perfil.
        formfoto = FormFoto()

        if formfoto.validate_on_submit():
            arquivo = formfoto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # os.path.abspath(os.path.dirname(__file__)) caminho do meu projeto onde está o routes.py
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], nome_seguro)
            # salvar o arquivo na pasta fotos_posts
            arquivo.save(caminho)
            # registrar esse arquivo no nosso banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, formfoto=formfoto)  # Retorna a página de perfil renderizada com os dados do usuário atual.
    else:  # Se o 'id_usuario' não for igual ao ID do usuário atualmente logado...
        # ...significa que o usuário está visualizando o perfil de outro usuário.
        usuario = Usuario.query.get(int(id_usuario))  # Busca no banco de dados o usuário com o ID especificado.
        return render_template('perfil.html', usuario=usuario, formfoto=None)  # Retorna a página de perfil renderizada com os dados do usuário buscado.



@app.route('/sair')
@login_required
def logout():

    logout_user()
    return redirect(url_for('homepage'))



@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template('feed.html', fotos=fotos)