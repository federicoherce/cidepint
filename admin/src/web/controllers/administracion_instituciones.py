from flask import Blueprint, render_template,request,session
from flask import redirect, url_for, flash
from src.core import auth
from src.core import users
from src.core import instituciones
from src.core import admin_instituciones
from src.forms.admin_institucion_form import adminInstitucionForm


admin_users_bp = Blueprint("admin", __name__, url_prefix="/administracion")


@admin_users_bp.get("/")
def buscar_usuario():
    owner = auth.find_user_by_mail(session["user_id"])
    institutions_ids = users.get_institutios_of_user_by_role(owner.id, 2)
    inst_of_owner = instituciones.get_institutions_by_id(institutions_ids)

    return render_template("admin_usuarios/buscar.html" , instituciones=inst_of_owner)


@admin_users_bp.post("/")
def buscar():
    email = request.form['email']
    institucion_id = request.form['institucion_id']
    if auth.find_user_by_mail(email):
        return redirect(url_for('admin.asignar_rol',institucion_id = institucion_id , email = email))
    else:
        flash("Ese usuario no se encuentra registrado")
        return redirect(url_for('admin.buscar'))


@admin_users_bp.get("/asignar_rol/<int:institucion_id>/<string:email>")
def asignar_rol(institucion_id, email):
    rolActual = ''
    user_id = auth.find_user_by_mail(email).id
    rol_actual_id = users.get_role_in_institution(user_id, institucion_id)
    if rol_actual_id is not None:
        rolActual = users.get_role_by_id(rol_actual_id.role_id).nombre
    return render_template("admin_usuarios/asignar.html" , user_id=user_id, institucion_id=institucion_id, rolActual=rolActual)


@admin_users_bp.post("/asignar_rol_post/<int:institucion_id>/<int:user_id>")
def asignar(institucion_id, user_id):
    rol = int(request.form['rol']) 
    if users.get_role_in_institution(user_id, institucion_id) is None: 
        users.assign_role_in_institution_to_user_by_id(rol, institucion_id, user_id)   
    else:
        users.update_role_for_user_in_institution(user_id, institucion_id, rol)     
          
    #create_historial(user_id , institucion_id, rol)  
    return redirect(url_for('admin.buscar_usuario'))


def create_historial(user_id , inti_id, rol_id):
    email = auth.find_user_email_by_id(user_id)
    historial  = admin_instituciones.create_historial(
        user_id  = user_id , 
        institucion_id = inti_id, 
        rol_id =  rol_id,
        email = email)
    return historial



