from flask import Blueprint, render_template, make_response, jsonify, request

from .task_list import TaskList
import distutils

bp = Blueprint("site", __name__)

task_list = TaskList()

@bp.route("/")
def index():
    """ Renders the initial URL """
    return render_template("index.html", 
                            tasks=task_list.get_tasks(),
                            warning=False)

#TODO fix readirect behavior
@bp.route("/create_task", methods = ['POST'])
def creat_task():
    """ Creates a new task in the list """
    warning = False
    try:
        task_list.creat_task(request.form.get('title'), request.form.get('description'))
    except:
        warning = True
    return render_template("index.html", 
                            tasks=task_list.get_tasks(),
                            warning=warning)

@bp.route("/get_tasks")
def get_tasks():
    """ Returns the list of tasks """
    tasks = task_list.get_tasks()
    if tasks: 
        return make_response(jsonify(tasks), 200)
    else:
        return make_response("No tasks added", 204)

@bp.route("/edit_task/", methods = ['POST'])
def edit_task():
    """ Editites the task """
    #TODO treat for exceptions
    task_list.edit_task(request.form.get("id"),
                        request.form.get("title"),
                        request.form.get("description"),
                        bool(int(request.form.get("status"))))
    return render_template("index.html", 
                        tasks=task_list.get_tasks(),
                        warning=False)
