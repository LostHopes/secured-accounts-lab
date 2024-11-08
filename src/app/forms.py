from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(min=8, max=256)], 
        render_kw={"placeholder": "Enter your email address"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=50)],
        render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)],
        render_kw={'placeholder': "Enter your username"})
    email = EmailField("Email", validators=[DataRequired(), Length(min=8, max=256)],
        render_kw={"placeholder": "Enter your email address"})
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=50)],
        render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), Length(min=8, max=50)],
        render_kw={"placeholder": "Confirm your password"})
    terms = BooleanField("Accept Terms", validators=[DataRequired()])
    submit = SubmitField("Register")