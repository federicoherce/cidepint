from flask import Blueprint, render_template, abort, request,session
from flask import redirect, url_for, flash
from src.core import auth
from src.core import users
from src.core import instituciones
from src.web.helpers.auth import login_required, has_permissions
from src.web.helpers.auth import login_required, has_permissions, user_is_superadmin
admin_bp = Blueprint("admin", __name__, url_prefix="/administracion")




@admin_bp.get("/")
@login_required
def index():
    if request.args:
        email = request.args.get('email')
        estado = request.args.get('estado')
    else:
        email = ""
        estado = "todos"

    users = get_users(email, estado)
    
    return render_template("admin_insti/buscar_user.html", users=users)

@admin_bp.post("/update_state/<int:user_id>")
@login_required
def update_state(user_id):
    user = auth.get_user_by_id(user_id)
    auth.update_state(user)

    return redirect(url_for("admin.user_profile", user_id=user_id))

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


@admin_bp.get("/profile/<int:user_id>")
@login_required
def user_profile(user_id):
    owner = auth.find_user_by_mail(session["user_id"])
    user = auth.get_user_by_id(user_id)
    is_superadmin = user_is_superadmin(user=user)
    instituciones_del_usuario =  users.get_user_institutions_and_roles(user)

    # Obtengo las instituciones y roles del usuario
    instituciones_roles = users.get_user_institutions_and_roles(owner)


    return render_template(
        "admin_insti/asignar_rol.html",
        user=user,
        user_is_superadmin=is_superadmin,
        instituciones_roles_owner=instituciones_roles,
        instituciones_roles_user = instituciones_del_usuario
        
    )
    
@admin_bp.post("/assign_role_institution/<int:institution_id>/<int:user_id>")
@login_required
def assign_role_institution(institution_id, user_id):
    new_role = get_role_requested(request.form.get("new_role"))
    user = auth.get_user_by_id(user_id)
    institution = instituciones.find_institucion_by_id(institution_id)
    role = users.get_role_by_id(new_role)

    users.assign_role_in_institution_to_user(role, institution, user)
    print(user_id, institution_id, new_role,"PUSO NUEVO ROLLLLLLLLLLLLLLLLL ")
    return redirect(url_for("admin.user_profile", user_id=user_id))


def get_role_requested(new_role):
    if (new_role == "owner"):
        return 2
    elif (new_role == "admin"):
        return 3
    elif (new_role == "operator"):
        return 4
    elif (new_role == "none"):
        return -1


@admin_bp.post("/update_role_institution/<int:institution_id>/<int:user_id>")
@login_required
def update_role_institution(institution_id, user_id):
    """
    Esta función actualiza el rol del usuario en una institución.
    Esta implementación es posible ya que sabemos el id de cada rol (definido por nosotros en la BD)
    """

    new_role = get_role_requested(request.form.get("new_role"))
    if (new_role != -1):
        users.update_role_for_user_in_institution(user_id, institution_id, new_role)
        print(user_id, institution_id, new_role,"AAAAAAAAAAAAAAAAAAAAA")
        print("entrooooooooooooooooooooooooooooooooo")
    else:
        users.delete_role_in_institution_to_user_by_id(institution_id, user_id)
    return redirect(url_for("admin.user_profile", user_id=user_id))

