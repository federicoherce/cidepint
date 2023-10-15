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
        services.create_service(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            keywords=form.keywords.data,
            centros=form.centros.data,
            tipo_servicio=form.tipo_servicio.data,
            habilitado=form.habilitado.data
        )
        flash('Servicio creado con exito', 'success')
        return redirect(url_for('services.index'))
    return render_template("services/agregar_servicio.html", form=form)


@services_bp.get("/editar/<int:servicio_id>")
@login_required
def editar(servicio_id):
    if not has_permissions(['user_update']):
        abort(401)
    servicio = services.get_service(servicio_id)
    form = ServiciosForm(obj=servicio)
    return render_template('services/editar_servicio.html',
                           form=form, servicio=servicio)


@services_bp.post("/editar_servicio/<int:servicio_id>")
@login_required
def editar_servicio(servicio_id):
    servicio = services.get_service(servicio_id)
    form = ServiciosForm()
    if form.validate_on_submit():
        services.update_service(form, servicio)
        flash('Servicio actualizado correctamente', 'success')
        return redirect(url_for("services.index"))
    return render_template('services/editar_servicio.html', form=form)


@services_bp.post("/eliminar/<int:servicio_id>")
@login_required
def eliminar(servicio_id):
    if not has_permissions(['user_destroy']):
        abort(401)
    servicio = services.get_service(servicio_id)
    services.delete_service(servicio)
    flash('Servicio eliminado correctamente', 'success')
    return redirect(url_for("services.index"))
