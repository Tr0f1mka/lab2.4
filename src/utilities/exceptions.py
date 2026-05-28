class SetAtrTaskException(Exception):
    """
    Ошибка установки атрибута задачи
    """
    pass

class DelAtrTaskException(Exception):
    """
    Ошибка удаления атрибута задачи
    """
    pass

class InvalidSourceData(Exception):
    """
    Ошибка некорректных данных для задачи
    """
    pass
