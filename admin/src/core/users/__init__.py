from src.core.users.role import Roles, UserRoleInstitution
from src.core.users.permission import Permissions
from src.core.database import database as db


def create_role(**kwargs):
    role = Roles(**kwargs)
    db.session.add(role)
    db.session.commit()

    return role


# Provisoriamente la dejo
def assign_role_user(user, role):
    user.roles.append(role)
    role.usuarios.append(user)
    db.session.commit()


def assign_role_in_institution_to_user(role, institution, user):
    insertion = UserRoleInstitution(user.id, institution.id, role.id)
    db.session.add(insertion)
    db.session.commit()


def create_permission(**kwargs):
    permission = Permissions(**kwargs)
    db.session.add(permission)
    db.session.commit()

    return permission


def assign_permission_role(role, permission):
    role.permisos.append(permission)
    db.session.add(role)
    db.session.commit()


def list_permissions_by_user(user):
    list_permissions = set()
    for role in get_user_roles(user):
        for permission in role.permisos:
            list_permissions.add(permission.nombre)

    return list(list_permissions)


def set_permission(permission):
    return Permissions.query.filter_by(nombre=permission).first()


def get_user_roles(user):
    tuplas = UserRoleInstitution.query.filter_by(user_id=user.id).all()
    roles = set()
    for t in tuplas:
        roles.add(t.role)
    return list(roles)


def get_user_institutions(user):
    tuplas = UserRoleInstitution.query.filter_by(user_id=user.id).all()
    institutions = set()
    for t in tuplas:
        institutions.add(t.institution)
    return list(institutions)


def update_role_for_user_in_institution(user_id, institution_id, new_role_id):
    user_institution_relationship = UserRoleInstitution.query.filter_by(
        user_id=user_id, institution_id=institution_id
    ).first()
    user_institution_relationship.role_id = new_role_id
    db.session.add(user_institution_relationship)
    db.session.commit()


def cascade_delete_user(user_id):
    UserRoleInstitution.query.filter_by(user_id=user_id).delete()
    db.session.commit()
