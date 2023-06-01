import json
from typing import Optional

from app.core.src.models.task import Task
from app.core.src.repository.task_repository import TaskRepository


class JsonTaskRepository(TaskRepository):
    def __init__(self, file_path):
        self.file_path = file_path

    def create(self, task: Task):
        tasks = self._load_tasks()
        tasks[task.task_id] = task.description
        self._save_tasks(tasks)
        return task

    def find_by_id(self, task_id: str) -> Optional[Task]:
        tasks = self._load_tasks()
        if task_id in tasks:
            return Task(task_id, tasks[task_id])
        return None

    def edit(self, updated_task: Task):
        tasks = self._load_tasks()
        if updated_task.task_id in tasks:
            tasks[updated_task.task_id] = updated_task.description
            self._save_tasks(tasks)
            return updated_task
        return None

    def delete(self, delete_task: Task):
        tasks = self._load_tasks()
        if delete_task.task_id in tasks:
            del tasks[delete_task.task_id]
            self._save_tasks(tasks)
            return True
        return None
    
    def list_all(self) -> Optional[Task]:
        tasks = self._load_tasks()
        return [Task(task_id, description) for task_id, description in tasks.items()]

    def _load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = {}
        return tasks

    def _save_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file)
