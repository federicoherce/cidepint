from flask import Flask
from flask import render_template
from src.web import error
from src.core import database, seeds, mail
from src.web.config import config
from flask_session import Session
from src.web.controllers.auth import auth_bp
from src.web.helpers import auth
import logging


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


session = Session()


def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    app.get("/")

    database.init_app(app)
    mail.init_app(app)
    app.register_blueprint(auth_bp)

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    @app.get("/")
    def home():
        return render_template("home.html")

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    app.register_error_handler(404, error.not_found_error)

    return app
