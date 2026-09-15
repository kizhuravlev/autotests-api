from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict

class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestDataConfig(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter=".",
        env_file_encoding="utf-8",
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig

settings = Settings()