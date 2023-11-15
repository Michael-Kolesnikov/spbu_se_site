from flask import Blueprint

bp = Blueprint("internships", __name__)
from src.internships import routes
