from unittest import mock
from unittest.mock import MagicMock
import pytest
from taskList.ext.site.task_list import EmptyTitleException

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

def test_task_should_update_title_when_it_is_edited(task_list):
    old_title:str = "test1"
    new_title:str = "new" + old_title
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task(old_title, "testing")
    task_list.edit_task(0, title=new_title)

    task = task_list.get_task_by_id(id=0)

    assert task["title"] == new_title

def test_task_should_not_update_title_when_it_is_not_edited(task_list):
    title:str = "test1"
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task(title, "testing")
    task_list.edit_task(0)

    task = task_list.get_task_by_id(id=0)

    assert task["title"] == title

def test_task_should_update_description_when_it_is_edited(task_list):
    old_description:str = "testing"
    new_description:str = "new" + old_description
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task("test1", old_description)
    task_list.edit_task(0, description=new_description)

    task = task_list.get_task_by_id(id=0)

    assert task["description"] == new_description

def test_task_should_update_description_when_it_is_edited(task_list):
    description:str = "testing"
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task("test1", description)
    task_list.edit_task(0)

    task = task_list.get_task_by_id(id=0)

    assert task["description"] == description

def test_task_should_update_completion_status_when_it_is_edited(task_list):
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task("test1", "testing")
    task_list.edit_task(0, completed=True)

    task = task_list.get_task_by_id(id=0)

    assert task["completed"] == True

def test_task_should_not_update_title_when_title_is_not_edited(task_list):
    task_list.create_id = MagicMock(return_value=0)

    task_list.create_task("test1", "testing")
    task_list.edit_task(0)

    task = task_list.get_task_by_id(id=0)

    assert task["completed"] == False

def test_editing_fails_when_title_is_empty(task_list):
    with pytest.raises(EmptyTitleException) as e_info:
            old_title:str = "test1"
            new_title:str = ""
            task_list.create_id = MagicMock(return_value=0)

            task_list.create_task(old_title, "testing")
            task_list.edit_task(0, title=new_title)