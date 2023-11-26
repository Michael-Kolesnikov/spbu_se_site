from flask import Blueprint

bp = Blueprint("diplomas", __name__)
from src.diplomas import routes
