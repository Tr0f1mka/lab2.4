import asyncio
from dataclasses import dataclass
from random import random
from uuid import uuid4

from src.settings.constants import STATUS
from src.task.descriptors import (ImmutableStrDescriptor,
                             StatusDescriptor,
                             PriorityDescriptor)


@dataclass()
class Task:
    """
    Задача
    """
    id = ImmutableStrDescriptor()
    name = ImmutableStrDescriptor()
    body = ImmutableStrDescriptor()
    status = StatusDescriptor()
    priority = PriorityDescriptor()

    def __init__(self, id: str, name: str, body: str, status: int, priority: int):
        self.id = id
        self.name = name
        self.body = body
        self.status = status
        self.priority = priority

    def __str__(self) -> str:
        """
        Преобразует задачу в строку
        :return: Строка - результат
        """
        return f"Task( id: {self.id}, name: {self.name}, body: {self.body}, status: {self.status}, priority: {self.priority} )"

    def short(self) -> str:
        """
        Преобразует задачу в короткую строку
        :return: Строка - результат
        """
        return f"Task( name: {self.name} )"

    @classmethod
    def create(cls, data: dict) -> "Task | None":
        """
        Создание задачи
        :param json_form: строка - данные задачи
        :return: Задача
        """
        return cls(
            id = str(uuid4()),
            name = data.get("name"),        #type: ignore
            body = data.get("body"),        #type: ignore
            status = data.get("status"),    #type: ignore
            priority = data.get("priority") #type: ignore
        )

    async def run(self) -> None:
        """
        Запуск выполнения задачи (заглушка)
        """
        if self.status == STATUS.COMPLETED:
            return
        await asyncio.sleep(random()*5)
        self.status = int(STATUS.COMPLETED)
        print(f"Я сделать задача {self.short()}, начальника!")
