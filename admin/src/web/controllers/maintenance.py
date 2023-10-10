from flask import Blueprint, render_template, abort,request, redirect, url_for
from src.core import auth
from src.web.helpers.auth import login_required, has_permissions
from src.web.config  import config
from flask import current_app as app


maintenance_bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")


@maintenance_bp.route('/', methods=['GET', 'POST'])
@login_required
def toggle_maintenance():
    if request.method == 'POST':
        if not has_permissions(['user_update']):
               abort(403)  # Acceso prohibido si no es un super admin
        else:       
            action = request.form['action']
            if action == 'Activar Mantenimiento':
                app.config['MAINTENANCE_MODE'] = True
                print("SJSSJJSJSJSJSJJJSJSJS" , app.config['MAINTENANCE_MODE'])
            elif action == 'Desactivar Mantenimiento':
               app.config['MAINTENANCE_MODE']  = False
            return redirect(url_for('maintenance.toggle_maintenance'))  # Redirige para mostrar el estado actualizado
         
    return render_template('maintenance_form.html')
