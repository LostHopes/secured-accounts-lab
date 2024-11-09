from flask_bcrypt import generate_password_hash, check_password_hash
from app.models import User


class UserQueries(User):

    def register(self, **kwargs):
        pass


    def login(self, **kwargs):
        pass