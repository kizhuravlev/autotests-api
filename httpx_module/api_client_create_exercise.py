from httpx_module.clients.auth.auth_schema import LoginRequestSchema
from httpx_module.clients.users.public_users_client import get_public_users_client
from httpx_module.clients.users.users_schema import CreateUserRequestSchema
from httpx_module.tools.fakers import random_user_email
from httpx_module.clients.files.files_client import get_files_client
from httpx_module.clients.files.files_schema import CreateFileRequestSchema
from httpx_module.clients.courses.courses_client import get_courses_client, CreateCoursesRequestDict
from httpx_module.clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=random_user_email(),
    password="Password123",
    last_name="lastName",
    first_name="firstName",
    middle_name="middleName",
)
create_user_response = public_user_client.create_user(create_user_request)

login_request = LoginRequestSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(login_request)
courses_client = get_courses_client(login_request)
exercises_client = get_exercises_client(login_request)

files_request = CreateFileRequestSchema(
    filename="filename",
    directory="directory",
    upload_file="./testdata/files/image.png",
)
files_response = files_client.create_file(files_request)
print(f"Create file data: {files_response}")

courses_request = CreateCoursesRequestDict(
    title="Course",
    maxScore=100,
    minScore=1,
    description="Description about course",
    estimatedTime="2 weeks",
    previewFileId=files_response.file.id,
    createdByUserId=create_user_response.user.id
)
courses_response = courses_client.create_course(courses_request)
print(f"Create course data: {courses_response}")

exercise_request = CreateExerciseRequestDict(
    title="Exercise",
    courseId=courses_response["course"]["id"],
    maxScore=100,
    minScore=1,
    orderIndex=1,
    description="Description",
    estimatedTime="2 weeks",
)
exercise_response = exercises_client.create_exercise(exercise_request)
print(f"Create exercise data {exercise_response}")