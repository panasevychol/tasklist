from flask_restful import Api

from tasklist import app

from tasklist.tasks.urls import urls as resources


api = Api(app)

for resource in resources:
    api.add_resource(*resource)
