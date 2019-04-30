from flask_sqlalchemy import SQLAlchemy

from tasklist import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from tasklist.tasks.models import *

db.create_all()
