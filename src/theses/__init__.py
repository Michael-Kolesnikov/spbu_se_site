from flask import Blueprint

bp = Blueprint("theses", __name__)
from src.theses import routes
from src.theses.review import routes
