from flask import Flask
def create_app():
    app = Flask(__name__)
    app.get("/")

    @app.get("/")
    def home():
        return "Hola Mundo!"

    return app