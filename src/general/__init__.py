from flask import Blueprint

bp = Blueprint("general", __name__)
from src.general import routes
