from flask import Flask
from flask import render_template
from src.core import database, mail
from src.web.config import config
from src.web.helpers import auth
import logging
from src.web import routes
from src.web import commands
from src.web import error_handlers
from flask import session, abort
from src.web.helpers.auth import has_permissions

#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    app.get("/")
    
    @app.get("/")
    def home():
        return render_template("home.html")
    
    database.init_app(app)
    mail.init_app(app)
    routes.register_routes(app)
    commands.register_commands(app)
    error_handlers.register_errors(app)
    @app.before_request
    def check_maintenance_mode():
        print("MODO EN EL INIT???!!!!!!!@@@@??" ,app.config['MAINTENANCE_MODE'])
        if app.config['MAINTENANCE_MODE'] and (not session.get("user_id") or not has_permissions(['user_index'])):
            return abort(503) 
        
    @app.errorhandler(503)
    def error_503(error):
        return render_template("maintenance.html")
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    return app
