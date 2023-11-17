from flask import render_template
from src.errors import bp


@bp.app_errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html"), 404
