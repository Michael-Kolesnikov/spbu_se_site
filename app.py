from flask_frozen import Freezer
from src import create_app
import sys
from src.extensions import db
from src.extensions import init_db

app = create_app('default')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            with app.app_context():
                init_db()
    else:
        app.run(port=5000, debug=True)
