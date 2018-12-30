from functools import wraps
from flask import request, jsonify
from flask import current_app as app


def authenticator(strategy):
    strategy_fn = None

    def basic_authenticator(f):
        @wraps(f)
        def authenticate(*args, **kwargs):
            app.logger.info('In wrapped function')
            username = request.authorization['username']
            password = request.authorization['password']
            is_valid = True if username == password else False
            if not is_valid:
                app.logger.error('[Authentication] [User-{}] tried to access '
                                 '[path-{}] with [password-{}]'
                                 .format(username, request.path, password))
                return jsonify({
                    'message': 'Username and password must be same.'
                })
            return f(*args, **kwargs)
        return authenticate

    if strategy.lower() == 'basic':
        strategy_fn = basic_authenticator

    return strategy_fn
