from flask import Flask
from flask_wtf.csrf import CSRFProtect
from . import db

# A very simple Flask Hello World app for you to get started with...

csrf = CSRFProtect()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    csrf.init_app(app)
    db.init_app(app)

    from .routes import register_routes
    register_routes(app)

    return app

