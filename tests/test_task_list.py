from unittest import mock
from unittest.mock import MagicMock

def test_task_created_sucess(task_list):
    task_list.create_id = MagicMock(return_value=0)
    """ Test inserting a task operation success"""
    task_list.creat_task("test", "testing")
    assert len(task_list.get_tasks()) == 1
    assert task_list.get_tasks() == [{"completed":False,"description":"testing","id":0,"title":"test"}]
    
def test_unique_id_created_with_new_task(task_list):
    """ test the tasks creation of a Id """
    task_list.creat_task("test1", "testing")
    task_list.creat_task("test2", "testing")
    tasks = task_list.get_tasks()
    assert tasks[0]["id"]
    assert tasks[1]["id"]
    assert tasks[0]["id"] != tasks[1]["id"]