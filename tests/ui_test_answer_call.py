import time
import pytest
from fixture.application import Application


def test_ui_answer(app):
    app.login()
    app.header_page()
    app.click_when_availible()
    app.destroy()
