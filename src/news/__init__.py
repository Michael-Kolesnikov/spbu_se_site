from flask import Blueprint

bp = Blueprint("news", __name__)
from src.news import routes
