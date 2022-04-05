"""Module filters"""
from flask import Flask


def load(app: Flask) -> Flask:
    """
    load
    :param app:
    :return:
    """
    @app.template_filter()
    def text_upper(text):
        """
        Filter
        :param text:
        :return:
        """
        return text.upper()

    @app.template_filter()
    def text_truncate(text):
        """
        Filter
        :param text:
        :return:
        """
        return text[:80] + ' [...]'

    return app
