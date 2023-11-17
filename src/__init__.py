from flask import Flask
from config import config
from src.extensions import db
from pathlib import Path
import shutil
from flask_migrate import Migrate
from flask_simplemde import SimpleMDE
from src.general import bp as general_bp
from src.summer_schools import bp as school_bp
from src.scholarships import bp as scholarship_bp
from src.internships import bp as internship_bp


def create_app(config_name):
    app = Flask(
        __name__,
        static_url_path="",
        static_folder="static",
        template_folder="templates",
    )
    app.config.from_object(config[config_name])
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
                
    SimpleMDE(app)
    app.register_blueprint(general_bp)
    app.register_blueprint(school_bp)
    app.register_blueprint(scholarship_bp)
    app.register_blueprint(internship_bp)
    return app
