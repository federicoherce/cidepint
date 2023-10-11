from flask import Blueprint, render_template, abort,request, redirect, url_for,flash
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions
from src.web.config  import config
from flask import current_app as app


maintenance_bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")


@maintenance_bp.route('/', methods=['GET', 'POST'])
@login_required
def toggle_maintenance():
    if request.method == 'POST':
        if not has_permissions(['user_show']):
               abort(403)  # Acceso prohibido si no es un super admin
        else:       
            action = request.form['action']
            if action == 'Activar Mantenimiento':
                app.config['MAINTENANCE_MODE'] = True
                flash("Se activó modo Mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
            elif action == 'Desactivar mantenimiento':
               app.config['MAINTENANCE_MODE']  = False
               flash("Se deactivó modo mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
    return render_template('maintenance_form.html')
