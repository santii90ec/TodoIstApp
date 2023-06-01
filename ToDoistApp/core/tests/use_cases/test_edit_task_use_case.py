from ToDoistApp.adapters.src.repositories.memory.memory_task_repository import MemoryTaskRepository
from ToDoistApp.core.src.repository.task_repository import TaskRepository
from ToDoistApp.core.src.use_cases.add_task import AddTask
from ToDoistApp.core.src.use_cases.edit_task import EditTask



def test_edit_use_case():
    #Arrange
    task_repository: TaskRepository = MemoryTaskRepository()
    add_task_use_case = AddTask(task_repository)
    edit_task_use_case = EditTask(task_repository)
    task_id = 'TaskId'
    description = 'Original Task'
    #Act
    response = add_task_use_case.execute(task_id, description)
    description = 'Task Edited' 
    response = edit_task_use_case.execute(task_id, description)
    #Assert
    assert response == description

    