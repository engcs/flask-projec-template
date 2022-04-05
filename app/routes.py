"""Routes module"""
from flask import Flask, render_template

def load(app: Flask) -> Flask:
    @app.route('/testing')
    def testing():
        render = render_template('testing.html')
        return render

    @app.route('/home')
    def home():
        name = 'Home Page'
        render = render_template('home.html', name=name)
        return render
    return app
