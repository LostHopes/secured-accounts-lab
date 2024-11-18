from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_simple_captcha import CAPTCHA, DEFAULT_CONFIG
from flask_mail import Mail
from flask_security import Security
from app import config

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "You should login before accessing this page"
login_manager.login_message_category = "info"
captcha = CAPTCHA(DEFAULT_CONFIG)
mail = Mail()
security = Security()


def create_app(config_obj: object=config.DevConfig):

    with app.app_context():
        app.config.from_object(config_obj)
        from app import views
        from app import errors
        from app.models import User
        db.init_app(app)
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        captcha.init_app(app)
        mail.init_app(app)
        security.init_app(app, db)

        db.create_all(bind_key=None)

    return app