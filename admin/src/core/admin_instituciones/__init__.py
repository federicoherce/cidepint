from src.core.database import database as db
from src.core.admin_instituciones.historial import Historial


def create_historial(**kwargs):
    historial = Historial(**kwargs)
    db.session.add(historial)
    db.session.commit()

    return historial
