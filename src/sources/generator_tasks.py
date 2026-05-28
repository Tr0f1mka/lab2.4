import asyncio
from typing import AsyncGenerator
import random

from src.task.task import Task
from src.utilities.exceptions import InvalidSourceData, SetAtrTaskException
from src.utilities.create_task_utilities import filter
from src.utilities.gen_data_task import gen_data_task
from src.utilities.logger import logger

class GeneratorSource:
    """
    Программный источник задач
    """

    async def get_tasks(self,
                        name: str | None = None,
                        status: int | None = None,
                        priority: int | None = None
    ) -> AsyncGenerator[Task | None ]:
        """
        Асинхронный программный генератор задач
        :param name: Строка или ничего - нужное имя задач
        :param status: Число или ничего - нужный статус задач
        :param priority: Число или ничего - нужный приоритет задач
        :return: асинхронный генератор задач
        """
        for i in range(random.randint(3, 8)):
            await asyncio.sleep(0)
            try:
                data = gen_data_task()
                if filter(data, name, status, priority):
                    yield Task.create(data)
            except (ValueError, InvalidSourceData, SetAtrTaskException) as e:
                logger.error(e)
                print("Плохая задача начальника, не хочу её делать")
                continue
