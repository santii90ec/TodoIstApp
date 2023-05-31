from abc import ABC, abstractmethod
from typing import Optional

from ToDoistApp.core.src.models.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def find_by_id(self, task_id: str) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def create(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def edit(self, task: Task) -> Optional[Task]:
        raise NotImplementedError


    

