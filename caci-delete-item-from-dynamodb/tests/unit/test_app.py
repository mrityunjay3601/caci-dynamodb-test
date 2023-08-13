import pytest
from app import lambda_handler


def test_lambda_handler_success():
    # Arrange
    request_event = {"id": "10"}
    expected_response = {
        "statusCode": 200,
        "body": "record has been deleted successfully",
    }

    # Act
    response = lambda_handler(request_event, None)

    # Assert
    assert response == expected_response


def test_lambda_handler_error():
    # Arrange
    request_event = {"Weather": "Sunny"}
    expected_response = {
        "statusCode": 400,
        "body": "please provide id to delete the item",
    }

    # Act
    response = lambda_handler(request_event, None)

    # Assert
    assert response == expected_response
