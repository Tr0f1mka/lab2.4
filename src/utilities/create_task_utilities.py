from json import loads, JSONDecodeError

from src.utilities.exceptions import InvalidSourceData


def json_parser(data: str) -> dict[str, str|int]:
    """
    Парсит строку в json
    :param data: Строка, которую нужно распарсить
    :return: JSON-формат
    """
    try:
        return loads(data)
    except JSONDecodeError:
        raise ValueError

def validate(data: dict) -> None:
        """
        Проверка наличия данных задачи
        :param data: Словарь - атрибуты задачи
        """
        if data.get("name") is None:
            raise InvalidSourceData("Отсутствует поле name")
        if data.get("body") is None:
            raise InvalidSourceData("Отсутствует поле body")
        if data.get("status") is None:
            raise InvalidSourceData("Отсутствует поле status")
        if data.get("priority") is None:
            raise InvalidSourceData("Отсутствует поле priority")


def filter(data: dict,
               name: str | None,
               status: int | None,
               priority: int | None
    ) -> bool:
        """
        Фильтр задач
        :param data: Словарь - атрибуты задачи
        :param name: Строка или пустота - нужное имя
        :param status: Число или пустота - нужный статус
        :param priority: Число или пустота - нужный приоритет
        :return: Подходит задача или нет
        """
        if name and data.get("name", "") != name:
            return False
        if status and data.get("status", 0) != status:
            return False
        if priority and data.get("priority", 0) != priority:
            return False
        return True
