import uuid


class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
        super().__init__()
        self.task_list = []
        self.completed_task_list = []


    def creat_task(self, title: str, description: str):
        """ adds a new task to the task list """
        #TODO add a more robust treatment for missing title
        if not title:
            raise Exception("Missing title for task")
        else:
            self.task_list.append({
                'title': title,
                'description': description,
                'completed': False,
                'id': self.create_id()
            })
    
    def create_id(self):
        return uuid.uuid4()
    
    def edit_task(self, id: int, title="New task", description="New task",
                    completed=False):
        """ Alters task data """
        #TODO add treatment for exceptions
        self.task_list[id]['title'] = title
        self.task_list[id]['description'] = description
        self.task_list[id]['completed'] = completed
        self.task_list[id]['id'] = id

    
    def get_tasks(self):
        """ Return all the tasks """
        return self.task_list + self.completed_task_list
