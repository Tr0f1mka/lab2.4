from src.sources.task_source_contract import TaskSource
from src.sources.file_source import FileSource
from src.sources.generator_tasks import GeneratorSource

def test_type_source():
    assert isinstance(GeneratorSource, TaskSource)
    assert isinstance(FileSource, TaskSource)
