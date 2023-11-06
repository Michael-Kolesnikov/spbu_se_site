from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(
    __name__,
    static_url_path="",
    static_folder="static",
    template_folder="templates",
    )
    app.config.from_object(config[config_name])

    return app