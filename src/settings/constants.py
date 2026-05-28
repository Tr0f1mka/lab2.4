from enum import IntEnum

class STATUS(IntEnum):
    CREATED = 0
    IN_WORK = 1
    ON_REVIEW = 2
    ON_DEBUG = 3
    COMPLETED = 4

class PRIORITIES(IntEnum):
    COMPLETED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EXTRA_HIGH = 4

EXAMPLES_TASKS = [
    "Сделать лабу",
    "Понять смысл жизни",
    "Расширить длину недели",
    "Сделать вёрстку сайта",
    "Изучить Angular",
    "Пережить семестр",
    "Отдохнуть",
    "Дописать клон Undertale",
    "Придумать ещё примеры задач для генератора"
]
