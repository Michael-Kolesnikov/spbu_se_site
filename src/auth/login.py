from flask import flash, redirect, url_for, request
from src.models import Users
from src.extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@login_manager.unauthorized_handler
def handle_needs_login():
    flash("Для выполнения этого действия необходимо войти.")
    return redirect(url_for("login_index", next=request.endpoint))
