from flask import request
from flask_restful import Resource

from tasklist.db import db

from .models import TaskList, Task
from .utils import get_object_or_404, serialize_task, serialize_task_list


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
        json_response = request.get_json()
        task = Task(
            name=json_response['name'],
            task_list_id=json_response['task_list_id']
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
        json_response = request.get_json()
        name, task_finished = [
            json_response.get(param) for param in ('name', 'task_finished')
        ]
        for param in ('name', 'task_finished'):
            value = json_response.get(param)
            if value is not None:
                setattr(task, param, value)

        db.session.commit()
        return serialize_task(task)
