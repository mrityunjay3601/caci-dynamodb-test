import boto3
import json
import os

# Create a DynamoDB client
dynamodb = boto3.resource("dynamodb")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

def lambda_handler(event, context):
    # Convert the event body into a dictionary
    request_body = json.loads(json.dumps(event))

    # Validate request body
    record_id = validate_request(request_body)

    # if request body validation failed
    if record_id is None:
        return {"statusCode": 400, "body": "please provide id to delete the item"}

    # define the dynamo db table
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)

    # Delete the item with the specified id from the table
    response = table.delete_item(Key={"id": record_id})

    # Validate if ResponseMetadata and HTTPStatusCode in response
    if (
        "ResponseMetadata" in response
        and "HTTPStatusCode" in response["ResponseMetadata"]
    ):
        # Return a response indicating successful deletion
        return {"statusCode": 200, "body": "record has been deleted successfully"}

    # Return a response indicating an error occurred
    return {"statusCode": 400, "body": "something went wrong"}


def validate_request(request_body):
    # Validate if id is present in request body or not -- This code is if request directly came to lambda without api gateway
    record_id = None
    if "id" in request_body:
        # Extract the ID from the request body
        record_id = request_body["id"]
    elif "body" in request_body:
        # Extract the ID from the request body
        record_id = json.loads(request_body["body"])["id"]

    return record_id
