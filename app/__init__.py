from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
# app.debug = True
migrate = Migrate(app, db)

from app import routes, models
