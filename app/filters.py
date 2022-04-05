"""Module filters"""


def text_upper(text):
    """
    Filter
    :param text:
    :return:
    """
    return text.upper()


def text_truncate(text):
    """
    Filter
    :param text:
    :return:
    """
    return text[:80] + ' [...]'
