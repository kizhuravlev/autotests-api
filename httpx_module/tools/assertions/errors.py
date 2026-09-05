from httpx_module.clients.files.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema
from httpx_module.tools.assertions.base import assert_equal, assert_length

def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")

def assert_validation_response_error(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details): 
        assert_validation_error(actual.details[index], detail)