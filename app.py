from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

from routes import *

if __name__ == '__main__':
    app.run(port=5555, debug=True)
