from pydantic import BaseModel, Field

class ShortUserSchema(BaseModel):
    age: int
    is_lox: bool = Field(True, alias="isLox")

class UserSchema(ShortUserSchema):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str

class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema


course = CourseSchema(
    id = "id",
    title = "title",
    maxScore = 100,
    minScore = 1,
    description = "description",
    previewFile = {
        'id': "id",
        "filename": "filename",
        "directory": "directory",
        "url": "url"
    },
    estimatedTime = "2 weeks",
    createdByUser = {
        "id": "id",
        "email": "email",
        "lastName": "lastName",
        "firstName": "firstName",
        "middleName": "middleName",
        "age": 20,
        "isLox": False,
    }
)

print(course.model_dump_json(), type(course))