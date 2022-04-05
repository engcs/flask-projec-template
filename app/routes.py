"""Routes module"""
from flask import Flask, render_template, request


def load(app: Flask) -> Flask:
    """
    Carrega as rotas
    :param app:
    :return:
    """

    @app.route('/testing')
    def testing():
        render = render_template('testing.html')
        return render

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        contact = ''

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            contact = f'<Name {name}> {email}'

        render = render_template('login.html', contact=contact)
        return render

    @app.route('/home')
    def home():
        name = 'Home Page'
        long_text = (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Nullam nec efficitur lacus. Nulla id sem sit amet justo '
            'sollicitudin consequat.'
        )
        itens = ['Item 1', 'Item 2', 'Item 3']
        render = render_template(
            'home.html', name=name, long_text=long_text, itens=itens
        )
        return render

    return app
