from src.core.services.services import Servicio, Solicitud
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


def delete_service(service):
    db.session.delete(service)
    db.session.commit()

# ------------------------ SOLICITUDES


def list_solicitudes():
    solicitudes = Solicitud.query.all()
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
    
def paginate_services(page, per_page):
    return Servicio.query.paginate(page=page, per_page=per_page)
