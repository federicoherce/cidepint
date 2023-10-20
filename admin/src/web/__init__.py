from flask import Flask
from flask import render_template
from src.core import database, mail
from src.web.config import config
from src.web import routes
from src.web import commands
from src.web import error_handlers
from src.web import jinja
from flask_caching import Cache
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    cache = Cache(app, config={"CACHE_TYPE": "simple"})

    database.init_app(app)
    mail.init_app(app)
    routes.register_routes(app)
    commands.register_commands(app)
    error_handlers.register_errors(app)
    jinja.register_jinja_env_globals(app)

    return app
