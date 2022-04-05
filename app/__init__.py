"""System module."""
__version__ = '0.1.0'
import os

import jinja2
from flask import Flask, render_template

from app import filters, routes
from config import BASE_DIR


def create_app():
    """
    Esta função cria a instância do app
    :return:
    """
    template_folder = os.path.join(BASE_DIR, 'resources', 'templates')
    static_folder = os.path.join(BASE_DIR, 'resources', 'static')
    app = Flask(
        __name__, template_folder=template_folder, static_folder=static_folder
    )

    routes.load(app)
    filters.load(app)

    return app
