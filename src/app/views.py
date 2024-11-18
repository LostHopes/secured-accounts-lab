from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_mail import Message
from app import app, db, captcha, mail
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.get("/")
def index():
    title: str = "Home"
    return render_template("index.html", title=title)


@app.get("/login/")
def login():
    title: str = "Login"

    if current_user.is_authenticated:
        flash("You are already logged in", "flash-info")
        return redirect(url_for("profile"))

    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("profile"))

    return render_template("login.html", title=title, form=form)


@app.get("/register/")
def register():
    title: str = "Register"
    simple_captcha = captcha.create()

    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("login"))

    return render_template("register.html", title=title, form=form, captcha=simple_captcha)


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


    if not form.validate() and \
        check_password_hash(user.password, password) is False \
            or not user:

        flash("Invalid password or the user didn't exist", "flash-info")
        return redirect(url_for("login"))

    remember = form.remember.data

    login_user(user, remember)
    flash("Logged in successfully", "flash-success")
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
        
        captcha_hash = request.form.get("captcha-hash")
        captcha_text = request.form.get("captcha-text")

        if captcha.verify(captcha_text, captcha_hash) is False:
            flash("Couldn't verify the captcha", "flash-error")
            return redirect(url_for("register"))

        if form.validate() is False:
            flash("Failed to validate data", "flash-error")
            return redirect(url_for("register"))


        password_hash = generate_password_hash(password)
        if check_password_hash(password_hash, confirm_password) is False:
            flash("Passwords aren't the same", "flash-info")
            return redirect(url_for("register"))

        msg = Message(
            subject=f"Confirm registration for {username}",
            recipients=[email],
            body=None
        )

        mail.send(msg)
        flash("The mail with confirmation was sent to your email", "flash-info")

        user = User(username=username, email=email, password=password_hash)

        db.session.add(user)
        db.session.commit()

    except IntegrityError:
        flash("User already exists", "flash-error")
        db.session.rollback()
        return redirect(url_for("register"))
        

    flash("User has been successfully registered", "flash-success")
    return redirect(url_for("login"))
    

@app.post("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "flash-info")
    return redirect(url_for("index"))


@app.post("/confirm/")
def confirm_account():
    flash("Your account has been verified", "flash-success")
    return redirect(url_for("login"))