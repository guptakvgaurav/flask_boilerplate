from flask import Flask
from celery import Celery

from logging.config import dictConfig
from .settings import config

celery = Celery(__name__,
                backend="redis://localhost:6379",
                broker="redis://localhost:6379")


def create_app(config_name):
    """
    Flask factory function which gives the app server instance.
    :return:
    """
    from .apis.user import user_blueprint
    dictConfig(config.log_config)
    flask_app = Flask(__name__)
    flask_app.config.update(config.flask_config)

    # register the api blueprint here.
    flask_app.register_blueprint(user_blueprint)
    flask_app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379',
        CELERY_RESULT_BACKEND='redis://localhost:6379'
    )

    celery.conf.update(flask_app.config)

    if __name__ == '__main__':
        flask_app.run()

    return flask_app
