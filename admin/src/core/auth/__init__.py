from src.core.auth.user import Users
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
    db.session.commit()
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
    """
    Le añade a un usuario existente una contraseña (codificada)
    """
    user = find_user_by_mail(email)
    hashed_password = sha256_crypt.hash(pw)
    user.password = hashed_password
    db.session.add(user)
    db.session.commit()


def find_user_by_token(token):
    return Users.query.filter_by(token=token).first()


def delete_token(email):
    """
    Cuando el usuario completa su registro, el token se elimina.
    """
    user = find_user_by_mail(email)
    user.token = None
    db.session.add(user)
    db.session.commit()


def find_user_by_mail(email):
    user = Users.query.filter_by(email=email).first()
    return user


def get_user_by_id(id):
    user = Users.query.get_or_404(id)
    return user


def list_users(page, per_page):
    users = Users.query.paginate(page=page, per_page=per_page)
    return users


def find_user_contains_mail(email, page, per_page):
    users = Users.query.filter(Users.email.contains(f'{email}')).paginate(page=page, per_page=per_page)
    return users


def find_user_by_state(state, page, per_page):
    return Users.query.filter(Users.activo == (state == 'activo')).paginate(page=page, per_page=per_page)


def find_user_by_email_and_state(email, state, page, per_page):
    """
    Esta función filtra primero por email y después por el estado (según si se
    busca por activo o bloqueado)
    """
    query = Users.query

    if email:
        query = query.filter(Users.email.contains(email))

    if state == 'activo':
        query = query.filter(Users.activo == True)
    elif state == 'bloqueado':
        query = query.filter(Users.activo == False)

    return query.paginate(page=page, per_page=per_page, error_out=False)


def check_user(email, password):
    """
    Verifica la contraseña ingresada por un usuario
    """
    user = find_user_by_mail(email)

    if user and sha256_crypt.verify(password, user.password):
        return user
    else:
        return None


def update_state(user):
    user.activo = not user.activo
    db.session.commit()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()


def update_name_surname_email(user, name, surname, email):
    user.nombre = name
    user.apellido = surname
    user.email = email
    db.session.commit()

def find_user_contains_mail(email):
    users = Users.query.filter(Users.email.contains(f'{email}'))
    return users

def find_user_email_by_id(id):
    user = Users.query.filter_by(id=id).first()
    return user.email