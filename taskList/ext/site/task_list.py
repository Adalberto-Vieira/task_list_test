import uuid


class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
        super().__init__()
        self.task_list = {}


    def creat_task(self, title: str, description: str):
        """ adds a new task to the task list """
        #TODO add a more robust treatment for missing title
        if not title:
            raise Exception("Missing title for task")
        else:
            self.task_list[self.create_id()] = {
                'title': title,
                'description': description,
                'completed': False,  
            }
    
    def create_id(self):
        return str(uuid.uuid4())
    
    def edit_task(self, id, title="New task", description="New task",
                    completed=False):
        """ Alters task data """
        #TODO add treatment for exceptions
        try:
            self.task_list[id]['title'] = title
            self.task_list[id]['description'] = description
            self.task_list[id]['completed'] = completed
        except:
            print(self.task_list)
            raise

    def complete_task(self, id):
        self.task_list[id]['completed'] = True
    
    def get_tasks(self):
        """ Return all the tasks """
        return self.task_list
    
    def get_uncompleted_tasks(self):
        return {k: v for k,v in self.task_list.items() if not v["completed"]}
    
    def get_completed_task(self):
        return {k: v for k,v in self.task_list.items() if v["completed"]}
