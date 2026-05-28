import pytest    #type: ignore
import asyncio

from src.task.task import Task

def test_task_str():
    test = Task.create({"name": "name", "body": "body", "status": 1, "priority": 1})
    str_test = str(test)
    assert str_test.startswith("Task( id: ")
    assert str_test.endswith(", name: name, body: body, status: 1, priority: 1 )")

def test_task_short():
    test = Task.create({"name": "name", "body": "body", "status": 1, "priority": 1})
    str_test = test.short()
    assert str_test.startswith("Task( name: name )")

@pytest.mark.asyncio
async def test_run():
    task = Task.create({"name": "name", "body": "body", "status": 1, "priority": 1})
    running_task = asyncio.create_task(task.run())
    await asyncio.sleep(5.1)
    assert running_task.done
    task = task = Task.create({"name": "name", "body": "body", "status": 4, "priority": 1})
    running_task = asyncio.create_task(task.run())
    assert running_task.done
