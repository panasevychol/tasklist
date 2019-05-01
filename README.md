# test-flask

## Tasklist app

### Running the app

To run the app on macOS or Linux:
- install docker and docker-compose
- clone the repository
- execute `make build` in project root folder
- execute `make run`

(should work also on Windows but I didn't test it)

### Usage

- after launching the app with `make run` open http://localhost:3000/ in your browser to see the welcome page.
- go to admin panel by clicking the link (or opening http://localhost:5000/admin) and add some Task List and some Tasks (optional)
- you can browse your Task Lists in UI by opening the path `/tasklist/<id>` (example: http://localhost:3000/#!/tasklist/1). There you got a main view of Task List where you can see tasks, finish/unfinish, edit and delete them.

### Urls

Front:
- `/` - welcome screen
- `/tasklist/1` - Task List view

Back:
- `/api/task-lists` - create Task List API view. Method `POST`
- `/api/task-lists/<int:id>` - retrieve-update-destroy Task List API view. Methods: `GET`, `PATCH`, `DELETE`
- `/api/tasks` - create Task API view. Method `POST`
- `/api/tasks/<int:id>` - retrieve-update-destroy Task API view. Methods: `GET`, `PATCH`, `DELETE`
