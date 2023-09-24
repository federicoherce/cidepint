from src.core.auth.user import Users
from src.core.database import database as db
from passlib.hash import sha256_crypt



def create_User(**kwargs):
    """
    hashea la contraseña y crear el usuario
    """
    raw_password = kwargs.get("password")
    hashed_password = sha256_crypt.hash(raw_password)
    kwargs["password"] = hashed_password 
    user = Users(**kwargs)
    db.session.add(user)
    db.session.commit()       # Efectuamos la query 
    return user 


def list_users():
    users = Users.query.all()
    return users

def find_user_by_email_and_password(email):
	user = Users.query.filter_by(email=email).first()
	return user



def check_user(email, password):
    user = find_user_by_email_and_password(email)
    
    if user and sha256_crypt.verify(password, user.password):
        return user
    else:
        return None