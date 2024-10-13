from site_pinterest import app

# debug=True significa que o servidor será reiniciado automaticamente sempre que você fizer uma alteração no seu código. Além disso, 
# se ocorrer um erro, você verá uma descrição detalhada do erro no navegador.
# Esta linha verifica se o script está sendo executado diretamente. Se for o caso, o bloco de código indentado abaixo dela será executado.
if __name__ == '__main__':
    app.run(debug=True)