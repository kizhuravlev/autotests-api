from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings

class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    test_data: TestData
    http_client: HTTPClientConfig