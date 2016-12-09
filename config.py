from flask import Flask

WTF_CSRF_ENABLED = True
SECRET_KEY = 'flask-hello-world'

app = Flask(__name__)

MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = ''
MYSQL_HOST = ''
