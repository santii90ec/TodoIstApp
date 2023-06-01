from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository

class ListTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self) -> TaskRepository:
        repository_task = self.task_repository.list_all()
        return repository_task