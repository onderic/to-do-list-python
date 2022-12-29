import pytest
from main import *


def test_task():
    task = Task('Buy groceries','high')
    assert task.description == 'Buy groceries'
    assert task.priority == 'high'
    assert str(task) == "Buy groceries (priority: high)"

def test_high_priority_task():
    task = HighPriorityTask('Buy groceries')
    assert task.description == 'Buy groceries'
    assert task.priority == 'high'
    assert str(task) == "Buy groceries (priority: high)"

def test_medium_priority_task():
    task = MediumPriorityTask('Take out the trash')
    assert task.description == 'Take out the trash'
    assert task.priority == 'medium'
    assert str(task) == "Take out the trash (priority: medium)"

def test_low_priority_task():
    task = LowPriorityTask('Watch a movie')
    assert task.description == 'Watch a movie'
    assert task.priority == 'low'
    assert str(task) == "Watch a movie (priority: low)"

@pytest.fixture
def factory():
    return TaskFactory()
    
def test_task_factory(factory):
    task = factory.create_task('Buy groceries','high')
    assert isinstance(task, HighPriorityTask)
    task = factory.create_task('Take out the trash','medium')
    assert isinstance(task,MediumPriorityTask)
    task = factory.create_task('Watch a movie','low')
    assert isinstance(task, LowPriorityTask)


@pytest.fixture
def todo_list():
    return TodoList()
  
def test_to_list(todo_list):
    todo_list = TodoList()
    todo_list.add_task('Buy groceries','high')
    todo_list.add_task('Take out the trash','medium')
    todo_list.add_task('Watch a movie','low')

    assert len(todo_list.tasks) == 3
    assert str(todo_list.tasks[0]) == "Buy groceries (priority: high)"
    assert str(todo_list.tasks[1]) == "Take out the trash (priority: medium)"
    assert str(todo_list.tasks[2]) == "Watch a movie (priority: low)"

def test_to_do_list_remove(todo_list):
  
    todo_list.add_task('Buy groceries','high')
    todo_list.add_task('Take out the trash','medium')
    todo_list.add_task('Watch a movie','low')

    todo_list.remove_task(0)
    assert len(todo_list.tasks) == 2
    assert str(todo_list.tasks[0]) == "Take out the trash (priority: medium)"
    assert str(todo_list.tasks[1]) == "Watch a movie (priority: low)"

def test_view_to_list(capsys,todo_list):
    todo_list.add_task('Buy groceries','high')
    todo_list.add_task('Take out the trash','medium')
    
    todo_list.view_tasks()
    captured = capsys.readouterr()
    assert captured.out == "1. Buy groceries (priority: high)\n2. Take out the trash (priority: medium)\n"
