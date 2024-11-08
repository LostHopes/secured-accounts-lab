from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.get("/")
def index():
    title: str = "Home"
    return render_template("index.html", title=title)


@app.get("/login")
def login():
    title: str = "Login"

    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("profile"))

    return render_template("login.html", title=title, form=form)


@app.get("/register")
def register():
    title: str = "Register"

    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("login"))

    return render_template("register.html", title=title, form=form)


@app.get("/profile")
@login_required
def profile():
    title: str = "Profile"
    return render_template("profile.html", title=title)

