from flask import Flask
from flask import render_template
from src.web import error
from src.core import database, seeds
from src.web.config import config

session = Session()

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    app.get("/")

    database.init_app(app)

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