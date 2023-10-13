from flask import Blueprint, render_template, abort, request, redirect, url_for, session
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions, is_superadmin

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)

    if request.args:
        email = request.args.get('email')
        estado = request.args.get('estado')
    else:
        email = ""
        estado = "todos"

    users = get_users(email, estado)

    return render_template("users/index.html", users=users)


def get_users(email, estado):
    """
    Este método se encarga de traer los usuarios (se haga o no una búsqueda)
    - Si no se realizó una búsqueda:
      - Me traigo a todos
    - Si se realizó una búsqueda por email y estado:
      - Me traigo a los que contengan el email cuyo estado sea
      igual al recibido
    - Si solo se busca por un criterio, se aplicará solo ese al listado.
    """
    if email == "" and estado == "todos":
        return auth.list_users()

    users = []

    if email != "":
        users.extend(auth.find_user_contains_mail(email))

    if estado != "todos":
        aux = auth.find_user_by_state(estado)  # Menos lecturas
        if email != "":
            users = [u for u in users if u in aux]
        else:
            users.extend(aux)

    return users


@users_bp.get("/profile/<int:user_id>")
@login_required
def user_profile(user_id):
    if not has_permissions(['user_show']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    user_is_superadmin = is_superadmin(user=user)

    return render_template("users/profile.html",
                           user=user,
                           user_is_superadmin=user_is_superadmin)


@users_bp.post("/update_state/<int:user_id>")
@login_required
def update_state(user_id):
    if not has_permissions(['user_update']):
        abort(401)

    user = auth.get_user_by_id(user_id)
    auth.update_state(user)

    return redirect(url_for("users.user_profile", user_id=user_id))
