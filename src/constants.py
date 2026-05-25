from enum import IntEnum

class STATUS(IntEnum):
    CREATED = 0
    IN_WORK = 1
    ON_REVIEW = 2
    ON_DEBUG = 3
    COMPLETED = 4
