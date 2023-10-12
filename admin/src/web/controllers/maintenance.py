from flask import Blueprint, render_template, abort,request, redirect, url_for,flash
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions
from src.web.helpers.maintenance import maintenance
from src.web.config  import config
from flask import current_app as app
from forms.maintenance_form import MaintenanceForm

maintenance_bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")


@maintenance_bp.get('/')
@login_required
def index():
    return render_template('maintenance_form.html',form = MaintenanceForm())


#@maintenance_bp.before_request
#@login_required
#def not_has_permissions():
#    if not has_permissions(['user_maintenance']):
#           abort(401)  # Acceso prohibido si no es un super admin



@maintenance_bp.post('/toggle')
@maintenance
def toggle_maintenance():   
    form = MaintenanceForm()
    if form.validate_on_submit():
        if form.activate_maintenance.data:
            app.config['MAINTENANCE_MODE'] = True
            flash("Se activó modo Mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
        elif form.deactivate_maintenance.data:
            app.config['MAINTENANCE_MODE']  = False
            flash("Se deactivó modo mantenimiento: " + str(app.config['MAINTENANCE_MODE']), "info")
        return redirect(url_for('maintenance.index'))