from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__)
db = SQLAlchemy()


def create_app(config_obj: object=config.DevConfig):

    with app.app_context():
        app.config.from_object(config_obj)
        from app import views
        from app.models import User
        db.init_app(app)
        db.create_all(bind_key=None)

    return app