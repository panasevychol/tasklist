from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from tasklist import app

from tasklist.db import db
from tasklist.tasks.models import TaskList, Task

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(TaskList, db.session))
admin.add_view(ModelView(Task, db.session))
