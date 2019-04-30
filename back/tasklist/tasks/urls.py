from .views import (
    CreateTaskAPIView,
    CreateTaskListAPIView,
    TaskAPIView,
    TaskListAPIView
)

urls = [
    (CreateTaskListAPIView, '/task-lists'),
    (TaskListAPIView, '/task-lists/<int:id>'),

    (CreateTaskAPIView, '/tasks'),
    (TaskAPIView, '/tasks/<int:id>'),
]
