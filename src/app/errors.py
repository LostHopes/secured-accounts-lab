from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_exist(request):
    title = "Not found"
    error = "Page doesn't exist"
    return render_template("errors.html", title=title, error=error)