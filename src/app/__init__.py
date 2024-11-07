from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__)
db = SQLAlchemy()


def create_app(config_obj: object=config.DevConfig):

    with app.app_context():
        app.config.from_object(config_obj)
        from app import views
        db.init_app(app)

    return app