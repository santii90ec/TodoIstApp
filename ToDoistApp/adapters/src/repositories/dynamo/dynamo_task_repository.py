from ToDoistApp.adapters.src.repositories.dynamo.operations import put_item, get_item
from ToDoistApp.core.src.models.task import Task
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class DynamoTaskRepository(TaskRepository):

    def __init__(self, table):
        self.table = table

    def find_by_id(self, task_id: str):
        key = {
            'ID': task_id,
        }
        item = get_item(self.table, key)
        return Task(task_id=item.get('ID'), description=item.get('description'))

    def create(self, task: Task):
        task_id = task.task_id
        task = {
            'ID': task_id,
            'description': task.description,
        }
        put_item(
            self.table,
            item=task,
            condition_expression='attribute_not_exists(PK)',
        )
        return self.find_by_id(task_id)
