from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.core import auth
from passlib.hash import sha256_crypt
from src.core import auth

auth_bp = Blueprint("auth",__name__,url_prefix="/sesion")

@auth_bp.get("/")
def login():
    return render_template("auth/login.html")


@auth_bp.post("/authenticate")
def authenticate():
    params = request.form
    user = auth.check_user(params["email"], params["password"])

    if not user:
        flash("Email o clave incorrecta", "error")
        return redirect(url_for("auth.login"))

    session["user_id"] = user.email
    flash("La sesion se inicio correctamente", "succes")

    return redirect(url_for("auth.login"))



@auth_bp.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
        return redirect(url_for('home'))
    else:
        flash("No hay usuario logueado. Por favor, inicia sesión antes de cerrar sesión.", "warning")
        return redirect(url_for('auth.login'))
