import pytest              #type: ignore
import tempfile

from src.sources.file_source import FileSource


@pytest.mark.asyncio
async def test_read():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write('{"name": "task1", "body": "create", "priority": 2, "status": 1}\n')
        f.write('{"name": "task2", "body": "create", "priority": 2, "status": 1}\n')
        f.write('\n')
        f.write('{"bad_task":1}\n')
        f.write('{"name": "task3", "body": "create", "priority": 2, "status": 1}\n')
        file = f.name

    tasks = []
    async for i in FileSource(file).get_tasks():
        tasks.append(i)
    assert len(tasks) == 3
    assert tasks.count(None) == 0
    assert tasks[0].name == "task1"
    assert tasks[1].name == "task2"
    assert tasks[2].name == "task3"
