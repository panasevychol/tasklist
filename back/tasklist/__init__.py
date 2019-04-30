from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = b'Really super secret'
CORS(app)

from tasklist.db import db

from tasklist.admin import admin

from tasklist.api import api
