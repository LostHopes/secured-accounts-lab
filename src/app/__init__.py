from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app import config

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "You should login before accessing this page"
login_manager.login_message_category = "info"

def create_app(config_obj: object=config.DevConfig):

    with app.app_context():
        app.config.from_object(config_obj)
        from app import views
        from app.models import User
        bcrypt.init_app(app)
        login_manager.init_app(app)
        db.init_app(app)
        db.create_all(bind_key=None)

    return app