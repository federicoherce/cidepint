from src.core.services.services import Servicio
from src.core.database import database as db


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