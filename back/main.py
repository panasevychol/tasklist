from flask import Flask
from flask_admin import Admin
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = b'Really super secret'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    task_finished = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.name

db.create_all()

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(Task, db.session))


api = Api(app)

# utils
from sqlalchemy.orm import exc
from werkzeug.exceptions import abort


def get_object_or_404(model, **criterion):
    try:
        return model.query.filter_by(**criterion).one()
    except (exc.NoResultFound, exc.MultipleResultsFound):
        abort(404)

# end utils

class TaskAPIView(Resource):

    @staticmethod
    def serialize(task):
        return {
            attr: getattr(task, attr)
            for attr in ['id', 'name', 'task_finished']
        }

    def get(self, id):
        task = get_object_or_404(Task, id=id)
        return self.serialize(task)

    def patch(self, id):
        pass

api.add_resource(TaskAPIView, '/tasks/<int:id>')
