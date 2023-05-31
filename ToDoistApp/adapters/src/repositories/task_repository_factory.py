from abc import ABC, abstractmethod

from ToDoistApp.core.src.repository.task_repository import TaskRepository


class TaskRepositoryFactory(ABC):

    @abstractmethod
    def get_task_repository(self) -> TaskRepository:
        raise NotImplementedError
