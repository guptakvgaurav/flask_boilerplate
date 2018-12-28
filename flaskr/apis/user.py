from flask import Blueprint
from flask import current_app as app
user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/')
def get():
    app.logger.info('[User] Start')
    return "Yo!! user."


