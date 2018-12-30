from functools import wraps
from flask import request, jsonify
from flask import current_app as app


def validator(validator_fns):
    """
    A validator executor function, which executes the list of validator fns.
    :param validator_fns: List of validator functions. Every validator
    function is supposed to return a boolean.
    :return:
    """
    def _validator(f):
        @wraps(f)
        def __validate(*args, **kwargs):
            results = [validation_fn() for validation_fn in validator_fns]
            if False in results:
                app.logger.info('[Validation] Validation failed.')
                return jsonify({'message': 'Validation failed.'})
            return f(*args, **kwargs)
        return __validate
    return _validator
