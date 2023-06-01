from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository

class DeleteTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository
    
    def execute(self, task_id: str):
        task_to_delete = self.task_repository.find_by_id(task_id)
        if task_to_delete is None:
            raise Exception('There is no Task to Delete')
        response = self.task_repository.delete(task_to_delete)
        return response
