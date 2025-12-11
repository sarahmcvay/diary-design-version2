from lib.todo_list import *
from unittest.mock import Mock

"""
If there are no todo entries, 
the task manager returns an empty list
"""
def test_todo_list_starts_with_an_empty_list():
    todo_list = TodoList()
    result = todo_list.list_todo
    assert result == []

"""
# todo list can add new task
# """
def test_task_man_add_task():
    todo_list = TodoList()
    task_1 = Mock()
    task_2 = Mock()
    todo_list.add(task_1)
    todo_list.add(task_2)

    assert todo_list.list_todo == [task_1, task_2]