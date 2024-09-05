import os
from dotenv import load_dotenv
FLASK_APP = 'microblog.py'
basedir = os.path.abspath(os.path.dirname(__file__))  
# ENVIRONMENT = 'development'


FLASK_DEBUG = True
SECRET_KEY = 'GDtfD^&$%@^8tgYjD'
class Config:
    SECRET_KEY = os.environ.get(SECRET_KEY) or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')