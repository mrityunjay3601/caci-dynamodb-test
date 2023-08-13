class ValidateRequest:
    def validate_request_body(self, request_body):
        allowed_attributes = ["id", "Weather"]
        invalid_attributes = [
            attr for attr in request_body.keys() if attr not in allowed_attributes
        ]
        missing_fields = [
            field for field in allowed_attributes if field not in request_body
        ]

        error_message = ""

        if invalid_attributes:
            error_message = f"Invalid attributes found: {', '.join(invalid_attributes)}"

        if missing_fields:
            missing_fields_message = (
                f"Required fields not passed: {', '.join(missing_fields)}"
            )
            error_message = (
                error_message + " and " + missing_fields_message
                if error_message
                else missing_fields_message
            )

        return error_message
