from flask import Blueprint, render_template, abort, flash, redirect, url_for
from src.core import services
from src.forms.servicios_form import ServiciosForm
from src.web.helpers.auth import login_required, has_permissions

services_bp = Blueprint("services", __name__, url_prefix="/services")


@services_bp.get("/")
@login_required
def index():
    if not has_permissions(['user_index']):
        abort(401)
    servicios = services.list_services()
    return render_template("services/index.html", services=servicios)

@services_bp.get("/agregar")
@login_required
def agregar():
    if not has_permissions(['user_new']):
        abort(401)
    form = ServiciosForm()
    return render_template("services/agregar_servicio.html", form=form)

@services_bp.post("/agregar_servicio")
@login_required
def agregar_servicio():
    form = ServiciosForm()
    if form.validate_on_submit():
        servicio = services.create_service(
            nombre = form.nombre.data,
            descripcion = form.descripcion.data,
            keywords = form.keywords.data, 
            centros = form.centros.data, 
            tipo_servicio = form.tipo_servicio.data,
            habilitado = form.habilitado.data
        )
        flash('Servicio creado con exito', 'success')
        return redirect(url_for('services.index'))
    return render_template("services/agregar_servicio.html", form=form)
