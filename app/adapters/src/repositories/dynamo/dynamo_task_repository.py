from typing import Optional

from app.adapters.src.repositories.dynamo.operations import put_item, get_item, update_item
from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository


class DynamoTaskRepository(TaskRepository):

    def __init__(self, table):
        self.table = table

    def find_by_id(self, task_id: str) -> Optional[Task]:
        key = {
            'ID': task_id,
        }
        item = get_item(self.table, key)

        if not item:
            return None

        return Task(task_id=item.get('ID'), description=item.get('description'))

    def create(self, task: Task) -> Optional[Task]:
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

    def edit(self, task: Task) -> Optional[Task]:
        taskDict = {
            'ID': task.task_id,
        }
        updateexpression:str = 'SET description = val1'

        update_item(
            self.table,
            taskDict,
            updateexpression,
            {
                'val1': task.description
            },
            {'#attr1': 'description'}

        )
        return self.find_by_id(task.task_id)
