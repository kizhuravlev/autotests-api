from httpx import Response

from httpx_module.clients.api_client import APIClient
from httpx_module.clients.auth.auth_client import LoginRequestSchema
from httpx_module.clients.private_http_builder import get_private_http_client
from httpx_module.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema

import allure

from httpx_module.tools.routes import APIRoutes


class FilesClient(APIClient):
    """
    Клиент для работы с APIRoutes.FILES
    """

    @allure.step("Get file by id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={
                "upload_file": (request.upload_file.name, request.upload_file.read_bytes())
            },
        )

    @allure.step("Delete file by id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Метод создания файла с возвращаемой структурой json()

        :return: Возвращает данные созданного файла в json()
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)
    
def get_files_client(user: LoginRequestSchema) -> FilesClient:
    """
    Функция создает и настраивает готовый FilesClient

    :return: Возвращает настроенный готовый FilesClient
    """
    return FilesClient(client=get_private_http_client(user=user))
