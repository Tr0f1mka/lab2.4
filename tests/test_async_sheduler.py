import pytest   #type: ignore
import asyncio
from unittest.mock import patch, Mock

from src.async_sheduler import Sheduler
from src.task import Task
from src.constants import STATUS

@pytest.mark.asyncio
async def test_create_task():
    sheduler = Sheduler()

    task = Task(id="ERt", name="YJYJ", body="g5h5", status=2, priority=2)
    await sheduler.create_task(task)
    assert task.status == STATUS.COMPLETED

    task = Task(id="ERt", name="YJYJ", body="g5h5", status=4, priority=2)
    await sheduler.create_task(task)
    assert task.status == STATUS.COMPLETED


async def fast_task():
    await asyncio.sleep(0.1)
    return "done"


async def slow_task():
    await asyncio.sleep(20)
    return "done"


@pytest.mark.asyncio
async def test_clean_complete_task():

    sheduler = Sheduler()
    task1 = asyncio.create_task(fast_task())
    task2 = asyncio.create_task(slow_task())

    sheduler.tasks = [task1, task2]

    cleaner = asyncio.create_task(sheduler.clean_complete_tasks())

    await asyncio.sleep(3.1)

    assert len(sheduler.tasks) == 1
    assert sheduler.tasks[0] == task2
    cleaner.cancel()
    task2.cancel()


@pytest.mark.asyncio
async def test_list():
    sheduler = Sheduler()

    task1 = Mock()
    task2 = Mock()
    task1.__str__ = Mock(return_value="Mock")
    task2.__str__ = Mock(return_value="Mock")
    sheduler.tasks = [task1, task2]

    with patch('asyncio.to_thread') as mock_input:
        mock_input.side_effect = ["list", "exit"]
        main = asyncio.create_task(sheduler.run())
        await asyncio.sleep(0.3)
        main.cancel()
    task1.__str__.assert_called()
    task2.__str__.assert_called()


@pytest.mark.asyncio
async def test_exit():
    sheduler = Sheduler()

    task = asyncio.create_task(slow_task())
    sheduler.tasks = [task]

    with patch('asyncio.to_thread') as mock_input:
        mock_input.side_effect = ["exit"]
        main = asyncio.create_task(sheduler.run())
        await asyncio.sleep(0.3)
        assert main.done()
        assert task.done()
