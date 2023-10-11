from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from src.core import instituciones
from src.web.helpers.auth import login_required, has_permissions
from forms.institucion_form import InstitucionForm

instituciones_bp = Blueprint("instituciones", __name__, url_prefix="/instituciones")

@instituciones_bp.route('/instituciones', methods=['GET'])
def list_instituciones():
    instits = instituciones.list_instituciones()
    return render_template("instituciones/list_instituciones.html", instits=instits)


@instituciones_bp.route('/instituciones/<int:id>', methods=['GET'])
def show(id):
    # Lógica para mostrar detalles de una institución específica
    return f'Detalles de la institución {id}'

@instituciones_bp.get("/create")
def create():
    form = InstitucionForm()
    return render_template("instituciones/create_institucion.html", form=form)


@instituciones_bp.post("/create_institucion")
def create_institucion():
    form = InstitucionForm()
    if form.validate_on_submit():
        instituciones.create_institucion(
            nombre=form.nombre.data,
            informacion = form.informacion.data,
            direccion = form.direccion.data,
            localizacion = form.localizacion.data,
            palabras_claves = form.palabras_claves.data,
            horarios = form.horarios.data,
            web = form.web.data,
            contacto = form.contacto.data
        )
        flash('Institucion agregada exitosamente', 'success')
        return redirect(url_for('home'))
    return render_template("instituciones/create_institucion.html", form=form)


@instituciones_bp.route('/instituciones/<int:id>', methods=['PUT'])
def update(id):
    # Lógica para actualizar una institución existente
    return f'Actualizar institución {id}'

@instituciones_bp.route('/instituciones/<int:id>', methods=['DELETE'])
def destroy(id):
    # Lógica para eliminar una institución
    return f'Eliminar institución {id}'

@instituciones_bp.route('/instituciones/<int:id>/activate', methods=['PUT'])
def activate(id):
    # Lógica para activar una institución
    return f'Activar institución {id}'

@instituciones_bp.route('/instituciones/<int:id>/deactivate', methods=['PUT'])
def deactivate(id):
    # Lógica para desactivar una institución
    return f'Desactivar institución {id}'

