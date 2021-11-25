from flask import render_template, request  # ADDED
from app import app
from models.todo_list import tasks, add_new_task
from models.task import Task


@app.route("/tasks")
def index():
    return render_template("index.html", title="Home", tasks=tasks)


@app.route("/tasks", methods=["POST"])  # Methods is expected - can pass more than one
def add_task():
    # ToDO:
    # 1. Using the data from the form to create a new task.
    task_title = request.form["title"]
    task_description = request.form["description"]

    new_task = Task(task_title, task_description, False)
    # 2. Add the new task to tasks
    add_new_task(new_task)
    # 3. Render the updated task list
    return index()
