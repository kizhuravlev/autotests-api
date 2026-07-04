from httpx_module.clients.api_client import APIClient
from httpx_module.clients.auth.auth_client import LoginRequestDict
from httpx_module.clients.private_http_builder import get_private_http_client

from typing import TypedDict

from httpx import Response

class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: str
    
class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа на создание файла.
    """
    file: File

class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/files", data=request, files={
            "upload_file": open(request["upload_file"], "rb")
        })
    
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")
    
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Метод создания файла с возвращаемой структурой json()

        :return: Возвращает данные созданного файла в json()
        """
        response = self.create_file_api(request)
        return response.json()
    
def get_files_client(user: LoginRequestDict) -> FilesClient:
    """
    Функция создает и настраивает готовый FilesClient

    :return: Возвращает настроенный готовый FilesClient
    """
    return FilesClient(client=get_private_http_client(user=user))