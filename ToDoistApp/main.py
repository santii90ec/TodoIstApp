from ToDoistApp.adapters.src.repositories.task_dynamo_factory import TaskDynamoFactory
from ToDoistApp.core.src.repository.task_repository import TaskRepository
from ToDoistApp.core.src.use_cases.add_task import AddTask


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


if __name__ == '__main__':
    while True:
        print('Task Management')
        print('1. Create Task')
        print('2. Exit')

        choice: str = input('Enter your choice: ')

        if choice == '2':
            print('Thanks for coming!')
            break

        options = {
            '1': create_task,
        }

        selected_option = options.get(choice, None)

        if selected_option:
            task_repository = TaskDynamoFactory().get_task_repository()
            selected_option(task_repository)
        else:
            print('Invalid choice. Please try again.')
