from ToDoistApp.core.src.models.task import Task
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class AddTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str, description: str) -> str:
        task = Task(task_id=task_id, description=description)
        response: Task = self.task_repository.create(task)
        return response.task_id
