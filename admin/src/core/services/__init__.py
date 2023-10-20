from src.core.services.services import Servicio, Solicitud
from src.core.api.api_user import ApiUsers
from src.core.database import database as db


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


def update_service(form, service):
    form.populate_obj(service)
    db.session.commit()


def delete_service(id):
    service = Servicio.query.filter_by(id=id).first()
    db.session.delete(service)
    db.session.commit()


def paginate_services_type_and_keywords(tipo, q, page, per_page):
    return Servicio.query.filter(Servicio.tipo_servicio==tipo,
                                 Servicio.habilitado==True,
                                 Servicio.keywords.like(f"%{q}%")).paginate(page=page, per_page=per_page)


def paginate_services_keyword(q, page, per_page):
    return Servicio.query.filter(Servicio.habilitado==True,
                                 Servicio.keywords.like(f"%{q}%")).paginate(page=page, per_page=per_page)


def paginate_services(page, per_page):
    return Servicio.query.paginate(page=page, per_page=per_page)


# ------------------------ SOLICITUDES


def paginate_solicitudes(page, per_page, institucion_id):
    solicitudes = Solicitud.query.join(Solicitud.servicio).filter(Servicio.institucion_id == institucion_id).paginate(page=page, per_page=per_page)
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
        query = query.join(Solicitud.cliente).filter(ApiUsers.username == username)

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


