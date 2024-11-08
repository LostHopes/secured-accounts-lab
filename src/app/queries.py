from flask_bcrypt import generate_password_hash, check_password_hash
from app import models


class UserQueries(models.User):
    pass