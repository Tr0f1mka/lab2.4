from dataclasses import dataclass
from uuid import uuid4

from src.parser import json_parser

@dataclass()
class Task:
    """
    Задача
    """
    id: str
    name: str
    body: str
    status: int
    priority: int

    def __str__(self) -> str:
        """
        Преобразует задачу в строку
        :return: Строка - результат
        """
        return f"Task( id: {self.id}, name: {self.name}, body: {self.body}, status: {self.status}, priority: {self.priority} )"

    @classmethod
    def create(cls, json_str: str) -> "Task | None":
        """
        Создание задачи
        :param json_form: строка - данные задачи
        :return: Задача
        """
        json_form = json_parser(json_str)
        return cls(
            id = str(uuid4()),
            name = str(json_form.get("name", "")),
            body = str(json_form.get("body", "")),
            status = int(json_form.get("status", 0)),
            priority = int(json_form.get("priority", 1))
        )
