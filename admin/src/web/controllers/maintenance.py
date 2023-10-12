from flask import Blueprint, render_template, abort,request, redirect, url_for,flash
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions
from src.web.config  import config
from flask import current_app as app


maintenance_bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")


@maintenance_bp.get('/')
def index():
    return render_template('maintenance_form.html')


@maintenance_bp.before_request
@login_required
def not_has_permissions():
    if not has_permissions(['user_show']):
           abort(401)  # Acceso prohibido si no es un super admin



@maintenance_bp.post('/toggle')
def toggle_maintenance():   
    action = request.form['action']
    if action == 'Activar Mantenimiento':
        app.config['MAINTENANCE_MODE'] = True
        flash("Se activó modo Mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
    elif action == 'Desactivar Mantenimiento':
       app.config['MAINTENANCE_MODE']  = False
       flash("Se deactivó modo mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
    return redirect(url_for('maintenance.index'))
