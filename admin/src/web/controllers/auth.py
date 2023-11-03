from flask import Blueprint, render_template
from flask import redirect, url_for, flash, session, abort, request
from flask_oauthlib.client import OAuth
from src.core import auth
from src.core import users
from forms.registro_form import SignUpForm, PasswordForm
from flask_mail import Message
from core.mail import mail
import secrets
from src.web.helpers.auth import has_permissions_mail, user_is_superadmin
from flask import current_app
from src.web.helpers.maintenance import maintenanceActivated
from src.core import configuracion
from flask_jwt_extended import create_access_token, set_access_cookies,unset_jwt_cookies,jwt_required
from flask import jsonify
from src.core import api

auth_bp = Blueprint("auth", __name__, url_prefix="/sesion")


@auth_bp.get("/")
def login():
    return render_template("auth/login.html")

@auth_bp.post('/login_jwt')
def login_jwt():
  data = request.get_json()
  email = data['email']
  password = data['password']
  user = api.check_user(email, password)
  if user:
    access_token = create_access_token(identity=user.id,fresh=True)
    response = jsonify({'token':access_token})
    set_access_cookies(response, access_token)
    return response, 201
  else:
    return jsonify(message="debe registrarse antes de hacer el login"), 401


@auth_bp.get('/logout_jwt')
@jwt_required()
def logout_jwt():
  response = jsonify(message="Logged out successfully")
  unset_jwt_cookies(response)
  return response, 200

@auth_bp.post("/authenticate")
def authenticate():
    """
    Esta función verifica las credenciales ingresadas.
    - Si el modo mantenimiento está activado y el usuario no cuenta con
    los permisos -> 503
    - Si el usuario está bloqueado -> 403
    - Sino, se crea la sesión con el mail del usuario, sus permisos y si es
    superadmin (solo lo usamos para las vistas).
    """
    params = request.form
    user = auth.check_user(params["email"], params["password"])

    if not user:
        flash("Email o clave incorrecta", "error")
        return redirect(url_for("auth.login"))

    if configuracion.get_state() and not has_permissions_mail(['config_show'], user.email):
        return abort(503)
    elif not user.activo:
        return abort(403)
    else:
        session["user_id"] = user.email
        session["is_superadmin"] = user_is_superadmin(user)
        session["permissions"] = users.list_permissions_by_user(user)
        flash("La sesion se inicio correctamente", "success")

    return redirect(url_for("home.index"))



@auth_bp.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
        return redirect(url_for('home.index'))
    else:
        flash("No hay usuario logueado. Por favor, inicia sesión antes de cerrar sesión.", "warning")
        return redirect(url_for('auth.login'))


def generate_confirmation_token():
    token = secrets.token_urlsafe(16)
    return token


@auth_bp.get("/register")
@maintenanceActivated
def register():
    form = SignUpForm()
    return render_template("auth/register.html", form=form)


@auth_bp.post("/register_user")
@maintenanceActivated
def register_user():
    """
    Ésta función registra al usuario, verifica que el mail ingresado no se
    repita, crea un token que servirá hasta que el usuario termine su registro
    y envía un correo al mail ingresado para que continue con el registro.
    """
    form = SignUpForm()
    if form.validate_on_submit():
        existe = auth.find_user_by_mail(form.email.data)
        if existe:
            flash('Este correo electrónico ya está en uso. Por favor, elige otro.', 'error')
            return redirect(url_for('auth.register'))

        token = generate_confirmation_token()
        auth.create_user_no_pw(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            email=form.email.data,
            token=token
        )
        send_confirmation_email(form.email.data, token)
        flash('Tu cuenta ha sido creada, te enviamos un mail', 'success')
        return redirect(url_for('home.index'))
    return render_template("auth/register.html", form=form)


def send_confirmation_email(email, token):
    """
    Este metodo envia un email al usuario registrado para que 
    confirme su registro, y enviará una url distinta si el sitio
    se encuentra corriendo en Producción o Desarrollo
    """
    msg = Message(
        'Confirma tu registro',
        sender='cidepint.proyecto@gmail.com',
        recipients=[email])
    url = current_app.config['URL_REGISTRO']
    confirmation_link = f'{url}/{email}/{token}'
    msg.html = f"""
                Para confirmar tu registro, haz clic en el siguiente enlace:
                <a href="{confirmation_link}">Confirmar Registro</a>'
                """
    mail.send(msg)


@auth_bp.get("/confirmar_registro/<email>/<token>")
def confirm_registration(email, token):
    user = auth.find_user_by_token(token)
    if user:
        form = PasswordForm()
        return render_template(
            'auth/confirmar_registro.html',
            form=form,
            email=email,
            token=token
        )
    else:
        abort(404)


@auth_bp.post("/guardar_contrasenia/<email>/<token>")
def save_password(email, token):
    form = PasswordForm()
    auth.enter_password(form.password.data, email)
    auth.delete_token(email)
    flash('Contraseña seteada con exito', 'success')
    return redirect(url_for('home.index'))


@auth_bp.get("/google")
def google():
    print(f"FFFFFASDASDSAD {current_app.extensions['oauthlib.client'].google}")
    return current_app.extensions['oauthlib.client'].google.authorize(
        callback=url_for('auth.google_authorization', _external=True)
    )


@auth_bp.route("/google/authorization")
def google_authorization():
    response = current_app.extensions['oauthlib.client'].google.authorized_response()
    if response is None or response.get('access_token') is None:
        abort(401)

    print(response)
    session['google_token'] = (response['access_token'], '')
    google_user = current_app.extensions['oauthlib.client'].google.get('userinfo')
    user_info = google_user.data

    user_email = user_info['email']
    user_name = user_info.get('name')
    user_lastname = user_info.get('family_name')

    existe = auth.find_user_by_mail(user_email)
    if existe:
        flash('Esta cuenta ya fue registrada anteriormente.', 'error')
        return redirect(url_for('auth.register'))

    token = generate_confirmation_token()

    auth.create_user_no_pw(
        nombre=user_name,
        apellido=user_lastname,
        email=user_email,
        token=token
    )

    send_confirmation_email(user_email, token)
    flash('Tu cuenta ha sido creada, te enviamos un mail', 'success')
    return redirect(url_for('home.index'))
