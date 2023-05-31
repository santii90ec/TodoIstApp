import json
from typing import Optional

from ToDoistApp.core.src.models.task import Task
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class JsonTaskRepository(TaskRepository):
    def __init__(self, file_path):
        self.file_path = file_path

    def create(self, task):
        tasks = self._load_tasks()
        tasks.append(task)
        self._save_tasks(tasks)
        return task

    def find_by_id(self, task_id: str) -> Optional[Task]:
        tasks = self._load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                return task
        return None

    def read_task(self, task_id):
        tasks = self._load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                return task
        return None

    def edit(self, updated_task: Task):
        tasks = self._load_tasks()
        for i, task in tasks:
            if task['id'] == task.task_id:
                tasks[i] = updated_task
                self._save_tasks(tasks)
                return True
        return False

    def delete_task(self, task_id):
        tasks = self._load_tasks()
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                del tasks[i]
                self._save_tasks(tasks)
                return True
        return False

    def _load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def _save_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)
