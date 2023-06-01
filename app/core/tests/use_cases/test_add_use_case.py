from app.adapters.src.repositories.memory.memory_task_repository import MemoryTaskRepository
from app.core.src.repository.task_repository import TaskRepository
from app.core.src.use_cases.add_task import AddTask


def test_add_use_case():
    #Arrange
    task_repository: TaskRepository = MemoryTaskRepository()
    add_task_use_case = AddTask(task_repository)
    task_id = 'TASK_ID'
    description = 'Test task description'
    #Act
    response = add_task_use_case.execute(task_id, description)
    #Assert
    assert response == task_id
