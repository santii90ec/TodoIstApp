from abc import ABC, abstractmethod

from ToDoistApp.core.src.models.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def find_by_id(self, task_id: str):
        raise NotImplementedError

    @abstractmethod
    def create(self, task: Task):
        raise NotImplementedError
