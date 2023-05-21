from unittest import mock
from unittest.mock import MagicMock

def test_task_created_sucess(task_list):
    """ Test inserting a task operation success"""
    task_list.create_id = MagicMock(return_value=0)
    task_list.create_task("test", "testing")
    assert task_list.get_tasks() == {0:{"completed":False,"description":"testing","title":"test"}}
    
def test_unique_id_created_with_new_task(task_list):
    """ test the tasks creation of a Id """
    task_list.create_task("test1", "testing")
    task_list.create_task("test2", "testing")
    tasks = task_list.get_tasks()
    assert len(tasks.keys()) == 2
    
    
def test_complete_task_succesfully(task_list):
    """ """
    task_list.create_task("test1", "testing")
    task_list.create_task("test2", "testing")
    pass

def test_task_should_update_title_when_title_is_edited(task_list):
    old_title:str = "test1"
    new_title:str = "new" + old_title
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task("test1", "testing")
    task_list.edit_task(0, title=new_title)

    task = task_list.get_task_by_id(id=0)

    assert task["title"] == new_title