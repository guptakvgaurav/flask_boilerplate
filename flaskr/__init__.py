from flask import Flask
from .apis.user import user_blueprint
from logging.config import dictConfig
from .settings import config


def create_app():
    """
    Flask factory function which gives the app server instance.
    :return:
    """
    dictConfig(config.log_config)
    flask_app = Flask(__name__)
    flask_app.config.update(config.flask_config)

    # register the api blueprint here.
    flask_app.register_blueprint(user_blueprint)

    if __name__ == '__main__':
        flask_app.run()

    return flask_app
