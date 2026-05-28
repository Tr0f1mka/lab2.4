import pytest    #type: ignore
from random import seed

from src.utilities.create_task_utilities import json_parser, validate, filter
from src.utilities.gen_data_task import gen_data_task
from src.utilities.exceptions import InvalidSourceData

def test_parser_with_error():
    with pytest.raises(ValueError):
        json_parser('{AZAZA:12}')


def test_gen_data_task():
    seed(1)
    data = gen_data_task()
    assert data == {"name": "Task3", "body": "Понять смысл жизни", "status": 2, "priority": 0}

def test_validate():
    with pytest.raises(InvalidSourceData):
        validate({"body": "body", "status": 1, "priority": 4})

    with pytest.raises(InvalidSourceData):
        validate({"name": "body", "status": 1, "priority": 4})

    with pytest.raises(InvalidSourceData):
        validate({"body": "body", "name": "1", "priority": 4})

    with pytest.raises(InvalidSourceData):
        validate({"body": "body", "status": 1, "name": "4"})


def test_filter():
    data = {"name": "Task1", "body": "body", "status": 1, "priority": 1}
    assert not filter(data, name="NoTask1", status=None, priority=None)
    assert not filter(data, name=None, status=2, priority=None)
    assert not filter(data, name=None, status=None, priority=2)
    assert filter(data, name=None, status=None, priority=None)
