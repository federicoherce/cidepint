from src.web.controllers.auth import auth_bp
from src.web.controllers.users import users_bp
from src.web.controllers.services import services_bp
from src.web.controllers.maintenance import maintenance_bp


def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(maintenance_bp)
