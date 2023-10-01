from src.core import auth


def run():
    user = auth.create_User(
        email="juan@admin.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez"
    )

    superadmin_role = auth.create_role(nombre="superadmin")

    user_index_permission = auth.create_permission(nombre="user_index")
    user_show_permission = auth.create_permission(nombre="user_show")
    user_new_permission = auth.create_permission(nombre="user_new")    # Create
    user_destroy_permission = auth.create_permission(nombre="user_destroy")
    user_update_permission = auth.create_permission(nombre="user_update")

    auth.assign_role_user(user, superadmin_role)
    auth.assign_permission_role(superadmin_role, user_index_permission)
    auth.assign_permission_role(superadmin_role, user_show_permission)
    auth.assign_permission_role(superadmin_role, user_new_permission)
    auth.assign_permission_role(superadmin_role, user_destroy_permission)
    auth.assign_permission_role(superadmin_role, user_update_permission)
