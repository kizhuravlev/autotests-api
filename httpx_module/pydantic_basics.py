import uuid

from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_user_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(default="Factory")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile", default=None, )
    estimate_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser", default=None)

course_default_model = CourseSchema(
    maxScore=10,
    minScore=1,
    description="Playwright",
    previewFile=FileSchema(
        id="id",
        filename="filename",
        directory="dir",
        url="http://localhost:8000",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="id",
        email="test@example.com",
        lastName="Last",
        firstName="First",
        middleName="Middle",
    ),
)

print("Course default model:", course_default_model)


course_dict = {
    "id": "id",
    "title": "Playwright",
    "maxScore": 10,
    "minScore": 1,
    "description": "Playwright",
    "previewFile": {
        "id": "id",
        "url": "http://localhost:8000",
        "filename": "filename",
        "directory": "dir",
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "id",
        "email": "test@example.com",
        "lastName": "Last",
        "firstName": "First",
        "middleName": "Middle",
    },
}

course_dict_model = CourseSchema(**course_dict)
print("Course dict model:", course_dict_model)

course_json = """
{
    "id": "id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 1,
    "description": "Playwright",
    "previewFile": {
        "id": "id",
        "url": "http://localhost:8000",
        "filename": "filename",
        "directory": "dir"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "id",
        "email": "test@example.com",
        "lastName": "Last",
        "firstName": "First",
        "middleName": "Middle"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course json model:", course_json_model)