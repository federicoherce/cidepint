from datetime import datetime, time
from flask import Blueprint, render_template, abort, flash, redirect, url_for
from src.core import services, users, auth, api
from src.forms.servicios_form import ServiciosForm, ActualizarSolicitudesForm, FiltroSolicitudesForm
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


@services_bp.route("/index_solicitudes", methods=['POST', 'GET'])
def index_solicitudes():
    form = FiltroSolicitudesForm()  # Asume que tienes un formulario para el filtrado
    solicitudes = services.list_solicitudes()

    if form.validate_on_submit():
        if form.fecha_inicio.data:
            fecha_inicio = datetime.combine(form.fecha_inicio.data, time.min)
            solicitudes = [solicitud for solicitud in solicitudes if solicitud.fecha_creacion >= fecha_inicio]

        if form.fecha_fin.data:
            fecha_fin = datetime.combine(form.fecha_fin.data, time.min)
            solicitudes = [solicitud for solicitud in solicitudes if solicitud.fecha_creacion <= fecha_fin]

        if form.estado.data:
            solicitudes = [solicitud for solicitud in solicitudes if solicitud.estado == form.estado.data]

        if form.tipo_servicio.data:
            solicitudes = [solicitud for solicitud in solicitudes if solicitud.servicio.tipo_servicio == form.tipo_servicio.data]

        if form.cliente_username.data:
            solicitudes = [solicitud for solicitud in solicitudes if solicitud.cliente.username == form.cliente_username.data]


    return render_template("services/index_solicitudes.html", solicitudes=solicitudes, form=form)


@services_bp.route("/show_solicitud/<int:id>", methods=['POST', 'GET'])
def show_solicitud(id):
    solicitud = services.show_solicitud(id)
    cliente = api.get_user_by_id(solicitud.cliente_id)
    servicio = services.get_service(solicitud.servicio_id)
    return render_template("services/solicitud.html", solicitud=solicitud, cliente=cliente, servicio=servicio)


@services_bp.post("/update_solicitud/<int:id>")
def update_solicitud(id):
    solicitud = services.show_solicitud(id)
    form = ActualizarSolicitudesForm(obj=solicitud)
    form.set_estado_choices(solicitud)

    if form.validate_on_submit():
        if (form.estado.data == solicitud.estado and form.comentario.data != ''):
            services.update_solicitud(solicitud, comentario = form.comentario.data)
        elif (form.comentario.data == ''):
            services.update_solicitud(
                solicitud,
                estado = form.estado.data,
                observacion_cambio_estado = form.observacion_cambio_estado.data,
                fecha_cambio_estado = datetime.utcnow(),
            )
        else:
            services.update_solicitud(
                solicitud,
                estado = form.estado.data,
                observacion_cambio_estado = form.observacion_cambio_estado.data,
                fecha_cambio_estado = datetime.utcnow(),
                comentario = form.comentario.data
            )

        flash('Solicitud actualizada exitosamente', 'success')

        return redirect(url_for('services.show_solicitud', id=solicitud.id))

    return render_template("services/update_solicitud.html", solicitud=solicitud, form=form)


@services_bp.route("/destroy_solicitud/<int:id>", methods=['POST', 'DELETE'])
def destroy_solicitud(id):
    services.delete_solicitud(id)
    flash('Solicitud eliminada exitosamente', 'success')
    return redirect(url_for('services.index_solicitudes'))




