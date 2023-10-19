from flask import Blueprint, render_template, session
from src.core import users, auth

home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.get("/")
def index():
    return render_template("home.html")
