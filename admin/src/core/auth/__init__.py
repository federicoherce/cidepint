from src.core.auth.user import Users
from src.core.auth.role_permission import Roles, Permissions
from src.core.database import database as db
from passlib.hash import sha256_crypt


def create_User(**kwargs):
    """
    Esta función se ejecuta cuando el usuario
    ingresa vía el enlace envíado en el correo.
    """
    raw_password = kwargs.get("password")
    hashed_password = sha256_crypt.hash(raw_password)
    kwargs["password"] = hashed_password
    user = Users(**kwargs)
    db.session.add(user)
    db.session.commit()       # Efectuamos la query
    return user


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


def find_user_by_token(token):
    return Users.query.filter_by(token=token).first()


def delete_token(email):
    user = find_user_by_mail(email)
    user.token = None
    db.session.add(user)
    db.session.commit()


def list_users():
    users = Users.query.all()
    return users


def find_user_by_mail(email):
    user = Users.query.filter_by(email=email).first()
    return user


def check_user(email, password):
    """
    Verifica la contraseña ingresada por un usuario
    """
    user = find_user_by_mail(email)

    if user and sha256_crypt.verify(password, user.password):
        return user
    else:
        return None


def create_role(**kwargs):
    role = Roles(**kwargs)
    db.session.add(role)
    db.session.commit()

    return role


def assign_role_user(user, role):
    user.roles.append(role)
    role.usuarios.append(user)
    db.session.commit()


def create_permission(**kwargs):
    permission = Permissions(**kwargs)
    db.session.add(permission)
    db.session.commit()

    return permission


def assign_permission_role(role, permission):
    print(permission.nombre)
    print(permission.id)
    role.permisos.append(permission)
    db.session.add(role)
    db.session.commit()
