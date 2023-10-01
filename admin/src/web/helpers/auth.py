from flask import session, abort
from src.core import auth
from src.core import users
from functools import wraps


def is_authenticated(session):
    return session.get("user_id") is not None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function


def has_permissions(required_permissions_list):
    user = auth.find_user_by_mail(session.get("user_id"))
    user_permission_list = users.list_permissions_by_user(user)

    for permission in required_permissions_list:
        if permission in user_permission_list:
            return True
    return False
