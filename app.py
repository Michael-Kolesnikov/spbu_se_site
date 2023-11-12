from flask_frozen import Freezer
from src import create_app
import sys
from src.extensions import db

app = create_app('default')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
