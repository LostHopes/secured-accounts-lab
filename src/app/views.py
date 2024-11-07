from flask import render_template
from flask_login import login_required
from app import app, login_manager
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.get("/")
def index():
    title: str = "Home"
    return render_template("index.html", title=title)


@app.get("/login")
def login():
    title: str = "Login"
    return render_template("login.html", title=title)


@app.get("/register")
def register():
    title: str = "Register"
    return render_template("register.html", title=title)


@app.get("/profile")
@login_required
def profile():
    title: str = "Profile"
    return render_template("profile.html", title=title)

