def test_create_sucess(task_list):
    """ Test inserting a task operation success"""
    task_list.creat_task("test", "testing")
    assert task_list.get_tasks() == [{"completed":False,"description":"testing","id":0,"title":"test"}]