from lib.todo import *

"""
Test that on init the task is set to incomplete, shown by Boolean False
"""
def test_todo_starts_with_task_set_as_False():
    todo = Todo("Feed cat")
    assert todo.task == "Feed cat"
    assert todo.completed == False

"""
When we do the task, 
it should be marked as complete, shown by Boolean True
"""
def test_todo_starts_with_task_set_as_True():
    todo = Todo("Feed cat")
    todo.mark_complete()
    assert todo.completed == True