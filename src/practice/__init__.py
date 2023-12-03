from flask import Blueprint

bp = Blueprint("practice", __name__)

from src.practice import routes
