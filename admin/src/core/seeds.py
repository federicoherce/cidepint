from src.core import auth
from src.core import users
from src.core import services


def run():
    user = auth.create_User(
        email="juan@admin.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    superadmin_role = users.create_role(nombre="superadmin")

    user_index_permission = users.create_permission(nombre="user_index")
    user_show_permission = users.create_permission(nombre="user_show")
    user_new_permission = users.create_permission(nombre="user_new")
    user_destroy_permission = users.create_permission(nombre="user_destroy")
    user_update_permission = users.create_permission(nombre="user_update")

    users.assign_role_user(user, superadmin_role)
    users.assign_permission_role(superadmin_role, user_index_permission)
    users.assign_permission_role(superadmin_role, user_show_permission)
    users.assign_permission_role(superadmin_role, user_new_permission)
    users.assign_permission_role(superadmin_role, user_destroy_permission)
    users.assign_permission_role(superadmin_role, user_update_permission)
    
    
def run_services():
    services.create_service(
        nombre="Pintura Especializada",
        descripcion="Calidad",
        keywords="pintura, especializada",
        centros="Institucion 1, Institucion 2, Institucion 3",
        tipo_servicio="Desarrollo",
        habilitado=True
    )
    user = auth.create_User(
        email="juan@owner.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    owner = users.create_role(nombre="owner")

    users.assign_role_user(user, owner)
    users.assign_permission_role(owner, users.set_permission("user_index"))
    users.assign_permission_role(owner, users.set_permission("user_new"))
