from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')

from app import views
