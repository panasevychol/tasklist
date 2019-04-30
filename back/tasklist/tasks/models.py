from tasklist.db import db


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
