import boto3
import json
import os
from validate_requests import ValidateRequest

dynamodb_client = boto3.client("dynamodb")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

def lambda_handler(event, context):
    # Convert the event to a JSON string and then load it as a dictionary
    request_body = json.loads(json.dumps(event))

    # Validate the request body
    validate_request = ValidateRequest().validate_request_body(request_body)

    # If validation fails, return a validation error message
    if validate_request != "":
        return {"statusCode": 400, "body": validate_request}

    # Add the weather data to the DynamoDB table
    dynamodb_client.put_item(
        TableName=DYNAMODB_TABLE_NAME,
        Item={
            "id": {"S": request_body["id"]},
            "Weather": {"S": request_body["Weather"]},
        },
    )

    # Return a success message
    return {"statusCode": 200, "body": "Record has been added successfully"}
