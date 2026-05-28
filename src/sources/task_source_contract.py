from typing import Protocol, runtime_checkable, AsyncGenerator

from src.task.task import Task


@runtime_checkable
class TaskSource(Protocol):
    """
    Класс источника. Задаёт общие контракты get_tasks и create_source для всех источников
    """

    async def get_tasks(self,
                        name: str | None = None,
                        status: int | None = None,
                        priority: int | None = None
    ) -> AsyncGenerator[Task | None ]:
        ...
