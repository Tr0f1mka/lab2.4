import asyncio
from random import random

from src.async_source import FileSource
from src.task import Task
from src.constants import STATUS


class Sheduler:
    tasks: list

    def __init__(self):
        self.tasks = []

    async def main(self) -> None:
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

            elif cin.startswith("add_source"):
                cmd = cin.split()
                if len(cmd) != 2:
                    print("Incorrect input")
                try:
                    async for i in FileSource(cmd[1]):
                        if i:
                            self.tasks.append(asyncio.create_task(self.create_task(i)))
                except FileNotFoundError:
                    print(f"Файла {cmd[1]} не существуют")
                except PermissionError:
                    print("У вас нет прав на этот файл")

            elif cin == "list":
                for i in self.tasks:
                    print(i)

            else:
                print("Incorrect input")

    async def create_task(self, task: Task) -> None:
        if task.status == STATUS.COMPLETED:
            return
        await asyncio.sleep(random()*5)
        task.status = int(STATUS.COMPLETED)
        print(f"Я сделать задача {task.short()}, начальника!")

    async def clean_complete_tasks(self):
        while True:
            await asyncio.sleep(3)
            self.tasks = [i for i in self.tasks if not i.done()]
