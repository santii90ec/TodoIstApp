from typing import Optional

from botocore.exceptions import ClientError


def get_item(
        table,
        key: dict,
        project_expression: Optional[str] = None
):
    get_item_options = {}

    if project_expression:
        get_item_options['ProjectionExpression'] = project_expression

    response = table.get_item(
        Key=key,
        **get_item_options
    )

    return response.get('Item')


def query(
        table,
        key_condition_expression: str,
        expression_attribute_names: dict,
        expression_attribute_values: dict,
        scan_index_forward: bool = True,
        index_name: Optional[str] = None,
        project_expression: Optional[str] = None,
        filter_expression: Optional[str] = None,
):
    query_options = {}

    if scan_index_forward:
        query_options['ScanIndexForward'] = scan_index_forward

    if index_name:
        query_options['IndexName'] = index_name

    if project_expression:
        query_options['ProjectionExpression'] = project_expression

    if filter_expression:
        query_options['FilterExpression'] = filter_expression

    response = table.query(
        KeyConditionExpression=key_condition_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        **query_options
    )
    return response


def put_item(
        table,
        item: dict,
        return_values: Optional[str] = 'ALL_OLD',
        condition_expression: Optional[str] = None
):
    put_item_options = {}

    if condition_expression:
        put_item_options['ConditionExpression'] = condition_expression

    try:
        response = table.put_item(
            Item=item,
            ReturnValues=return_values,
            **put_item_options
        )
        return response.get('Attributes')
    except ClientError as error:
        error_code: dict = error.response.get('Error').get('Code')

        if error_code == 'ConditionalCheckFailedException':
            raise Exception('Item does not meet specified condition.')
        raise Exception('An error occurred while trying to create the item.')


def update_item(
        table,
        key: dict,
        update_expression: str,
        expression_attribute_names: dict,
        expression_attribute_values: dict,
        return_values: Optional[str] = 'ALL_NEW',
        condition_expression: Optional[str] = None
):
    update_item_options = {}

    if condition_expression:
        update_item_options['ConditionExpression'] = condition_expression

    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues=return_values,
        **update_item_options
    )

    return response.get('Attributes')
