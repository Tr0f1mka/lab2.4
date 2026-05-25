import aiofiles                 #type: ignore
from typing import AsyncGenerator

from src.task import Task

class FileSource:
    filename: str

    def __init__(self, filename: str) -> None:
        self.filename = filename

    async def __aiter__(self) -> AsyncGenerator[Task | None]:
        async with aiofiles.open(self.filename, "r", encoding="utf-8") as f:
            async for i in f:
                if i.strip():
                    try:
                        yield Task.create(i)
                    except ValueError:
                        print("Плохая задача начальника, не хочу её делать")
                        continue
