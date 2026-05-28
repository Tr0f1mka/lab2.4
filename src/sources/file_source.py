import aiofiles                          #type: ignore
from typing import AsyncGenerator

from src.task.task import Task
from src.utilities.exceptions import InvalidSourceData, SetAtrTaskException
from src.utilities.create_task_utilities import json_parser, validate, filter
from src.utilities.logger import logger

class FileSource:
    """
    Файловый источник задач
    """
    filename: str

    def __init__(self, filename: str) -> None:
        """
        Инициализация задачи
        :param filename: Строка - имя файла
        """
        self.filename = filename

    async def get_tasks(self,
                        name: str | None = None,
                        status: int | None = None,
                        priority: int | None = None
    ) -> AsyncGenerator[Task | None ]:
        """
        Асинхронный генератор задач из файла
        :param name: Строка или ничего - нужное имя задач
        :param status: Число или ничего - нужный статус задач
        :param priority: Число или ничего - нужный приоритет задач
        :return: асинхронный генератор задач
        """
        async with aiofiles.open(self.filename, "r", encoding="utf-8") as f:
            async for i in f:
                if i.strip():
                    try:
                        data = json_parser(i)
                        validate(data)
                        if filter(data, name, status, priority):
                            yield Task.create(data)
                    except (ValueError, InvalidSourceData, SetAtrTaskException) as e:
                        logger.error(e)
                        print("Плохая задача начальника, не хочу её делать")
                        continue
