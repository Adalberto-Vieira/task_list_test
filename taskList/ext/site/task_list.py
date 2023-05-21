import uuid

class EmptyTitleException(Exception):
    pass

class UnknownIdException(Exception):
    pass


class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
        super().__init__()
        self.task_list = {}


    def create_task(self, title: str, description: str):
        """ adds a new task to the task list """
        #TODO add a more robust treatment for missing title
        if not title:
            raise EmptyTitleException("Missing title for task")
        else:
            self.task_list[self.create_id()] = {
                'title': title,
                'description': description,
                'completed': False,  
            }
    
    def create_id(self):
        return str(uuid.uuid4())
    
    def edit_task(self, id, title=None, description=None,
                    completed=None):
        """ Alters task data """
        #TODO add treatment for exceptions
        try:
            if title is not None:
                if title == "":
                    raise EmptyTitleException("Task must have a title")
                self.task_list[id]['title'] = title
            if description is not None:
                self.task_list[id]['description'] = description
            if completed is not None:
                self.task_list[id]['completed'] = completed
        except:
            print(self.task_list)
            raise UnknownIdException()

    def complete_task(self, id):
        pass

    def get_task_by_id(self, id):
        """ Return task by id """
        try:
            return self.task_list[id]
        except KeyError:
            raise UnknownIdException()
    
    def get_tasks(self):
        """ Return all the tasks """
        return self.task_list
    
    def get_uncompleted_tasks(self):
        
        return self.task_list
    
    def get_completed_task(self):
        return self.completed_task_list