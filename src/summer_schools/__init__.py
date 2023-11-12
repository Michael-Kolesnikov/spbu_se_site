from flask import Blueprint

bp = Blueprint("summer_schools", __name__)
from src.summer_schools import routes