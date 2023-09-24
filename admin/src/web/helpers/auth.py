from flask import session, abort
from functools import wraps

def is_authenticated(session):
    return session.get("user_id") is not None

