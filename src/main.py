import asyncio

from src.async_sheduler import Sheduler


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    asyncio.run(Sheduler().run())


if __name__ == "__main__":
    main()
