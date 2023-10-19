from src.core.instituciones.institucion import Institucion
from src.core.database import database as db


def create_institucion(**kwargs):
    institucion = Institucion(**kwargs)
    db.session.add(institucion)
    db.session.commit()      # Efectuamos la query
    return institucion


def delete_institucion(id):
    institucion = Institucion.query.filter_by(id=id).first()
    db.session.delete(institucion)
    db.session.commit()


def find_institucion_by_id(id):
    return Institucion.query.filter_by(id=id).first()


def update_institucion(institucion, **kwargs):
    for key, value in kwargs.items():
        if hasattr(institucion, key):
            setattr(institucion, key, value)
    db.session.commit()


def habilitar_institucion(institucion, value):
    setattr(institucion, 'habilitado', value)
    db.session.commit()


def list_instituciones():
    instituciones = Institucion.query.filter(id!=1).all()
    return instituciones


def paginate_instituciones(page, per_page):
    return Institucion.query.filter(Institucion.id != 1).paginate(page=page, per_page=per_page)


def paginate_institutions_habilited(page, per_page):
    """
    Retorna todas las instituciones habilitadas de manera paginada
    """
    return Institucion.query.filter(Institucion.id != 1, Institucion.habilitado == True).paginate(page=page, per_page=per_page)