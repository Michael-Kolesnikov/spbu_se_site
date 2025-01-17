import shutil
from flask import Flask
from config import config
from src.extensions import db, login_manager
from pathlib import Path
from flaskext.markdown import Markdown
from flask_migrate import Migrate
from flask_simplemde import SimpleMDE
from flask_admin import Admin
from src.general import bp as general_bp
from src.summer_schools import bp as school_bp
from src.scholarships import bp as scholarship_bp
from src.internships import bp as internship_bp
from src.errors import bp as errors_bp
from src.auth import bp as auth_bp
from src.news import bp as news_bp
from src.diplomas import bp as diplomas_bp
from src.theses import bp as theses_bp
from src.practice import bp as practice_bp


admin = Admin(name="se_admin", template_mode="bootstrap4")


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
    admin.init_app(app)
    login_manager.init_app(app)
    # Init markdown
    Markdown(app, extensions=["tables"])
    migrate = Migrate(app, db, render_as_batch=True)
    SimpleMDE(app)

    app.register_blueprint(errors_bp)
    app.register_blueprint(general_bp)
    app.register_blueprint(school_bp)
    app.register_blueprint(scholarship_bp)
    app.register_blueprint(internship_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(diplomas_bp)
    app.register_blueprint(theses_bp)
    app.register_blueprint(practice_bp)
    from src.admin import bp as admin_bp

    app.register_blueprint(admin_bp)
    return app
