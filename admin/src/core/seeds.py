from src.core import auth
from src.core import users
from src.core import services
from src.core import api
from src.core import instituciones


def run():
    # Creación de usuarios:
    user_superadmin = auth.create_User(
        email="juan@admin.com",
        password="1234",
        token=None,
        nombre="Juan",
        apellido="Perez",
        activo=True
    )

    user_op1 = auth.create_User(
        email="ana@op.com",
        password="1234",
        nombre="Ana",
        apellido="Diaz",
        activo=True
    )

    user_ow1 = auth.create_User(
        email="jose@owner.com",
        password="1234",
        nombre="Jose",
        apellido="Lopez",
        activo=True
    )

    user_admin1 = auth.create_User(
        email="pablo@admin.com",
        password="1234",
        nombre="Pablo",
        apellido="Garcia",
        activo=True
    )

    user_to_delete = auth.create_User(
        email="sacrifice@user.com",
        password="1234",
        nombre="Joe",
        apellido="Doe",
        activo=True
    )

    # Creación de roles:
    superadmin_role = users.create_role(nombre="superadmin")
    owner_role = users.create_role(nombre="owner")
    admin_role = users.create_role(nombre="admin")
    operator_role = users.create_role(nombre="operator")

    # Creación de instituciones:
    superadmin_institution = instituciones.create_institucion(
        nombre="Institucion de Superadministradores",
        informacion="",
        direccion="",
        localizacion="",
        palabras_claves="",
        horarios="",
        web="",
        contacto=""
    )

    cidepint_institution = instituciones.create_institucion(
        nombre="Institucion CIDEPINT",
        informacion="Somos la institución principal",
        direccion="Av. 52 e/ 121 y 122",
        localizacion="La Plata",
        palabras_claves="Pinturas Recubrimientos Investigacion Centro",
        horarios="08:00hs - 20:00hs",
        web="https://cidepint.ing.unlp.edu.ar/",
        contacto="0221 421-6214"
    )

    institucion1 = instituciones.create_institucion(
        nombre="Institución 1",
        informacion="Somos la institución 1",
        direccion="Calle 50 & Av. 120",
        localizacion="La Plata",
        palabras_claves="Software Proyecto",
        horarios="10:00hs - 19:00hs",
        web="https://www.info.unlp.edu.ar/",
        contacto="0221 427-7270"
    )

    # Creación de permisos:
    user_index_permission = users.create_permission(nombre="user_index")
    user_show_permission = users.create_permission(nombre="user_show")
    user_new_permission = users.create_permission(nombre="user_new")
    user_destroy_permission = users.create_permission(nombre="user_destroy")
    user_update_permission = users.create_permission(nombre="user_update")
    admintasks_permission = users.create_permission(nombre="admintasks")
    user_maintenance_permission = users.create_permission(nombre="user_maintenance")

    # users.assign_role_user(user_superadmin, superadmin_role)
    # Asignación de usuarios en una institución con un rol:
    users.assign_role_in_institution_to_user(superadmin_role, superadmin_institution, user_superadmin)
    users.assign_role_in_institution_to_user(admin_role, cidepint_institution, user_admin1)
    users.assign_role_in_institution_to_user(owner_role, cidepint_institution, user_ow1)
    users.assign_role_in_institution_to_user(operator_role, cidepint_institution, user_op1)
    users.assign_role_in_institution_to_user(operator_role, cidepint_institution, user_to_delete)

    # Asignación de permisos y roles:
    users.assign_permission_role(superadmin_role, user_index_permission)
    users.assign_permission_role(superadmin_role, user_show_permission)
    users.assign_permission_role(superadmin_role, user_new_permission)
    users.assign_permission_role(superadmin_role, user_destroy_permission)
    users.assign_permission_role(superadmin_role, user_update_permission)
    users.assign_permission_role(superadmin_role, admintasks_permission)
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
