from typing import List, Optional

from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository


class MemoryTaskRepository(TaskRepository):

    tasks: List[Task]
    updatedTasks: List[Task]

    def __init__(self):
        self.tasks = []
        self.updatedTasks = []

    def find_by_id(self, task_id: str) -> Optional[Task]:
        return next((task for task in self.tasks if task.task_id == task_id), None)

    def create(self, task: Task) -> Optional[Task]:
        self.tasks.append(task)
        return task
    
    def edit(self, task: Task) -> Optional[Task]:
        self.updatedTasks.append(task)
        return task

    def list_all(self) -> Optional[Task]:
        pass

    def delete(self, task: Task) -> Optional[Task]:
        pass
