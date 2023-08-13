import pytest
from app import lambda_handler
from validate_requests import ValidateRequest


def test_lambda_handler_success():
    # Arrange
    request_event = {"id": "10", "Weather": "Rainy"}
    expected_response = {
        "statusCode": 200,
        "body": "Record has been added successfully",
    }

    # Act
    response = lambda_handler(request_event, None)

    # Assert
    assert response == expected_response


def test_lambda_handler_error():
    # Arrange
    request_event = {"Weather": "Sunny"}
    validate_message = ValidateRequest().validate_request_body(request_event)
    expected_response = {"statusCode": 400, "body": validate_message}

    # Act
    response = lambda_handler(request_event, None)

    # Assert
    assert response == expected_response
