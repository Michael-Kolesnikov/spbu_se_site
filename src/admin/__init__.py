from flask import Blueprint

bp = Blueprint("admin_se", __name__)

from src.admin import routes
