from app.adapters.src.repositories.json.json_task_repository import JsonTaskRepository
from app.adapters.src.repositories.task_repository_factory import TaskRepositoryFactory
from app.core.src.repository.task_repository import TaskRepository


class TaskJsonFactory(TaskRepositoryFactory):

    def get_task_repository(self) -> TaskRepository:
        path:str = '/Users/santiagoatapuma/Workspace/BackEndArchi/TodoIstApp/infrastructure/BD.json'
        return JsonTaskRepository(path)
    