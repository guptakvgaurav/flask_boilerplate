from flask import Blueprint, request, jsonify
from flask import current_app as app
from ..common import authenticator, validator
from .validator import get_user_validator
from ..tasks.big_task import do_big_thing

user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/<int:user_id>')
@authenticator('Basic')
@validator([get_user_validator])
def get(user_id):
    """
    A get api which demonstrates the use of decorator chaining in Flask HTTP
    request. You can add as many decorators as you want.
    :param user_id:
    :return: json result.
    """
    # /user/12
    app.logger.info('[User] Start')
    do_big_thing.delay("Heyyyyyyy")
    return jsonify({'id': user_id})


@user_blueprint.route('/search', methods=['GET'])
def search():
    # /user/search?title=woodland&min_price=1000
    app.logger.info('[User] Start')
    return jsonify(request.args)


@user_blueprint.route('/', methods=['POST'])
def post():
    return jsonify(request.get_json())


@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def put(user_id):
    param = request.get_json()
    param.update({'id': user_id})
    return jsonify(param)
