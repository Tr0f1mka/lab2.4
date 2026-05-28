import asyncio

from src.sources.file_source import FileSource
from src.sources.generator_tasks import GeneratorSource


class Sheduler:
    """
    Исполнитель задач
    """

    tasks: list

    def __init__(self) -> None:
        """
        Инициализация класса
        """
        self.tasks = []

    async def run(self) -> None:
        """
        Основная часть исполнителя: асинхронная консоль
        """
        clean_tasks = asyncio.create_task(self.clean_complete_tasks())
        while True:
            cin = await asyncio.to_thread(input, "> ")
            cin = cin.strip()

            if cin == "exit":
                for i in self.tasks:
                    i.cancel()
                self.tasks.clear()
                clean_tasks.cancel()
                break

            elif cin == "":
                continue

            elif cin.startswith("file "):
                cmd = cin.split()
                if len(cmd) != 2:
                    print("Incorrect input")
                    continue
                try:
                    async for i in FileSource(cmd[1]).get_tasks():
                        if i:
                            self.tasks.append(asyncio.create_task(i.run()))
                except FileNotFoundError:
                    print(f"Файла {cmd[1]} не существуют")
                except PermissionError:
                    print("У вас нет прав на этот файл")

            elif cin.startswith("file_name "):
                cmd = cin.split()
                if len(cmd) != 3:
                    print("Incorrect input")
                    continue
                try:
                    async for i in FileSource(cmd[1]).get_tasks(name=cmd[2]):
                        if i:
                            self.tasks.append(asyncio.create_task(i.run()))
                except FileNotFoundError:
                    print(f"Файла {cmd[1]} не существуют")
                except PermissionError:
                    print("У вас нет прав на этот файл")

            elif cin.startswith("file_status "):
                cmd = cin.split()
                if len(cmd) != 3:
                    print("Incorrect input")
                    continue
                try:
                    async for i in FileSource(cmd[1]).get_tasks(status=int(cmd[2])):
                        if i:
                            self.tasks.append(asyncio.create_task(i.run()))
                except FileNotFoundError:
                    print(f"Файла {cmd[1]} не существуют")
                except PermissionError:
                    print("У вас нет прав на этот файл")


            elif cin.startswith("file_priority "):
                cmd = cin.split()
                if len(cmd) != 3:
                    print("Incorrect input")
                    continue
                try:
                    async for i in FileSource(cmd[1]).get_tasks(priority=int(cmd[2])):
                        if i:
                            self.tasks.append(asyncio.create_task(i.run()))
                except FileNotFoundError:
                    print(f"Файла {cmd[1]} не существуют")
                except PermissionError:
                    print("У вас нет прав на этот файл")

            elif cin == "gen":
                async for i in GeneratorSource().get_tasks():
                    if i:
                        self.tasks.append(asyncio.create_task(i.run()))

            elif cin.startswith("gen_name "):
                cmd = cin.split()
                if len(cmd) != 2:
                    print("Incorrect input")
                    continue
                async for i in GeneratorSource().get_tasks(name=cmd[1]):
                    if i:
                        self.tasks.append(asyncio.create_task(i.run()))

            elif cin.startswith("gen_status "):
                cmd = cin.split()
                if len(cmd) != 2:
                    print("Incorrect input")
                    continue
                async for i in GeneratorSource().get_tasks(status=int(cmd[1])):
                    if i:
                        self.tasks.append(asyncio.create_task(i.run()))

            elif cin.startswith("gen_priority "):
                cmd = cin.split()
                if len(cmd) != 2:
                    print("Incorrect input")
                    continue
                async for i in GeneratorSource().get_tasks(priority=int(cmd[1])):
                    if i:
                        self.tasks.append(asyncio.create_task(i.run()))

            elif cin == "list":
                for i in self.tasks:
                    print(i)

            else:
                print("Incorrect input")


    async def clean_complete_tasks(self):
        """
        Фоновый очиститель выполненных задач из массива
        """
        while True:
            await asyncio.sleep(3)
            self.tasks = [i for i in self.tasks if not i.done()]
