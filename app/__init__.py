from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = 'secret-key' as a dictionary/object
# see in terminal by running `from pytodo import app` and `app.config['SECRET_KEY']`

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
