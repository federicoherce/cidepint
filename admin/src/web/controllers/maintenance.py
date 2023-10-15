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
@maintenance
def index():
    return render_template('maintenance_form.html',form = MaintenanceForm())




@maintenance_bp.post('/toggle')
@login_required
def toggle_maintenance():   
    form = MaintenanceForm()
    if form.validate_on_submit():
        if form.activate_maintenance.data:
            app.config['MAINTENANCE_MODE'] = True
            flash("Se activó modo Mantenimiento: ", "info")
        elif form.deactivate_maintenance.data:
            app.config['MAINTENANCE_MODE']  = False
            flash("Se deactivó modo mantenimiento: ", "info")
        return redirect(url_for('maintenance.index'))