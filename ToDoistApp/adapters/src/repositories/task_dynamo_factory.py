import boto3

from ToDoistApp.adapters.src.repositories.dynamo.dynamo_task_repository import DynamoTaskRepository
from ToDoistApp.adapters.src.repositories.task_repository_factory import TaskRepositoryFactory
from ToDoistApp.core.src.repository.task_repository import TaskRepository


class TaskDynamoFactory(TaskRepositoryFactory):

    def get_task_repository(self) -> TaskRepository:
        dynamodb = boto3.resource('dynamodb',
                                  region_name='us-east-1',
                                  aws_access_key_id='your-access-key',
                                  aws_secret_access_key='your-secret-key',
                                  endpoint_url='http://localhost:4566'
                                  )
        table = dynamodb.Table('dev_backend_architecture_table')
        return DynamoTaskRepository(table)
