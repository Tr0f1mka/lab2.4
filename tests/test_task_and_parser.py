import pytest       #type: ignore

from src.task import Task
from src.parser import json_parser

def test_parser_with_error():
    with pytest.raises(ValueError):
        json_parser('{AZAZA:12}')

def test_task_str():
    test = Task.create('{"name": "name", "body": "body", "status": 1, "priority": 1}')
    str_test = str(test)
    assert str_test.startswith("Task( id: ")
    assert str_test.endswith(", name: name, body: body, status: 1, priority: 1 )")

def test_task_short():
    test = Task.create('{"name": "name", "body": "body", "status": 1, "priority": 1}')
    str_test = test.short()
    assert str_test.startswith("Task( name: name )")
