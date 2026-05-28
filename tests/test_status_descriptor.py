import pytest  # type: ignore

from src.task.task import Task
from src.task.descriptors import StatusDescriptor
from src.utilities.exceptions import SetAtrTaskException, DelAtrTaskException

def test_get():

    test_task = Task("id", "test1", "Сделать эту лабораторную работу", 3, 1)
    assert test_task.status == 3
    assert type(Task.status) is StatusDescriptor

def test_set():

    test_task = Task("id", "test1", "Сделать эту лабораторную работу", 3, 1)
    with pytest.raises(SetAtrTaskException):
        test_task.status = "id1"

def test_incorrect_value():
    with pytest.raises(SetAtrTaskException):
        Task("id", "rfrgr", "Сделать эту лабораторную работу", "3", 1)
    with pytest.raises(SetAtrTaskException):
        Task("id", "1", "Сделать эту лабораторную работу", None, 1)
    with pytest.raises(SetAtrTaskException):
        Task("id", "1", "Сделать эту лабораторную работу", 22, 1)


def test_del():
    test_task = Task("id", "test1", "Сделать эту лабораторную работу", 3, 1)
    with pytest.raises(DelAtrTaskException):
        del test_task.status
