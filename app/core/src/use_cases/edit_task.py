from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository

class EditTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository
    
    def execute(self, task_id: str, description: str) -> str:
        task = Task(task_id=task_id, description=description)
        response = self.task_repository.edit(task)
        if response is None:
            raise Exception('There is not exist any Task')
        return response.description