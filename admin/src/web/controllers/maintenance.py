from flask import Blueprint, render_template, redirect, url_for, flash
from src.web.helpers.auth import login_required
from src.web.helpers.maintenance import maintenance
from flask import current_app as app
from forms.maintenance_form import MaintenanceForm
from forms.maintenance_form import ContactoForm
from forms.maintenance_form import paginadoForm
from src.core import configuracion

maintenance_bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")


@maintenance_bp.get('/')
@login_required
@maintenance
def index():
    return render_template('configuraciones/maintenance_form.html', form=MaintenanceForm())


@maintenance_bp.post('/toggle')
@login_required
@maintenance
def toggle_maintenance():
    """
    Está función se ejecuta cuando interactuamos con la configuración de
    mantenimiento dependiendo de si activamos o desactivamos el modo
    mantenimiento. También actualiza el mensaje que se mostrará.
    """
    form = MaintenanceForm()
    if form.validate_on_submit():
        if form.activate_maintenance.data:
            configuracion.update_state(True)
            flash("Se activó modo Mantenimiento: ", "info")
        elif form.deactivate_maintenance.data:
            configuracion.update_state(False)
            flash("Se deactivó modo mantenimiento: ", "info")
        # Ojo que esto puede ejecutar siempre la escritura del mensaje (cambie o no)#arreglado#
        if form.mensaje.data:
            configuracion.update_mensaje(form.mensaje.data)
        return redirect(url_for('maintenance.index'))


@maintenance_bp.get('/contacto')
@login_required
@maintenance
def index_contacto():
    form = ContactoForm()
    return render_template('configuraciones/update_info.html', form=form)


@maintenance_bp.get('/info_contacto')
@login_required
@maintenance
def info_contacto():
    info = configuracion.get_info_contacto()
    return render_template('configuraciones/info_contacto.html', info=info)


@maintenance_bp.post('/update_contacto')
@login_required
@maintenance
def update_contacto():
    flash("Se guardaron los cambios correctamente", "info")
    form = ContactoForm()
    configuracion.update_info(form.telefono.data, form.email.data, form.direccion.data)
    return redirect(url_for('maintenance.index_contacto'))


@maintenance_bp.get('/paginado')
@login_required
@maintenance
def index_paginado():
    form = paginadoForm()
    return render_template('configuraciones/paginado.html', form=form)


@maintenance_bp.post('/update_paginado')
@login_required
@maintenance
def update_paginado():
    flash("Se guardaron los cambios correctamente", "info")
    form = paginadoForm()
    if form.validate_on_submit():
        app.config['PER_PAGE'] = form.per_page.data
        return redirect(url_for('maintenance.index_paginado'))
    return render_template('configuraciones/paginado.html')
