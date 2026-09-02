from pydantic import BaseModel
import pytest

from fixtures.users import UserFixture
from httpx_module.clients.files.files_client import FilesClient, get_files_client
from httpx_module.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema

class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(user=function_user.authentication_user)

@pytest.fixture
def function_files(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)