from ToDoistApp.adapters.src.repositories.task_json_factory import TaskJsonFactory
from ToDoistApp.adapters.src.repositories.task_memory_factory import TaskMemoryFactory
from ToDoistApp.core.src.repository.task_repository import TaskRepository
from ToDoistApp.core.src.use_cases.add_task import AddTask
from ToDoistApp.core.src.use_cases.edit_task import EditTask


def create_task(repository: TaskRepository) -> None:
    create_client_use_case: AddTask = AddTask(repository)

    task_id: str = input('Enter task id: ')
    description: str = input('Enter task description: ')

    try:
        task_id = create_client_use_case.execute(task_id, description)
        print('ID', task_id)
        print('Task created successfully!')
    except Exception as error:
        print(str(error))

def edit_task(repository: TaskRepository) -> None:
    edit_client_use_case: EditTask = EditTask(repository)

    task_id: str = input('Enter task id to search: ')
    description: str = input('Enter new description')

    try:
        description = edit_client_use_case.execute(task_id, description)
        print('Task Edited' , task_id)
        print('Task Description edited ' , description)
    except Exception as error:
        print(str(error))

if __name__ == '__main__':
    while True:
        print('Task Management')
        print('1. Create Task')
        print('2. Edit Task')
        print('3. Exit')

        choice: str = input('Enter your choice: ')

        if choice == '3':
            print('Thanks for coming!')
            break

        options = {
            '1': create_task,
            '2': edit_task,
        }

        selected_option = options.get(choice, None)

        if selected_option:
            task_repository = TaskJsonFactory().get_task_repository()
            selected_option(task_repository)
        else:
            print('Invalid choice. Please try again.')
