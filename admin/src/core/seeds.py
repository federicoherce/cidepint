from src.core import auth
from src.core import roles_permissions as rp


def run():
    user = auth.create_User(
        email="juan@admin.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez"
    )

    superadmin_role = rp.create_role(nombre="superadmin")

    user_index_permission = rp.create_permission(nombre="user_index")
    user_show_permission = rp.create_permission(nombre="user_show")
    user_new_permission = rp.create_permission(nombre="user_new")    # Create
    user_destroy_permission = rp.create_permission(nombre="user_destroy")
    user_update_permission = rp.create_permission(nombre="user_update")

    rp.assign_role_user(user, superadmin_role)
    rp.assign_permission_role(superadmin_role, user_index_permission)
    rp.assign_permission_role(superadmin_role, user_show_permission)
    rp.assign_permission_role(superadmin_role, user_new_permission)
    rp.assign_permission_role(superadmin_role, user_destroy_permission)
    rp.assign_permission_role(superadmin_role, user_update_permission)
