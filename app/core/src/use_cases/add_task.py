from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository


class AddTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str, description: str) -> str:
        task = Task(task_id=task_id, description=description)

        repository_task = self.task_repository.find_by_id(task_id)

        if repository_task:
            raise Exception('There is a Task with the same id')

        response = self.task_repository.create(task)
        return response.task_id
