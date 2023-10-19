from flask import Blueprint, render_template,request,session
from flask import redirect, url_for, flash
from src.core import auth
from src.core import users
from src.core import admin_instituciones
from src.forms.admin_institucion_form import adminInstitucionForm
from src.web.helpers.auth import login_required, has_permissions
from flask import current_app as app
from flask import abort


admin_users_bp = Blueprint("admin", __name__, url_prefix="/administracion")

def institutions_of_owner():
    owner = auth.find_user_by_mail(session["user_id"])
    return users.get_user_institutions_by_role(owner.id, 2) 

@admin_users_bp.get("/")
def buscar_usuario():
    if not has_permissions(['owner_index']):
        abort(401)
    inst = institutions_of_owner()
    return render_template("admin_usuarios/buscar.html" , inst=inst)


@admin_users_bp.post("/")
def buscar():
    if not has_permissions(['owner_update']):
        abort(401)
    email = request.form['email']
    institucion_id = request.form['institucion_id']
    if auth.find_user_by_mail(email):
        return redirect(url_for('admin.asignar_rol',institucion_id = institucion_id , email=email))
    else:
        flash("Ese usuario no se encuentra registrado")
        return redirect(url_for('admin.buscar'))


@admin_users_bp.get("/asignar_rol/<int:institucion_id>/<string:email>")
def asignar_rol(institucion_id, email):
    if not has_permissions(['owner_index']):
        abort(401)
    rolActual = ''
    user_id = auth.find_user_by_mail(email).id
    rol_actual_id = users.get_role_in_institution(user_id, institucion_id)
    if rol_actual_id is not None:
        rolActual = users.get_role_by_id(rol_actual_id.role_id).nombre
    return render_template("admin_usuarios/asignar.html" , user_id=user_id, institucion_id=institucion_id, rolActual=rolActual)


@admin_users_bp.post("/asignar_rol_post/<int:institucion_id>/<int:user_id>")
def asignar(institucion_id, user_id):
    """
    se le crea un rol al usuario en la institucion si no posee uno , si ya tiene uno se le actualiza
    y tambien puedes eleiminar el rol del usuario en la institucion
    
    """
    if not has_permissions(['owner_update','owner_create','owner_distroy']):
        abort(401)
    rol = int(request.form['rol']) 
    if users.get_role_in_institution(user_id, institucion_id) is None: 
        users.assign_role_in_institution_to_user_by_id(rol, institucion_id, user_id)   
        flash("Se asigno el rol correctamente") 
    elif (rol == 5): 
        users.delete_role_in_institution_to_user_by_id(institucion_id, user_id)   
        flash("Se ha quitado el rol correctamente")   
    else:
        users.update_role_for_user_in_institution(user_id, institucion_id, rol)     
        flash("Se actualizo el rol correctamente")      
    create_historial(user_id , institucion_id, rol)  
    return redirect(url_for('admin.buscar_usuario'))


def create_historial(user_id , inti_id, rol_id):
    email = auth.find_user_email_by_id(user_id)
    historial  = admin_instituciones.create_historial(
        user_id  = user_id , 
        institucion_id = inti_id, 
        rol_id =  rol_id,
        email = email)
    return historial


@admin_users_bp.get("/ver_historial/<int:institucion_id>")
def ver_historial(institucion_id):
    if not has_permissions(['owner_index']):
        abort(401)
    page = request.args.get('page', type=int, default=1)
    per_page = app.config['PER_PAGE']
    asigns = admin_instituciones.paginate_historial(page,per_page,institucion_id)
    roles = {
        2:"dueño",
        3:"Administrador",
        4:"operador",
    }
    return render_template("admin_usuarios/historial.html",asigns=asigns, roles=roles)


@admin_users_bp.post("/historial")
def historial():
    if not has_permissions(['owner_update']):
        abort(401)
    institucion_id = request.form['institucion_id']
    return redirect(url_for('admin.ver_historial', institucion_id=institucion_id))


@admin_users_bp.get("/select")
def select():
    if not has_permissions(['owner_index']):
        abort(401)
    inst = institutions_of_owner()
    return render_template("admin_usuarios/select.html", list_instituciones=inst)
