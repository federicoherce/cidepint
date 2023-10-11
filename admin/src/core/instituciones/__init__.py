from src.core.instituciones.institucion import Institucion
from src.core.database import database as db


def create_institucion(**kwargs):
    institucion = Institucion(**kwargs)
    db.session.add(institucion)
    db.session.commit()      # Efectuamos la query
    return institucion


def create_user_no_pw(**kwargs):
    """
    Esta función se ejecuta cuando el usuario
    hace la primera parte del registro.
    """
    user = Users(**kwargs)
    db.session.add(user)
    db.session.commit()


def enter_password(pw, email):
    user = find_user_by_mail(email)
    hashed_password = sha256_crypt.hash(pw)
    user.password = hashed_password
    db.session.add(user)
    db.session.commit()


def find_institucion_by_id(id):
    return Institucion.query.filter_by(id=id).first()


def update_institucion(institucion, **kwargs):
    for key, value in kwargs.items():
        if hasattr(institucion, key):
            setattr(institucion, key, value)
    db.session.commit()




def list_instituciones():
    instituciones = Institucion.query.all()
    return instituciones



