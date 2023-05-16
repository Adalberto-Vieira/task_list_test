
class TaskList:
    """ Classs that represents the interactions with a class"""
    def __init__(self):
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
                'id': len(self.task_list)
            })
    

    def edit_task(self, id: int, title="New task", description="New task",
                    completed=False):
        """ Alters task data """
        #TODO add treatment for exceptions
        try:
            self.task_list[id]['title'] = title
            self.task_list[id]['description'] = description
            self.task_list[id]['id'] = id
        except Exception as e:
            print("failed edition")


    def complet_task(self, id):
        try:
            pass
        except:
            raise
        pass
 
    def get_tasks(self):
        """ Return all the tasks """
        tl = [ task for task in self.task_list if not task["completed"] ]
        return tl
