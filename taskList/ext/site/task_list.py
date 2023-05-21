
class TaskList:
    """ Classs that represents the interactions with a class"""

    task_list = []
    completed_task_list = []


    @staticmethod
    def creat_task(title: str, description: str):
        """ adds a new task to the task list """
        #TODO add a more robust treatment for missing title
        if not title:
            raise Exception("Missing title for task")
        else:
            TaskList.task_list.append({
                'title': title,
                'description': description,
                'completed': False,
                'id': len(TaskList.task_list)
            })
    

    @staticmethod
    def edit_task(id: int, title="New task", description="New task",
                    completed=False):
        """ Alters task data """
        #TODO add treatment for exceptions
        TaskList.task_list[id]['title'] = title
        TaskList.task_list[id]['description'] = description
        TaskList.task_list[id]['completed'] = completed
        TaskList.task_list[id]['id'] = id


    @staticmethod    
    def get_tasks():
        """ Return all the tasks """
        return TaskList.task_list + TaskList.completed_task_list
