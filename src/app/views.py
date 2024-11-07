from flask import render_template
from app import app


@app.get("/")
def home():
    title: str = "Home"
    return render_template("index.html", title=title)