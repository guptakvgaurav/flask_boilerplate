from flask import request


def get_user_validator():
    """
    A validator function, which returns True if validation succeeds
    otherwise False.
    :return:
    """
    value = request.view_args.get('user_id')
    return True if isinstance(value, int) else False
