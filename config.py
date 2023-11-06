import os
import pathlib
from datetime import datetime

class Config(object):
    SECRET_KEY = os.path.join(
        pathlib.Path(__file__).parent, "configs/flask_se_secret.conf"
    )
    MAIL_PASSWORD_FILE = os.path.join(
        pathlib.Path(__file__).parent, "configs/flask_se_mail.conf"
    )
    if os.path.exists(MAIL_PASSWORD_FILE):
        with open(MAIL_PASSWORD_FILE, "r") as file:
            MAIL_PASSWORD = file.read().rstrip()
    else:
        print("There is no MAIL_PASSWORD_FILE, generate random MAIL_PASSWORD")
    current_data = datetime.today().strftime("%Y-%m-%d")
    SQLITE_DATABASE_BACKUP_NAME = "se_backup_" + current_data + ".db"
    MAIL_PASSWORD = os.urandom(16).hex()
    SECRET_KEY_THESIS = os.urandom(16).hex()
    SQLITE_DATABASE_NAME = "se.db"
    SQLITE_DATABASE_PATH = pathlib.Path("databases/").absolute().as_posix()
    # Flask configs
    APPLICATION_ROOT = "/"
    # Freezer config
    FREEZER_RELATIVE_URLS = True
    FREEZER_DESTINATION = "../docs"
    FREEZER_IGNORE_MIMETYPE_WARNINGS = True
    # SQLAlchimy config
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + SQLITE_DATABASE_NAME
    SECRET_KEY = SECRET_KEY
    SESSION_COOKIE_NAME = "se_session"
    # Secret for API
    SECRET_KEY_THESIS = SECRET_KEY_THESIS
    # Basic auth config
    BASIC_AUTH_USERNAME = "se_staff"
    BASIC_AUTH_PASSWORD = SECRET_KEY_THESIS
    # Db
    MSEARCH_BACKEND = "whoosh"
    MSEARCH_ENABLE = True
    # APScheduler
    SCHEDULER_TIMEZONE = "UTC"
    # SimpleMDE
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = False

config = {
    'default': Config
}