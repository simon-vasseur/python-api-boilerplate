from datetime import timedelta

from flask import Flask
from flask_cors import CORS

from .api import CustomResponse, ExtendedRequest
from .api.errors import setup_error_handlers


class App(Flask):

    response_class = CustomResponse
    request_class = ExtendedRequest


def create_app():
    """
        Initialize application
    """
    app = App(__name__)
    setup_api(app)

    return app


def setup_api(app):

    CORS(app, supports_credentials=True)

    from .api.views import views_to_register

    for view in views_to_register:
        prefix = "/api{}".format(view.url_prefix or "")
        app.register_blueprint(view, url_prefix=prefix)

    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=90)

    setup_error_handlers(app)
