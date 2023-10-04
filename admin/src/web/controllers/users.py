from flask import Blueprint, render_template, abort, request
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)

    email = request.args.get('email')
    estado = request.args.get('estado')

    users = get_users(email, estado)

    return render_template("users/index.html", users=users)


def get_users(email, estado):
    """
    Este método se encarga de traer los usuarios (se haga o no una búsqueda)
    - Si no se realizó una búsqueda
      - Me traigo a todos
    - Si se realizó una búsqueda por email y estado
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
