from pydantic import BaseModel
import pytest

from fixtures.files import FileFixture
from fixtures.users import UserFixture
from httpx_module.clients.courses.courses_client import CoursesClient, get_courses_client
from httpx_module.clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)

@pytest.fixture
def function_course(
    courses_client: CoursesClient,
    function_user: UserFixture,
    function_files: FileFixture
    ) -> CourseFixture:
    request = CreateCourseRequestSchema(
        previewFileId=function_files.response.file.id,
        createdByUserId=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)