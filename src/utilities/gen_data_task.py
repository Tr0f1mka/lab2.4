import random

from src.settings.constants import EXAMPLES_TASKS

def gen_data_task() -> dict[str, str | int | None]:
    """
    Генератор данных задачи
    :return: Словарь - данные задачи
    """

    return {"name": f"Task{random.randint(1, 10)}",
            "body": random.choice(EXAMPLES_TASKS),
            "status": random.randint(0, 5),
            "priority": random.randint(0, 5)}
