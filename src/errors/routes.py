from src.auth import bp
from flask import render_template


@bp.route("/404.html")
def status_404():
    return render_template("404.html")
