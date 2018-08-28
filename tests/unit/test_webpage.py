import os
from flask import url_for
# def test_home_page(app):
#     """
#     GIVEN a Flask application
#     WHEN the '/' page is requested (GET)
#     THEN check the response is valid
#     """
#     response = app.get('/')
#
#     assert response.status_code == 200
def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Pek and Monk" in response.data