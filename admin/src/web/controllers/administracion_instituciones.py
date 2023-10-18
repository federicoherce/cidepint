from flask import Blueprint, render_template, abort, request,session
from flask import redirect, url_for, flash
from src.core import auth
from src.core import users
from src.core import instituciones
from src.web.helpers.auth import login_required, has_permissions
from src.web.helpers.auth import login_required, has_permissions, user_is_superadmin
from src.core import admin_instituciones

admin_bp = Blueprint("admin", __name__, url_prefix="/administracion")




@admin_bp.get("/")
@login_required
def index():
    if not has_permissions(['owner_index']):
        abort(401)
    if request.args:
        email = request.args.get('email')
        estado = request.args.get('estado')
    else:
        email = ""
        estado = "todos"

    users = get_users(email, estado)
    
    return render_template("admin_insti/buscar_user.html", users=users)


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
    if not has_permissions(['owner_show']):
        abort(401)
        
    owner = auth.find_user_by_mail(session["user_id"])
    user = auth.get_user_by_id(user_id)
    is_superadmin = user_is_superadmin(user=user)
    instituciones_roles = users.get_user_institutions_and_roles(owner)

    return render_template(
        "admin_insti/asignar_rol.html",
        user=user,
        user_is_superadmin=is_superadmin,
        instituciones_roles_owner=instituciones_roles,
        
    )
 

def assign_role_institution(institution_id, user_id,new_role):
    if not has_permissions(['owner_update']):
        abort(401)
    user = auth.get_user_by_id(user_id)
    institution = instituciones.find_institucion_by_id(institution_id)
    role = users.get_role_by_id(new_role)

    users.assign_role_in_institution_to_user(role, institution, user)
    

    create_historial(user_id ,institution_id,new_role) #guardo el el historial de asignaciones 
     
    print(user_id, institution_id, new_role,"PUSO NUEVO ROLLLLLLLLLLLLLLLLL ")


def get_role_requested(new_role):
    if (new_role == "owner"):
        return 2
    elif (new_role == "admin"):
        return 3
    elif (new_role == "operator"):
        return 4
    elif (new_role == "none"):
        return -1


def update_role_institution(institution_id, user_id,new_role):
    """
    Esta función actualiza el rol del usuario en una institución.
    Esta implementación es posible ya que sabemos el id de cada rol (definido por nosotros en la BD)
    """
    if not has_permissions(['owner_update']):
        abort(401)

    
    if (new_role != -1):
        users.update_role_for_user_in_institution(user_id, institution_id, new_role)
        
    else:
        users.delete_role_in_institution_to_user_by_id(institution_id, user_id)
        
    create_historial(user_id ,institution_id,new_role)  #guardo el el historial de asignaciones   




def create_historial(user_id , inti_id, rol_id):
    email = auth.find_user_email_by_id(user_id)
    historial  = admin_instituciones.create_historial(
        user_id  = user_id , 
        institucion_id = inti_id, 
        rol_id =  rol_id,
        email = email)
    return historial

    
@admin_bp.post("/update_role_institution/<int:institution_id>/<int:user_id>")
def update_or_assign_rol(institution_id, user_id):
    """
    Si tiene rol, lo actualiza; de lo contrario, lo asigna.
    """
    new_role = get_role_requested(request.form.get("new_role"))


    if users.roles_in_institution(user_id, institution_id):
        update_role_institution(institution_id, user_id, new_role)
        print("ACTUALIZAAAAAAAAAAAAAAAA")
    else:
        assign_role_institution(institution_id, user_id,new_role)
        print("ASIGNAAAAAAAAAAAAAA")

    return redirect(url_for("admin.user_profile", user_id=user_id))
