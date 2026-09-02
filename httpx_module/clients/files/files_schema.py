from pydantic import BaseModel, Field, HttpUrl

from httpx_module.tools.fakers import fake

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl
    
class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание файла.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение файла.
    """
    file: FileSchema