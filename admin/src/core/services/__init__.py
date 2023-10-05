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