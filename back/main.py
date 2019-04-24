from flask import Flask, request
from flask_admin import Admin
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = b'Really super secret'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class TaskList(db.Model):
    __tablename__ = 'task_list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    task_finished = db.Column(db.Boolean, default=False, nullable=False)

    task_list_id = db.Column(
        db.Integer, db.ForeignKey('task_list.id'), nullable=False
    )
    task_list = db.relationship(
        "TaskList", backref=db.backref("tasks")
    )

    def __repr__(self):
        return '<Task %r>' % self.name

# db.drop_all()
db.create_all()

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(TaskList, db.session))
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


def serialize_task(task):
    return {
        attr: getattr(task, attr)
        for attr in ['id', 'name', 'task_finished']
    }

def serialize_task_list(task_list):
    task_list_serialized = {
        attr: getattr(task_list, attr)
        for attr in ['id', 'name']
    }
    task_list_serialized['tasks'] = [
        serialize_task(task) for task in task_list.tasks
    ]
    return task_list_serialized

# end utils


# API views

class CreateTaskListAPIView(Resource):

    def post(self):
        task_list = TaskList(
            name=request.get_json()['name']
        )
        db.session.add(task_list)
        db.session.commit()
        return serialize_task_list(task_list), 201


class TaskListAPIView(Resource):

    def get(self, id):
        task_list = get_object_or_404(TaskList, id=id)
        return serialize_task_list(task_list)


class CreateTaskAPIView(Resource):

    def post(self):
        task = Task(
            name=request.form['name'],
            task_list_id=request.get_json()['task_list_id']
        )
        db.session.add(task)
        db.session.commit()
        return serialize_task(task), 201


class TaskAPIView(Resource):

    @staticmethod
    def serialize(task):
        return {
            attr: getattr(task, attr)
            for attr in ['id', 'name', 'task_finished']
        }

    def get(self, id):
        task = get_object_or_404(Task, id=id)
        return serialize_task(task)

    def delete(self, id):
        task = get_object_or_404(Task, id=id)
        db.session.delete(task)
        db.session.commit()
        return True

    def patch(self, id):
        task = get_object_or_404(Task, id=id)
        task.task_finished = request.get_json()['task_finished']
        db.session.commit()
        return serialize_task(task)


api.add_resource(CreateTaskListAPIView, '/task-lists')
api.add_resource(TaskListAPIView, '/task-lists/<int:id>')

api.add_resource(CreateTaskAPIView, '/tasks')
api.add_resource(TaskAPIView, '/tasks/<int:id>')
