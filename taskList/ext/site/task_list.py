import uuid
import datetime

class EmptyTitleException(Exception):
    pass

class UnknownIdException(Exception):
    pass

settings:list[tuple[datetime.timedelta, str]] = [
    (datetime.timedelta(days=7), "Low time urgency"),
    (datetime.timedelta(days=3), "Medium time urgency"),
    (datetime.timedelta(hours=24), "High time urgency"),
    (datetime.timedelta(), "Extreme time urgency")
]


class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
        super().__init__()
        self.task_list = {}


    def create_task(self, title: str, description: str, deadline=None):
        """ adds a new task to the task list """
        #TODO add a more robust treatment for missing title
        if not title:
            raise EmptyTitleException("Missing title for task")
        else:
            self.task_list[self.create_id()] = {
                'title': title,
                'description': description,
                'completed': False,
                'deadline': deadline
            }
    
    def create_id(self):
        return str(uuid.uuid4())
    
    def edit_task(self, id, title:str=None, description:str=None,
                    completed:bool=None) -> None:
        """ Alters task data """
        try:
            if title is not None:
                if title == "":
                    raise EmptyTitleException("Task must have a title")
                self.task_list[id]['title'] = title
            if description is not None:
                self.task_list[id]['description'] = description
            if completed is not None:
                # Probably shouldn't exist since self.complete_task exists
                # to make a completed tasks uncompleted again?
                self.task_list[id]['completed'] = completed
        except KeyError:
            print(self.task_list)
            raise UnknownIdException()
            
    def get_task_by_id(self, id):
        """ Return task by id """
        try:
            return self.task_list[id]
        except KeyError:
            raise UnknownIdException()

    def complete_task(self, id):
        self.task_list[id]['completed'] = True
    
    def get_tasks(self):
        """ Return all the tasks """
        return self.task_list
    
    def get_uncompleted_tasks(self):
        array = {}
        for item in self.task_list.items():
            k = item[0]
            v = item[1]
            if not v["completed"]:
                array[k] = v
        return array
    
    def get_completed_task(self):
        array = {}
        for item in self.task_list.items():
            k = item[0]
            v = item[1]
            if v["completed"]:
                array[k] = v
        return array
    
    def has_deadline(self, id):
        return self.task_list[id]["deadline"] is not None
    
    def deadline_status(self, id):
        task = self.get_task_by_id(id)
        if not self.has_deadline(id):
            return "No time urgency"
        now = datetime.datetime.today()
        ret = None
        for k, v in settings:
            ret = v
            if task["deadline"] - now >= k:
                return v
        return "Delayed"
