from json import loads, JSONDecodeError

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
