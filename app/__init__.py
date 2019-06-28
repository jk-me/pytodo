from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = 'secret-key' as a dictionary/object
# see in terminal by running `from pytodo import app` and `app.config['SECRET_KEY']`
from app import routes
