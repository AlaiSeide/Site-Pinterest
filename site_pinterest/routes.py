from site_pinterest import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('homepage.html')



@app.route('/perfil/<usuario>')
def perfil(usuario):
    # o valor que vai ser passado no url sera passado para a minha pagina html, onde o usuario que está recenbendo o valor sera passado para o meu html usuario=usuario
    return render_template('perfil.html', usuario=usuario)