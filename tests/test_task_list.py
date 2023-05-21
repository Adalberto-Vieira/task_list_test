from unittest import mock
from unittest.mock import MagicMock

def test_task_created_sucess(task_list):
    """ Test inserting a task operation success"""
    task_list.create_id = MagicMock(return_value=0)
    task_list.creat_task("test", "testing")
    assert task_list.get_tasks() == {0:{"completed":False,"description":"testing","title":"test"}}
    
def test_unique_id_created_with_new_task(task_list):
    """ test the tasks creation of a Id """
    task_list.creat_task("test1", "testing")
    task_list.creat_task("test2", "testing")
    tasks = task_list.get_tasks()
    assert len(tasks.keys()) == 2
    
    
def test_complete_task_succesfully(task_list):
    """ """
    task_list.creat_task("test1", "testing")
    task_list.creat_task("test2", "testing")
    pass