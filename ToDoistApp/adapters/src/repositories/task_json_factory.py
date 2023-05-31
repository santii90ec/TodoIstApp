from ToDoistApp.adapters.src.repositories.json.json_task_repository import JsonTaskRepository
from ToDoistApp.adapters.src.repositories.task_repository_factory import TaskRepositoryFactory
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class TaskJsonFactory(TaskRepositoryFactory):

    def get_task_repository(self) -> TaskRepository:
        path:str = '/Users/santiagoatapuma/Workspace/BackEndArchi/TodoIstApp/infrastructure/BD.json'
        return JsonTaskRepository(path)
    