from httpx_module.clients.auth.auth_client import LoginRequestSchema
from httpx_module.clients.users.users_schema import CreateUserRequestSchema
from httpx_module.clients.users.public_users_client import get_public_users_client
from httpx_module.tools.fakers import random_user_email
from httpx_module.clients.files.files_client import get_files_client, CreateFileRequestDict
from httpx_module.clients.courses.courses_client import get_courses_client, CreateCoursesRequestDict

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=random_user_email(),
    password="Password123!",
    last_name="string",
    first_name="string",
    middle_name="string",
)
create_user_data = public_users_client.create_user(create_user_request)
print(f"Create user data: {create_user_data}")

user = LoginRequestSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

create_files_client = get_files_client(user)
create_files_request = CreateFileRequestDict(
    filename="file",
    directory='files',
    upload_file='./testdata/files/image.png',
)
create_files_data = create_files_client.create_file(create_files_request)
print(f"Create files data: {create_files_data}")

create_course_client = get_courses_client(user)
create_course_request = CreateCoursesRequestDict(
    title="Python",
    maxScore=100,
    minScore=1,
    description="Python API Course",
    estimatedTime="100 days",
    previewFileId=create_files_data["file"]["id"],
    createdByUserId=create_user_data["user"]["id"],
)
create_course_data = create_course_client.create_course(create_course_request)
print(f"Create course data: {create_course_data}")