"""System module."""
__version__ = '0.1.0'
from flask import Flask


def create_app():
    """
    Esta função criar a instância do app
    :return:
    """
    app = Flask(__name__)
    @app.route("/testing")
    def testing():
        return "Testing"
    return app
