from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import check_password_hash, generate_password_hash
from app import app, db
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.get("/")
def index():
    title: str = "Home"
    return render_template("index.html", title=title)


@app.get("/login/")
def login():
    title: str = "Login"

    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("profile"))

    return render_template("login.html", title=title, form=form)


@app.get("/register/")
def register():
    title: str = "Register"

    form = RegisterForm()
    if form.validate_on_submit():

        return redirect(url_for("login"))

    return render_template("register.html", title=title, form=form)


@app.get("/profile/")
@login_required
def profile():
    title: str = "Profile"
    return render_template("profile.html", title=title)
    

@app.post("/login/")
def process_login():
    form = LoginForm(request.form)

    email = form.email.data
    password = form.password.data

    user = db.session.query(User).filter_by(email=email).first()

    if form.validate() and check_password_hash(user.password, password) is False:
        flash("Invalid password or the user didn't exist", "info")
        return redirect(url_for("login"))

    remember = form.remember.data

    login_user(user, remember)
    flash("Login successful", "success")
    return redirect(url_for("profile"))


@app.post("/register/")
def process_register():

    try:
        form = RegisterForm(request.form)
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        terms = form.terms.data

        if form.validate() is False:
            flash("Failed to validate data", "error")
            return redirect(url_for("register"))


        password_hash = generate_password_hash(password)
        if check_password_hash(password_hash, confirm_password) is False:
            flash("Passwords aren't the same", "info")
            return redirect(url_for("register"))

        user = User(username=username, email=email, password=password_hash)

        db.session.add(user)
        db.session.commit()

    except IntegrityError:
        flash("User already exists", "error")
        db.session.rollback()
        return redirect(url_for("register"))
        

    flash("User has been successfully registered")
    return redirect(url_for("login"))
    

@app.post("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("index"))
