import time
import pytest
from fixture.application import Application


def test_ui_answer(app):
    app.select_operator()
    app.header_page()
    app.destroy()
