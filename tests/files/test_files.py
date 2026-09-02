import pytest
from http import HTTPStatus

from fixtures.files import FileFixture
from fixtures.users import function_user
from httpx_module.clients.files.files_client import FilesClient
from httpx_module.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from httpx_module.tools.assertions.base import assert_status_code
from httpx_module.tools.assertions.files import assert_create_file_response, assert_get_file_response
from httpx_module.tools.assertions.schema import validate_json_schema

@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient, function_files: FileFixture):
        request = CreateFileRequestSchema(upload_file="testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), function_files.response.model_json_schema())

    def test_get_file(self, files_client: FilesClient, function_files: FileFixture):
        response = files_client.get_file_api(function_files.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_files.response)

        validate_json_schema(response.json(), function_files.response.model_json_schema())

        