from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(Config)
# app.debug = True
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models