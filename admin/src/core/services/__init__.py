from src.core.services.services import Servicio, Solicitud
from src.core.api.api_user import ApiUsers
from src.core.database import database as db
from src.core.auth.user import Users
from src.core.instituciones.institucion import Institucion

def create_service(**kwargs):
    service = Servicio(**kwargs)
    db.session.add(service)
    db.session.commit()

    return service


def list_services(id):
    services = Servicio.query.filter_by(institucion_id=id).all()
    return services


def get_service(id):
    service = Servicio.query.filter_by(id=id).first()
    return service

def get_all_services():
    return Servicio.query.all()

def update_service(form, service):
    form.populate_obj(service)
    db.session.commit()


def delete_service(id):
    service = Servicio.query.filter_by(id=id).first()
    db.session.delete(service)
    db.session.commit()


def paginate_services(page, per_page, institucion_id):
    return Servicio.query.filter_by(institucion_id=institucion_id).paginate(page=page, per_page=per_page)


def paginate_services_api(page, per_page):
    return Servicio.query.paginate(page=page, per_page=per_page)


def search_services_api(**kwargs):
    query = Servicio.query

    if 'nombre' in kwargs and kwargs['nombre']:
        query = query.filter(Servicio.nombre.ilike(f"%{kwargs['nombre']}"))
    if 'descripcion' in kwargs and kwargs['descripcion']:
        query = query.filter(Servicio.descripcion.ilike(f"%{kwargs['descripcion']}"))
    if 'institucion' in kwargs and kwargs['institucion']:
        query = query.join(Servicio.institucion).filter(Institucion.nombre.ilike(f"%{kwargs['institucion']}"))
    if 'tipo_servicio' in kwargs and kwargs['tipo_servicio']:
        query = query.filter(Servicio.tipo_servicio == kwargs['tipo_servicio'])
    if 'keywords' in kwargs and kwargs['keywords']:
        query = query.filter(Servicio.keywords.ilike(f"%{kwargs['keywords']}"))
    
    return query.paginate(page=kwargs['page'], per_page=kwargs['per_page'])

# ------------------------ SOLICITUDES


def paginate_solicitudes(page, per_page, institucion_id):
    solicitudes = Solicitud.query.join(Solicitud.servicio).filter(Servicio.institucion_id == institucion_id).paginate(page=page, per_page=per_page)

    return solicitudes


def paginate_solicitudes_api(page, per_page):
    solicitudes = Solicitud.query.join(Solicitud.servicio).paginate(page=page, per_page=per_page)

    return solicitudes


def paginate_solicitudes_api_id(page, per_page,id):
    solicitudes = Solicitud.query.filter( Solicitud.cliente_id == id).paginate(page=page, per_page=per_page)
    return solicitudes


def solicitudes_api_id(cliente_id, solicitud_id):
    """
    Este metodo devuelve una solicitud que pertenezca al cliente_id
    y que tenga el id de solicitud_id
    """
    solicitudes = Solicitud.query.filter(Solicitud.cliente_id == cliente_id, Solicitud.id == solicitud_id).first()
    return solicitudes


def paginate_solicitudes_filtradas(page, per_page, inicio, fin, estado, tipo, username, institucion_id):
    """
    Este metodo recibe los filtros a aplicar en las solicitudes
    y, valga la redundancia, aplica aquellos que se hayan enviado.
    Luego pagina los resultados y los devuelve
    """
    query = Solicitud.query
    query = query.join(Solicitud.servicio).filter(Servicio.institucion_id == institucion_id)

    if inicio:
        query = query.filter(Solicitud.fecha_creacion > inicio)

    if fin:
        query = query.filter(Solicitud.fecha_creacion < fin)

    if estado:
        query = query.filter(Solicitud.estado == estado)

    if tipo:
        query = query.join(Solicitud.servicio).filter(Servicio.tipo_servicio == tipo)

    if username:
        query = query.join(Solicitud.cliente).filter(Users.nombre == username)

    # Ejecuta la consulta y obtén los resultados
    solicitudes = query.paginate(page=page, per_page=per_page)

    return solicitudes


def show_solicitud(id):
    solicitud = Solicitud.query.filter_by(id=id).first()
    return solicitud


def update_solicitud(solicitud, **kwargs):
    for key, value in kwargs.items():
        if hasattr(solicitud, key):
            setattr(solicitud, key, value)
    db.session.commit()


def delete_solicitud(id):
    solicitud = Solicitud.query.filter_by(id=id).first()
    db.session.delete(solicitud)
    db.session.commit()


def create_solicitud(**kwargs):
    solicitud = Solicitud(**kwargs)
    db.session.add(solicitud)
    db.session.commit()
    return solicitud


def get_top_institutions():
    subquery = (
        db.session.query(
            Servicio.institucion_id,
            db.func.sum(Solicitud.updated_at - Solicitud.inserted_at).label("tiempo_resolucion")
        )
        .join(Solicitud, Servicio.id == Solicitud.servicio_id)
        .filter(Solicitud.estado.like('FINALIZADA'))
        .group_by(Servicio.institucion_id)
        .subquery()
    )

    query = (
        db.session.query(Institucion)
        .join(subquery, subquery.c.institucion_id == Institucion.id)
        .order_by(subquery.c.tiempo_resolucion.desc())
        .limit(10)
    )

    return query.all()
