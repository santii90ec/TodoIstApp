from typing import List

from ToDoistApp.core.src.models.task import Task
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class MemoryTaskRepository(TaskRepository):

    tasks: List[Task]

    def __init__(self):
        self.tasks = []

    def find_by_id(self, task_id: str):
        return next((task for task in self.tasks if task.task_id == task_id), None)

    def create(self, task: Task):
        self.tasks.append(task)
        return task
