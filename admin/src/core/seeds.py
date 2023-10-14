from src.core import auth
from src.core import users
from src.core import services
from src.core import api

def run():
    # Creación de usuarios:
    user = auth.create_User(
        email="juan@admin.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    # Creación de roles:
    superadmin_role = users.create_role(nombre="superadmin")

    # Creación de permisos:
    user_index_permission = users.create_permission(nombre="user_index")
    user_show_permission = users.create_permission(nombre="user_show")
    user_new_permission = users.create_permission(nombre="user_new")
    user_destroy_permission = users.create_permission(nombre="user_destroy")
    user_update_permission = users.create_permission(nombre="user_update")
    user_maintenance_permission = users.create_permission(nombre="user_maintenance")

    users.assign_role_user(user, superadmin_role)

    # Asignación de permisos y roles:
    users.assign_permission_role(superadmin_role, user_index_permission)
    users.assign_permission_role(superadmin_role, user_show_permission)
    users.assign_permission_role(superadmin_role, user_new_permission)
    users.assign_permission_role(superadmin_role, user_destroy_permission)
    users.assign_permission_role(superadmin_role, user_update_permission)
    users.assign_permission_role(superadmin_role, user_maintenance_permission)


def run_services():
    user = auth.create_User(
        email="juan@owner.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    op = auth.create_User(
        email="juan@operator.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    owner = users.create_role(nombre="owner")
    operator = users.create_role(nombre="operator")

    users.assign_role_user(user, owner)
    users.assign_permission_role(owner, users.set_permission("user_index"))
    users.assign_permission_role(owner, users.set_permission("user_new"))
    users.assign_permission_role(owner, users.set_permission("user_update"))
    users.assign_permission_role(owner, users.set_permission("user_destroy"))

    users.assign_role_user(op, operator)
    users.assign_permission_role(operator, users.set_permission("user_index"))
    users.assign_permission_role(operator, users.set_permission("user_new"))
    users.assign_permission_role(operator, users.set_permission("user_update"))

def run_api():
    api.create_user(
        username="fedeherce",
        tipo_documento="DNI",
        nro_documento="42708561",
        direccion="10 y 60",
        telefono='2920687309',
        email="fede@gmail.com",
        password="1234"
    )
    
