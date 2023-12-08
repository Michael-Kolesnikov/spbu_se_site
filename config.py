import os
import pathlib
from datetime import datetime
from string import Template


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
    SQLITE_DATABASE_PATH = pathlib.Path("src/databases").absolute().as_posix()
    # Flask configs
    APPLICATION_ROOT = "/"
    # Freezer config
    FREEZER_RELATIVE_URLS = True
    FREEZER_DESTINATION = "../docs"
    FREEZER_IGNORE_MIMETYPE_WARNINGS = True
    # SQLAlchimy config
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + SQLITE_DATABASE_PATH + "/" + SQLITE_DATABASE_NAME
    )
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
    type_id_string = [
        "",
        "Bachelor_Report",
        "Bachelor_Thesis",
        "Master_Thesis",
        "Autumn_practice_2nd_year",
        "Spring_practice_2nd_year",
        "Autumn_practice_3rd_year",
        "Spring_practice_3rd_year",
        "Production_practice",
        "Pre_graduate_practice",
    ]
    # Yandex disk


YANDEX_CLIENT_ID = "10e079e42b49492295a39e2767e7b049"
YANDEX_SECRET_FILE = os.path.join(
    pathlib.Path(__file__).parent, "configs/flask_se_practice_yandex_secret.conf"
)
if os.path.exists(YANDEX_SECRET_FILE):
    with open(YANDEX_SECRET_FILE, "r") as file:
        YANDEX_SECRET = file.read().rstrip()
else:
    YANDEX_SECRET = ""

YANDEX_AUTHORIZE_URL_TEMPLATE = Template(
    "https://oauth.yandex.ru/authorize?response_type=code"
    "&client_id=$yandex_client_id&redirect_uri=$redirect_uri"
)
YANDEX_GET_TOKEN_URL = "https://oauth.yandex.ru/token"

TABLE_COLUMNS = {
    "name": "ФИО",
    "how_to_contact": "Способ оперативной связи (почта, Teams, Telegram, ...)",
    "supervisor": "Научный руководитель",
    "consultant": "Консультант (если есть), полностью ФИО, должность и компания",
    "theme": "Тема",
    "text": "Текст",
    "supervisor_review": "Отзыв научника",
    "reviewer_review": "Отзыв консультанта",
    "code": "Код",
    "committer": "Имя коммитера",
    "presentation": "Презентация",
}

TEXT_UPLOAD_FOLDER = "static/practice/texts/"
REVIEW_UPLOAD_FOLDER = "static/practice/reviews/"
PRESENTATION_UPLOAD_FOLDER = "static/practice/slides/"

ALLOWED_EXTENSIONS = {"pdf"}

MIN_LENGTH_OF_TOPIC = 7
MIN_LENGTH_OF_GOAL = 20
MIN_LENGTH_OF_TASK = 15

MIN_LENGTH_OF_FIELD_WAS_DONE = 10
MIN_LENGTH_OF_FIELD_PLANNED_TO_DO = 10

FORMAT_DATE_TIME = "%d.%m.%Y %H:%M"

# Folders for materials of archive theses
ARCHIVE_TEXT_FOLDER = "./static/thesis/texts/"
ARCHIVE_PRESENTATION_FOLDER = "./static/thesis/slides/"
ARCHIVE_REVIEW_FOLDER = "./static/thesis/reviews/"

config = {"default": Config}
