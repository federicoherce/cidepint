from flask import Blueprint, render_template, abort
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)

    users = auth.list_users()
    return render_template("users/index.html", users=users)
