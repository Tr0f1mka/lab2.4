import pytest  #type: ignore
from random import seed

from src.sources.generator_tasks import GeneratorSource
from src.task.task import Task


@pytest.mark.asyncio
async def test_gen_tasks():
    seed(1)

    async for i in GeneratorSource().get_tasks():
        assert isinstance(i, Task)
