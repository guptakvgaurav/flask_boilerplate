from flask import Blueprint, request, jsonify
from flask import current_app as app
user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/<int:id>')
def get(id):
    # /user/12
    app.logger.info('[User] Start')
    return jsonify({'id': id})


@user_blueprint.route('/search', methods=['GET'])
def search():
    # /user/search?title=woodland&min_price=1000
    app.logger.info('[User] Start')
    return jsonify(request.args)


@user_blueprint.route('/', methods=['POST'])
def post():
    return jsonify(request.get_json())


@user_blueprint.route('/<int:id>', methods=['PUT'])
def put(id):
    param = request.get_json()
    param.update({'id': id})
    return jsonify(param)
