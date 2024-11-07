from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    pass


class RegisterForm(FlaskForm):
    pass