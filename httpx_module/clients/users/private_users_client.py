from httpx import Response

from httpx_module.clients.api_client import APIClient
from httpx_module.clients.private_http_builder import get_private_http_client
from httpx_module.clients.auth.auth_schema import LoginRequestSchema
from httpx_module.clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema

class PrivateUsersClient(APIClient):
    """
    Приватный клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения информации о пользователе

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")
    
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")
    
    def patch_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод частичного обновления пользователя по идентификатору

        :param user_id: Идентификатор пользователя
        :param request: Словарь с email, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))
    
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору

        :param user_id: Идентификатор пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")
    
    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения данных о пользователе

        :param user_id: Идентификатор пользователя
        :return: Возвращает данные пользователя
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)
    
def get_private_users_client(user: LoginRequestSchema) -> PrivateUsersClient:
    """
    Функция для создания настроенного PrivateUsersClient

    :return: Возвращает готовый настроенный экземпляр PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user=user))