import boto3

from ToDoistApp.adapters.src.repositories.dynamo.dynamo_task_repository import DynamoTaskRepository
from ToDoistApp.core.src.use_cases.add_task import AddTask

dynamodb = boto3.resource('dynamodb',
                          region_name='us-east-1',
                          aws_access_key_id='your-access-key',
                          aws_secret_access_key='your-secret-key',
                          endpoint_url='http://localhost:4566'
                          )
table = dynamodb.Table('dev_backend_architecture_table')


def create_task() -> None:
    task_repository = DynamoTaskRepository(table)
    create_client_use_case: AddTask = AddTask(task_repository)

    task_id: str = input('Enter task id: ')
    description: str = input('Enter task description: ')

    task_id = create_client_use_case.execute(task_id, description)
    print('ID', task_id)
    print('Task created successfully!')


if __name__ == '__main__':
    while True:
        print('1. Create Task')
        print('2. Exit')

        choice: str = input('Enter your choice: ')

        if choice == '1':
            create_task()
        elif choice == '2':
            print('Exiting CLI...')
            break
        else:
            print('Invalid choice. Please try again.')
