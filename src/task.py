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

    def short(self) -> str:
        """
        Преобразует задачу в короткую строку
        :return: Строка - результат
        """
        return f"Task( name: {self.name} )"

    @classmethod
    def create(cls, json_str: str) -> "Task | None":
        """
        Создание задачи
        :param json_form: строка - данные задачи
        :return: Задача
        """
        json_form = json_parser(json_str)
        if json_form.get("name") is None or json_form.get("name") is None or json_form.get("name") is None or json_form.get("name") is None:
            raise ValueError
        return cls(
            id = str(uuid4()),
            name = str(json_form.get("name")),        #type: ignore
            body = str(json_form.get("body")),        #type: ignore
            status = int(json_form.get("status")),    #type: ignore
            priority = int(json_form.get("priority")) #type: ignore
        )
