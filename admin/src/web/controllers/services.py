from flask import Blueprint, render_template, abort, flash, redirect, url_for, session, request
from src.forms.servicios_form import ServiciosForm
from src.web.helpers.auth import login_required, has_permissions
from src.web.helpers.institutions import user_in_institution
from src.core import services, instituciones
from flask import current_app as app

services_bp = Blueprint("services", __name__, url_prefix="/services")


@services_bp.get("/<int:institucion_id>")
@login_required
@user_in_institution
def index(institucion_id):
    if not has_permissions(['services_index']): 
        abort(401)
    page = request.args.get('page', type=int, default=1)
    per_page = app.config['PER_PAGE']
    paginated_services = services.paginate_services(page, per_page)
    return render_template("services/index.html", services=paginated_services, institucion_id=institucion_id)


@services_bp.get("/agregar/<int:institucion_id>")
@login_required
@user_in_institution
def agregar(institucion_id):
    if not has_permissions(['services_new']):
        abort(401)
    form = ServiciosForm()
    return render_template("services/agregar_servicio.html", form=form, institucion_id=institucion_id)


@services_bp.post("/agregar_servicio/<int:institucion_id>")
@login_required
@user_in_institution
def agregar_servicio(institucion_id):
    form = ServiciosForm()
    if form.validate_on_submit():
        services.create_service(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            keywords=form.keywords.data,
            centros=form.centros.data,
            tipo_servicio=form.tipo_servicio.data,
            habilitado=form.habilitado.data,
            institucion = instituciones.find_institucion_by_id(institucion_id)
        )
        flash('Servicio creado con exito', 'success')
        return redirect(url_for('services.index', institucion_id=institucion_id))
    return render_template("services/agregar_servicio.html", form=form, institucion_id=institucion_id)


@services_bp.get("/editar/<int:servicio_id>/<int:institucion_id>")
@login_required
@user_in_institution
def editar(servicio_id, institucion_id):
    if not has_permissions(['services_update']):
        abort(401)
    servicio = services.get_service(servicio_id)
    form = ServiciosForm(obj=servicio)
    return render_template('services/editar_servicio.html',
                           form=form, servicio=servicio, institucion_id=institucion_id)


@services_bp.post("/editar_servicio/<int:servicio_id>/<int:institucion_id>")
@login_required
@user_in_institution
def editar_servicio(servicio_id, institucion_id):
    servicio = services.get_service(servicio_id)
    form = ServiciosForm()
    if form.validate_on_submit():
        services.update_service(form, servicio)
        flash('Servicio actualizado correctamente', 'success')
        return redirect(url_for("services.index", institucion_id=institucion_id))
    return render_template('services/editar_servicio.html', form=form, institucion_id=institucion_id)


@services_bp.post("/eliminar/<int:servicio_id>/<int:institucion_id>")
@login_required
@user_in_institution
def eliminar(servicio_id, institucion_id):
    if not has_permissions(['services_destroy']):
        abort(401)
    servicio = services.get_service(servicio_id)
    services.delete_service(servicio)
    flash('Servicio eliminado correctamente', 'success')
    return redirect(url_for("services.index", institucion_id=institucion_id))
