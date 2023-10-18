from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.core import auth


admin_users_bp = Blueprint("admin_users", __name__, url_prefix="/admin_users")


@admin_users_bp.get("/")
def buscar_usuario():
    return render_template("admin_usuarios/buscar.html")


@admin_users_bp.post("/")
def buscar():
    email = request.form['email']
    if auth.find_user_by_mail(email):
        return redirect(url_for('admin_users.asignar_rol'))
    else:
        flash("Ese usuario no se encuentra registrado")
        return redirect(url_for('admin_users.buscar'))

@admin_users_bp.get("/asignar_rol")
def asignar_rol():
    return render_template("admin_usuarios/asignar.html")
