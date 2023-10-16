from src.core.services.services import Servicio, Solicitud
from src.core.database import database as db


# ----------------------- SERVICIOS

def create_service(**kwargs):
    service = Servicio(**kwargs)
    db.session.add(service)
    db.session.commit()

    return service

def list_services():
    services = Servicio.query.all()
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

def delete_solicitud(solicitud):
    db.session.delete(solicitud)
    db.session.commit()