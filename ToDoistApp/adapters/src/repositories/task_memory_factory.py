from ToDoistApp.adapters.src.repositories.memory.memory_task_repository import MemoryTaskRepository
from ToDoistApp.adapters.src.repositories.task_repository_factory import TaskRepositoryFactory
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class TaskMemoryFactory(TaskRepositoryFactory):

    def get_task_repository(self) -> TaskRepository:
        return MemoryTaskRepository()
