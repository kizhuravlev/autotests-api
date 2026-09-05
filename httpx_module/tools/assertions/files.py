from httpx_module.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from httpx_module.clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from httpx_module.pydantic_basics import FileSchema
from httpx_module.tools.assertions.base import assert_equal
from httpx_module.tools.assertions.errors import assert_validation_response_error, assert_internal_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.url, expected.url, "url")

def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(get_file_response.file, create_file_response.file)

def assert_create_file_with_empty_filename(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                location=["body", "filename"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )
    assert_validation_response_error(actual, expected)

def assert_create_file_with_empty_directory(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
            details=[
                ValidationErrorSchema(
                    type="string_too_short",
                    location=["body", "directory"],
                    message="String should have at least 1 character",
                    input="",
                    context={"min_length": 1}
                )
            ]
        )
    assert_validation_response_error(actual, expected)

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(detail="File not found")

    assert_internal_error_response(actual, expected)

def assert_get_file_with_incorrect_file_id(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}
            )
        ]
    )

    assert_validation_response_error(actual, expected)
    