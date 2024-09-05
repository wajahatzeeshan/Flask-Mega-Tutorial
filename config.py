import os


ENVIRONMENT = 'development'
FLASK_APP = 'my-app'
FLASK_DEBUG = True
SECRET_KEY = 'GDtfD^&$%@^8tgYjD'
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'