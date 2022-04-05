"""Routes module"""
from flask import Flask, render_template


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

    @app.route('/home')
    def home():
        name = 'Home Page'
        long_text = (
            'Lorem ipsum asdasdsadsadasdasdasdsadasd asdasdsad sads'
            '1asdas dasdsadasdasd @ asdsadasdas dasd asdasd as dasd #'
        )
        render = render_template('home.html', name=name, long_text=long_text)
        return render

    return app
