from flask import Blueprint, render_template, abort, request
from src.core import services
from src.web.helpers.auth import login_required, has_permissions

services_bp = Blueprint("services", __name__, url_prefix="/services")


@services_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)
    servicios = services.list_services()
    return render_template("services/index.html", services=servicios)