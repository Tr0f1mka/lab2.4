from typing import TYPE_CHECKING

from src.utilities.logger import logger
from src.utilities.exceptions import (SetAtrTaskException,
                            DelAtrTaskException)
from src.settings.constants import PRIORITIES, STATUS
if TYPE_CHECKING:
    from src.task.task import Task


class ImmutableStrDescriptor:
    """
    Дескриптор неизменяемого атрибута задачи типа строка: запрещает изменения
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        :param cls: Класс для дескриптора
        :param name: Имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> str:
        """
        Геттер атрибута
        :param instance: Экземпляр класса
        :param cls: Класс для дескриптора
        """
        logger.info(f"GET {self.name}")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: str) -> None:
        """
        Сеттер атрибута
        :param instance: Экземпляр класса
        :param value: Строка с новым значением
        """
        logger.info(f"SET ID: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise SetAtrTaskException(f"{self.name} есть только в существуюшей задаче")
        if hasattr(instance, self.private_name):
            logger.error(f"{self.name} already set")
            raise SetAtrTaskException(f"Нельзя менять {self.name} задачи")
        if not isinstance(value, str) or value.strip() == "":
            logger.error("Incorrect value")
            raise SetAtrTaskException("Некорректное значение атрибута")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер атрибута
        :param instance: Экземпляр задачи
        """
        logger.error("DEL ID")
        raise DelAtrTaskException("Нельзя удалять ID задачи")


class PriorityDescriptor:
    """
    Дескриптор приоритета: можно смотреть и менять
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> int:
        """
        Геттер для priority
        """
        logger.info("GET priority")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: int) -> None:
        """
        Сеттер для priority
        """
        logger.info(f"SET priority: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise SetAtrTaskException("Приоритет есть только в существуюшей задаче")
        if not isinstance(value, int):
            logger.error("Incorrect type value")
            raise SetAtrTaskException("Приоритет задачи должен быть числом")
        if value not in PRIORITIES:
            logger.error("Incorrect value")
            raise SetAtrTaskException("Приоритет должен быть от 0 до 4")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для priority
        """
        logger.error("DEL priority")
        raise DelAtrTaskException("Нельзя удалять приоритет задачи")


class StatusDescriptor:
    """
    Дескриптор статуса: можно смотреть и менять
    """

    def __set_name__(self, cls: "type[Task]", name: str) -> None:
        """
        Создаёт имя атрибута
        """
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance: "Task", cls: "type[Task]") -> str:
        """
        Геттер для status
        """
        logger.info("GET status")
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance: "Task", value: int) -> None:
        """
        Сеттер для status
        """
        logger.info(f"SET status: TASK: VALUE: [{value}]")
        if instance is None:
            logger.error("Not defined task")
            raise SetAtrTaskException("Статус есть только в существуюшей задаче")
        if not isinstance(value, int):
            logger.error("Incorrect type value")
            raise SetAtrTaskException("Статус задачи должен быть числом")
        if value not in STATUS:
            logger.error("Incorrect value")
            raise SetAtrTaskException("Статус должен быть от 0 до 4")
        setattr(instance, self.private_name, value)
        logger.info("SUCCES")

    def __delete__(self, instance: "Task") -> None:
        """
        Делитер для status
        """
        logger.error("DEL status")
        raise DelAtrTaskException("Нельзя удалять статус задачи")
