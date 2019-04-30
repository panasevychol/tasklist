from flask_restful import Api

from tasklist import app

from tasklist.tasks.urls import urls as tasks_urls


api = Api(app)

for resource in [*tasks_urls, ]:
    api.add_resource(*resource)
