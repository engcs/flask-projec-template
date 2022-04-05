"""System module."""
__version__ = '0.1.0'
import os
from flask import Flask, render_template
from config import BASE_DIR


def create_app():
    """
    Esta função cria a instância do app
    :return:
    """
    template_folder = os.path.join(BASE_DIR, "resources", "templates")
    static_folder = os.path.join(BASE_DIR, "resources", "templates")
    app = Flask(__name__,
                template_folder=template_folder,
                static_folder=static_folder)

    @app.route("/testing")
    def testing():
        render = render_template("testing.html")
        return render

    @app.route("/home")
    def home():
        render = render_template("home.html")
        return render
    return app
