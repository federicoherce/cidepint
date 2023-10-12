from functools import wraps
from flask import session, abort
from src.web.helpers.auth import is_authenticated, has_permissions
from flask import current_app as app


def maintenance(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not has_permissions(['user_maintenance']):
            return abort(401)
        return f(*args, **kwargs)
    return decorated_function

def maintenanceActivated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if app.config['MAINTENANCE_MODE'] :
            return abort(503)
        return f(*args, **kwargs)
    return decorated_function


def isActivated():
    return app.config['MAINTENANCE_MODE']