from flask import Blueprint

bp = Blueprint("scholarships", __name__)
from src.scholarships import routes
