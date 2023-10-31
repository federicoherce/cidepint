from flask import Flask
from src.core import database, mail
from src.web.config import config, cache
from src.web import routes
from src.web import commands
from src.web import error_handlers
from src.web import jinja
from flask_caching import Cache
import logging
from flask_jwt_extended import JWTManager
from datetime import timedelta

#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    
    jwt = JWTManager(app)
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    
    database.init_app(app)
    mail.init_app(app)
    routes.register_routes(app)
    commands.register_commands(app)
    error_handlers.register_errors(app)
    jinja.register_jinja_env_globals(app)
    cache.init_app(app)

    return app
