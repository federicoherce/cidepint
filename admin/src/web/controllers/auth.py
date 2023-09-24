from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.core import auth
from passlib.hash import sha256_crypt
from src.core import auth

auth_bp = Blueprint("users",__name__,url_prefix="/sesion")



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        params = request.form
        user = auth.check_user(params.get("email"), params.get("password"))
        if(user):
            session['user_id'] = user.id
            flash("Se a iniciado session correctamente.", "warning")
            return redirect(url_for('users.login'))
        else:
            return 'Credenciales incorrectas'
    return render_template('auth/login.html')



@auth_bp.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
        return redirect(url_for('home'))
    else:
        flash("No hay usuario logueado. Por favor, inicia sesión antes de cerrar sesión.", "warning")
        return redirect(url_for('users.login'))
