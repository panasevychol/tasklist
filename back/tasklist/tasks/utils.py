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
