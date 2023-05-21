import uuid

class EmptyTitleException(Exception):
    pass

class UnknownIdException(Exception):
    pass

class EmptyListException(Exception):
    pass


class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
        super().__init__()
        self.task_list = {}
        self.task_bin = {}


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
        return {k: v for k,v in self.task_list.items() if not v["completed"]}
    
    def get_completed_task(self):
        return {k: v for k,v in self.task_list.items() if v["completed"]}

    def delete_task(self,id):
        pass

    def move_bin(self,id):
        try:
            if len(self.task_list) == 0:
                raise EmptyListException
            if id not in self.task_list.keys():
                raise UnknownIdException   
            self.task_bin[id] = self.task_list[id]
            self.task_list.pop(id)
        except:
            print("Failed move to bin")
        
    def get_bin(self):
        return self.task_bin