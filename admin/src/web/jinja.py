from src.web.helpers import auth


def register_jinja_env_globals(app):
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)
    app.jinja_env.globals.update(has_permissions=auth.has_permissions)
    app.jinja_env.globals.update(is_superadmin=auth.is_superadmin)
